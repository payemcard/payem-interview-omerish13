from flask import (
    Blueprint,
    jsonify,
    request,
)
import datetime
import pytz
from services.get_data import (
    get_request as _get_request,
    get_data,
)
from services.post_data import (
    create_request as _create_request,
    approve_request as _approve_request,
    decline_request as _decline_request,
)
from pydantic import ValidationError

tz = pytz.timezone('Asia/Jerusalem')

requests = Blueprint('requests', __name__, url_prefix='/api/requests')



@requests.route('', methods=['GET'])
def get_requests():
    return jsonify(get_data())


@requests.route('', methods=['POST'])
def create_request():

    request_data = request.json
    if not request_data:
        return jsonify({'error': 'Invalid request data'}), 400
    try:
        response = _create_request(request_data)
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify(response), 201

@requests.route('/<int:request_id>', methods=['GET'])
def get_request(request_id: int):

    response = _get_request(request_id)
    if 'error' in response:
        return jsonify(response), 404
    return jsonify(_get_request(request_id)), 200

@requests.route('/<int:request_id>/approve', methods=['PUT'])
def approve_request(request_id: int):
    request_data = request.json
    if not request_data or 'approved_amount' not in request_data:
        return jsonify({'error': 'Invalid request data'}), 400
    response = _approve_request(request_id, request_data['approved_amount'])
    if 'error' not in response:
        return jsonify(response), 200
    return jsonify(response), 404

@requests.route('/<int:request_id>/decline', methods=['PUT'])
def decline_request(request_id: int):
    response = _decline_request(request_id)
    if 'error' not in response:
        return jsonify(response), 200
    return jsonify(response), 404