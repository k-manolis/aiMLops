import os
import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/models"

# Create a temporary file for testing
@pytest.fixture
def model_file():
    model_path = 'test_model.pkl'
    with open(model_path, 'wb') as f:
        f.write(b"dummy_model_data")  # Add dummy data for testing
    #yield model_path
    os.remove(model_path)

# Test POST /models endpoint
def test_upload_model(model_file):
    files = {'model': open(model_file, 'rb')}
    data = {
        'name': 'test_model',
        'version': '1.0',
        'accuracy': '0.95'
    }
    response = requests.post(BASE_URL, files=files, data=data)
    assert response.status_code == 201
    assert response.json()['message'] == 'Model uploaded successfully'

# Test GET /models endpoint
def test_get_all_models():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert len(response.json()) > 0

# Test GET /models/{name} endpoint
def test_get_model_by_name():
    response = requests.get(f"{BASE_URL}/test_model")
    assert response.status_code == 200
    assert response.json()['name'] == 'test_model'

# Test GET /models/{name} for non-existent model
def test_get_model_not_found():
    response = requests.get(f"{BASE_URL}/non_existent_model")
    assert response.status_code == 404
    assert response.json()['error'] == 'Model not found'
