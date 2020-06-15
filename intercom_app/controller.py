import json
from math import radians, sin, cos, asin, sqrt
from os import environ

AVG_EARTH_RADIUS_KM = 6371


def get_single_row(file_path):
    """
    This function is a generate, that reads single json line and converts
    hashmap(dictionary in python) and yields it. We can read infinite lines
    without running out of memory.
    :param file_path: The location of the file you want to read
    :return:
    """

    try:
        with open(file_path) as file_handler:
            for line in file_handler:
                yield json.loads(line)
    except FileNotFoundError:
        raise FileNotFoundError(
            "File {} does not exist. Please ensure you have sent full "
            "path to the file".format(file_path))


def calculate_distance_from_office(cust_lat, cust_lang):
    """
    :param lat: Latitude of customer location
    :param lng: Longitude of customer location
    :return: Distance between Intercom office and Customer in Kilometers
     using the Haversine's formula.
    """
    o_lat, o_lng, cust_lat, cust_lng = map(radians, [
                                    float(environ.get("OFFICE_LATITUDE")),
                                    float(environ.get("OFFICE_LONGITUDE")),
                                    float(cust_lat), float(cust_lang)])

    lat_diff, lng_diff = cust_lat - o_lat, cust_lng - o_lng


    # Source: Great-circle distance
    # https://en.wikipedia.org/wiki/Great-circle_distance
    tmp = sin(lat_diff/2) ** 2 + cos(o_lat) * cos(cust_lat) * sin(lng_diff/2) \
         ** 2

    dist_in_km = 2 * AVG_EARTH_RADIUS_KM * asin(sqrt(tmp))
    return dist_in_km


def get_customers_in_range(customer_file='customers.txt', range=100):
    """
    :param customer_file: Full path to a file with customer details, defaults
     to customers.txt in current location.
    :param distance_allowed: distance in Km within which the customer should
     be located, defaults to 100 km.
    :return: Prints the names and ID of customers within allowed range to
     STDOUT sorted by customer ID.
    """
    customers_in_range = []

    # Scalable to very large files as we yield one line at a time, data not
    # held in memory
    for row in get_single_row(customer_file):
        distance_from_office = calculate_distance_from_office(
                                    row['latitude'],
                                    row['longitude'])
        if distance_from_office <= range:
            customers_in_range.append((row['user_id'], row['name']))
    return sorted(customers_in_range)


if __name__ == "__main__":
    get_customers_in_range(
        customer_file="/Users/dhanyajayachandra/PycharmProjects/intercom/customers.txt")