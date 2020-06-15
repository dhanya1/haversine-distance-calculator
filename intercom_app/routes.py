from flask import Blueprint, jsonify, request, current_app
from werkzeug.utils import secure_filename
from intercom_app.controller import get_customers_in_range
from os import path, environ


distance_calculator = Blueprint('distance_calculator', __name__)


@distance_calculator.errorhandler(404)
def handle_invalid_usage(error):
    error = error.to_dict()
    error["hint"] = "Please ensure you have added trailing / at end of endpoint"
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@distance_calculator.route('/')
@distance_calculator.route('/home/')
def hello():
    return "Hello"


@distance_calculator.route("/distance-calculator/", methods=['GET', 'POST'])
@distance_calculator.errorhandler(404)
def distance():
    if request.method == "GET":
        return "Reachable"

    # Primitive validation of the request.
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type', '')
        if 'multipart/form-data' not in content_type:
            return jsonify(
                {'error': 'Content-Type header is not set to '
                          'multipart/formdata'}), 400

        # Validate the file type
        file_received = request.files.get('file')

        if not file_received:
            return jsonify({'error': 'File not received'}), 400

        # Ensure the uploaded file is safe, using secure_filename to combat
        # threats.
        file_extension = path.splitext(file_received.filename)[1].strip()
        print(file_extension)
        if file_extension != ".txt":
            return jsonify({'message': 'Only ".txt"'
                                       ' files are accepted'}), 400

        filename = path.join(current_app.config.get("DOWNLOAD_DIR"),
                             secure_filename(file_received.filename))
        file_received.save(filename)

        # Config value
        distance = request.form.get("distance", current_app.config.get("RANGE"))

        # Find customers in range.
        customers_in_range = \
            get_customers_in_range(filename,
                                   range=int(distance))
        return jsonify({"customers_in_range": customers_in_range})