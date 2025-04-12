import pytest

from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""

    # Set the testing configuration for the Flask app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_requests(client):
    """Test the GET /api/requests route."""
    response = client.get('/api/requests')
    assert response.status_code == 200
    # Check if the response is a list
    assert isinstance(response.json, list)
    # Check if the list is not empty
    assert len(response.json) > 0

def test_create_request(client):
    """Test the POST /api/requests route."""
    request_data = {
        'name': 'Purchase Request 6',
        'description': 'Request to purchase office supplies',
        'amount': 100,
        'currency': 'USD',
        'employee_name': 'John Doe',
        'status': 'Pending',
        'request_type': 'Purchase'
    }
    response = client.post('/api/requests', json=request_data)
    assert response.status_code == 201
    assert response.json['amount'] == request_data['amount']
    assert response.json['description'] == request_data['description']
    assert response.json['status'] == 'Pending'

def test_get_request(client):
    """Test the GET /api/requests/<request_id> route."""
    response = client.get('/api/requests/1')
    assert response.status_code == 200
    assert response.json['id'] == 1
    assert response.json['name'] == 'Purchase Request 1'
    assert response.json['status'] == 'Declined'

def test_approve_request(client):
    """Test the PUT /api/requests/<request_id>/approve route."""
    request_data = {
        'approved_amount': 90.0
    }
    response = client.put('/api/requests/1/approve', json=request_data)
    assert response.status_code == 200
    assert response.json['status'] == 'Approved'
    assert response.json['approved_amount'] == request_data['approved_amount']

def test_decline_request(client):
    """Test the PUT /api/requests/<request_id>/decline route."""
    response = client.put('/api/requests/1/decline')
    assert response.status_code == 200
    assert response.json['status'] == 'Declined'

def test_bad_request(client):
    """Test the POST /api/requests route with invalid data."""
    request_data = {
        'name': 'Invalid Request',
        'description': 'Request with missing fields',
        # Missing amount, currency, employee_name, status
    }
    response = client.post('/api/requests', json=request_data)
    assert response.status_code == 400
    assert 'error' in response.json

def test_not_found(client):
    """Test the GET /api/requests/<request_id> route with a non-existent request."""
    response = client.get('/api/requests/999')
    assert response.status_code == 404
    assert 'error' in response.json

def test_approve_request_not_found(client):
    """Test the PUT /api/requests/<request_id>/approve route with a non-existent request."""
    request_data = {
        'approved_amount': 90.0
    }
    response = client.put('/api/requests/999/approve', json=request_data)
    assert response.status_code == 404
    assert 'error' in response.json

def test_decline_request_not_found(client):
    """Test the PUT /api/requests/<request_id>/decline route with a non-existent request."""
    response = client.put('/api/requests/999/decline')
    assert response.status_code == 404
    assert 'error' in response.json