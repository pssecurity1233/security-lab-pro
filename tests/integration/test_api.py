"""Integration tests for API"""
import requests

def test_api_status():
    response = requests.get('http://localhost:8888/api/v1/status')
    assert response.status_code == 200
