from services.db import db

def get_data() -> list | dict:
    """
    This function retrieves all requests from the database.
    It returns a list of dictionaries, each representing a request.

    :return:
    list: A list of dictionaries representing all requests in the database.
    """

    # Return the database content
    return db.get_db()

def get_request(request_id: int) -> dict:
    """
    This function retrieves a specific request from the database by its ID.
    It returns a dictionary representing the request.

    :param request_id: The ID of the request to retrieve.

    :return: A dictionary representing the request if found, otherwise None.
    """

    # Return the request with the given ID
    try:
        return db.get_request(request_id)
    except ValueError as error:
        # Handle the error if the request is not found
        return {'error': str(error)}