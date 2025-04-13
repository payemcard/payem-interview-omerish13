from models.base import Request, CustomJSONEncoder, CustomJSONDecoder
from pathlib import Path
import json


# db = [
#     {
#         'id': 1,
#         'name': 'Purchase Request 1',
#         'description': 'Request to purchase office supplies',
#         'amount': 100,
#         'currency': 'USD',
#         'employee_name': 'John Doe',
#         'status': 'Pending',
#         'created_at': datetime(2024, 7, 19, 8, 30, 0),
#         'updated_at': None,
#         'approved_amount': 90
#     },
#     {
#         'id': 2,
#         'name': 'Reimbursement Request 1',
#         'description': 'Reimbursement for travel expenses',
#         'amount': 150,
#         'currency': 'EUR',
#         'employee_name': 'Jane Smith',
#         'status': 'Approved',
#         'created_at': datetime(2024, 7, 18, 10, 15, 0),
#         'updated_at': datetime(2024, 7, 20, 14, 20, 0),
#         'approved_amount': 140
#     },
#     {
#         'id': 3,
#         'name': 'Purchase Request 2',
#         'description': 'Request to purchase new laptops',
#         'amount': 80,
#         'currency': 'USD',
#         'employee_name': 'Alice Johnson',
#         'status': 'Pending',
#         'created_at': datetime(2024, 7, 17, 12, 45, 0),
#         'updated_at': None,
#         'approved_amount': 75
#     },
#     {
#         'id': 4,
#         'name': 'Reimbursement Request 2',
#         'description': 'Reimbursement for conference fees',
#         'amount': 120,
#         'currency': 'EUR',
#         'employee_name': 'Bob Brown',
#         'status': 'Approved',
#         'created_at': datetime(2024, 7, 16, 9, 0, 0),
#         'updated_at': datetime(2024, 7, 18, 11, 30, 0),
#         'approved_amount': 110
#     },
#     {
#         'id': 5,
#         'name': 'Purchase Request 3',
#         'description': 'Request to purchase marketing materials',
#         'amount': 200,
#         'currency': 'USD',
#         'employee_name': 'Eve Green',
#         'status': 'Pending',
#         'created_at': datetime(2024, 7, 15, 14, 20, 0),
#         'updated_at': None,
#         'approved_amount': 180
#     },
#     {
#         'id': 6,
#         'name': 'Reimbursement Request 3',
#         'description': 'Reimbursement for team building event',
#         'amount': 90,
#         'currency': 'EUR',
#         'employee_name': 'Chris White',
#         'status': 'Approved',
#         'created_at': datetime(2024, 7, 14, 11, 10, 0),
#         'updated_at': datetime(2024, 7, 17, 16, 45, 0),
#         'approved_amount': 85
#     },
#     {
#         'id': 7,
#         'name': 'Purchase Request 4',
#         'description': 'Request to purchase software licenses',
#         'amount': 110,
#         'currency': 'USD',
#         'employee_name': 'Grace Black',
#         'status': 'Pending',
#         'created_at': datetime(2024, 7, 13, 9, 30, 0),
#         'updated_at': None,
#         'approved_amount': 105
#     },
#     {
#         'id': 8,
#         'name': 'Reimbursement Request 4',
#         'description': 'Reimbursement for client entertainment',
#         'amount': 180,
#         'currency': 'EUR',
#         'employee_name': 'David Gray',
#         'status': 'Approved',
#         'created_at': datetime(2024, 7, 12, 13, 0, 0),
#         'updated_at': datetime(2024, 7, 15, 17, 0, 0),
#         'approved_amount': 170
#     },
#     {
#         'id': 9,
#         'name': 'Purchase Request 5',
#         'description': 'Request to purchase office furniture',
#         'amount': 95,
#         'currency': 'USD',
#         'employee_name': 'Emma Brown',
#         'status': 'Pending',
#         'created_at': datetime(2024, 7, 11, 16, 45, 0),
#         'updated_at': None,
#         'approved_amount': 90
#     },
#     {
#         'id': 10,
#         'name': 'Reimbursement Request 5',
#         'description': 'Reimbursement for training course',
#         'amount': 130,
#         'currency': 'EUR',
#         'employee_name': 'Frank Johnson',
#         'status': 'Approved',
#         'created_at': datetime(2024, 7, 10, 8, 0, 0),
#         'updated_at': datetime(2024, 7, 13, 10, 30, 0),
#         'approved_amount': 120
#     }
# ]


class Database:
    def __init__(self):
        self.db = []
        self.next_id = len(self.db) + 1

    def get_db(self) -> list:
        """
        This function returns the database.
        It returns a list of dictionaries, each representing a request.
        :return:
        list: A list of dictionaries representing all requests in the database.
        """
        return self.db

    def get_next_id(self) -> int:
        """
        This function returns the next ID for a new request.
        :return:
        int: The next ID for a new request.
        """
        return self.next_id

    def add_request(self, row: Request) -> None:
        """
        This function adds a new request to the database.
        :param row:
        Request: A dictionary representing the request to be added.
        :return:
        None
        :raises ValueError: If the request is invalid.
        """
        self.db.append(row)
        self.next_id = len(self.db) + 1
        self.write_db()

    def write_db(self) -> None:
        """
        This function writes the database to a JSON file.
        It serializes the database using a custom JSON encoder.
        :return:
        None
        :raises FileNotFoundError: If the database file does not exist.
        """
        with Path("db.json").open("w") as f:
            f.write(json.dumps(self.db, cls=CustomJSONEncoder))

    def read_db(self) -> None:
        """
        This function reads the database from a JSON file.
        It deserializes the database using a custom JSON decoder.
        :return:
        None
        :raises FileNotFoundError: If the database file does not exist.
        """
        with Path("db.json").open("r") as f:
            self.db = json.loads(f.read(), cls=CustomJSONDecoder)
            self.next_id = len(self.db) + 1

    def get_request(self, request_id: int) -> dict:
        """
        This function retrieves a specific request from the database by its ID.
        :param request_id:
        int: The ID of the request to retrieve.
        :return:
        dict: A dictionary representing the request with the given ID.
        :raises ValueError: If the request ID is out of range.
        """
        if request_id < 1 or request_id > len(self.db):
            raise ValueError("Request ID out of range")
        return self.db[request_id - 1]


db = Database()
try:
    db.read_db()
except FileNotFoundError:
    # If the database file does not exist, create an empty database
    db.write_db()