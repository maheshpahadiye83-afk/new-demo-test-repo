"""
Unit tests for the Flask application
"""

import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask application"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'running'
    assert 'message' in data


def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'


def test_api_info_endpoint(client):
    """Test the API info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    data = response.get_json()
    assert data['api_version'] == '1.0'
    assert 'endpoints' in data
    assert len(data['endpoints']) > 0


def test_404_not_found(client):
    """Test 404 error handling"""
    response = client.get('/nonexistent')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data


def test_response_headers(client):
    """Test response content type"""
    response = client.get('/')
    assert response.content_type == 'application/json'
