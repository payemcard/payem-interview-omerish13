from services.db import db, Request
from datetime import datetime
import pytz

# Set the timezone to Asia/Jerusalem
tz = pytz.timezone('Asia/Jerusalem')

def create_request(request_data: dict) -> dict:
    """
    This function creates a new request in the database.
    It takes a dictionary representing the request data as input.
    It assigns a new ID, sets the created_at and updated_at timestamps,
    and sets the status to "Pending".

    :param request_data: A dictionary representing the request data.

    :return: A dictionary representing the created request.

    :raises ValueError: If the request data is invalid.
    """
    # Assign a new ID to the request
    request_data['id'] = db.get_next_id()

    # Set the created_at and updated_at timestamps
    request_data['created_at'] = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    request_data['updated_at'] = request_data['created_at']

    # Set the status to "Pending" and approved_amount to None
    request_data['status'] = 'Pending'
    request_data['approved_amount'] = 0.0

    request = Request(**request_data)

    # Save the new request to the database
    db.add_request(request)

    return request_data

def approve_request(request_id: int, approved_amount: float) -> dict | None:
    """
    This function approves a request in the database.
    It takes the request ID as input and updates the status to "Approved",
    sets the approved_amount, and updates the updated_at timestamp.

    :param request_id: The ID of the request to approve.
    :param approved_amount: The amount to approve for the request.

    :return: The updated request data if found, otherwise None.

    :raises ValueError: If the request is not found.
    """
    # Get the request data from the database
    try:
        request_data = db.get_request(request_id)
    except ValueError as error:
        # Handle the error if the request is not found
        return {'error': str(error)}

    if request_data:
        # Update the status and approved_amount
        request_data['status'] = 'Approved'
        request_data['approved_amount'] = approved_amount
        request_data['updated_at'] = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

        # Save the updated request to the database
        db.write_db()
        return request_data

    return None

def decline_request(request_id: int) -> dict | None:
    """
    This function declines a request in the database.
    It takes the request ID as input and updates the status to "Declined"
    and updates the updated_at timestamp.

    :param request_id: The ID of the request to decline.

    :return: The updated request data if found, otherwise None.
    """
    # Get the request data from the database
    try:
        request_data = db.get_request(request_id)
    except ValueError as error:
        # Handle the error if the request is not found
        return {'error': str(error)}

    if request_data:
        # Update the status
        request_data['status'] = 'Declined'
        request_data['updated_at'] = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

        # Save the updated request to the database
        db.write_db()
        return request_data

    return None