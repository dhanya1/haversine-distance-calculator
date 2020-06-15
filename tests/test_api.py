from intercom_app import create_app, controller
import configuration
import unittest
from os import path


class TestRequestCreateAPIs(unittest.TestCase):

    def setUp(self):
        self.test_app = create_app("configuration.TestConfig")
        self.app = self.test_app.test_client()
        self.filename = path.join(path.dirname(path.abspath(__file__)),
                             "test_customers.txt")

    def test_home(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def create_request(self, data=None):
        return self.app.post('/distance_calculator/',
                             data=data,
                             content_type='multipart/form-data')

    def test_create_request_no_file(self):
        response = self.create_request()
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'File not received', response.data)

    def test_create_request_invalid_data(self):
        data = {"range":10}
        response = self.create_request(data)
        self.assertIn(b'File not received', response.data)
        self.assertEqual(response.status_code, 400)

    def test_create_product_valid_data(self):
        data = dict(
            file=(open(self.filename,"rb"), "customer.txt"))
        response = self.create_request(data)
        self.assertIn(b'customers_in_range', response.data)
        self.assertEqual(response.status_code, 200)


class TestDistanceCalculator(unittest.TestCase):
    def setUp(self):
        self.test_app = create_app("configuration.TestConfig")
        self.app = self.test_app.test_client()
        self.filename = path.join(path.dirname(path.abspath(__file__)),
                                  "test_customers.txt")

    def test_get_single_row(self):
        generator = controller.get_single_row(self.filename)
        data = next(generator) # Generates one value at a time

        known_first_row = {"latitude": "52.986375",
                           "user_id": 12,
                           "name": "Christina McArdle",
                           "longitude": "-6.043701"}
        self.assertEqual(data, known_first_row)

    def test_calculate_distance_from_office(self):
        data = {"latitude": "52.986375",
                           "user_id": 12,
                           "name": "Christina McArdle",
                           "longitude": "-6.043701"}
        distance = controller.calculate_distance_from_office(data["latitude"],
                                                             data["longitude"])
        known_distance = 41.7687
        self.assertEqual(known_distance, round(distance,4))

    def test_customers_in_range(self):
        res = controller.get_customers_in_range(self.filename)
        # Distances of customers within range specified. Range is 100 here
        known_customers_list = [(12, 'Christina McArdle')]
        self.assertEqual(res, known_customers_list)


if __name__ == '__main__':
    unittest.main()