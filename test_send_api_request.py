import pytest
import requests
import requests_mock

from send_api_request import get_api_response

# Replace 'send_request' with the actual name of the Python file containing the get_api_response function.

def test_get_api_response_success():
    # Define the API URL and the expected response data
    api_url = "https://jsonplaceholder.typicode.com/posts"
    expected_data = [{"userId": 1, "id": 1, "title": "foo", "body": "bar"}]

    # Mock the API response using requests_mock
    with requests_mock.Mocker() as m:
        m.get(api_url, json=expected_data)

        # Call the get_api_response function
        api_response = get_api_response(api_url)

    # Assert the response is as expected
    assert api_response == expected_data

def test_get_api_response_failure():
    # Define the API URL
    api_url = "https://jsonplaceholder.typicode.com/nonexistent"

    # Mock the API response with a non-successful status code
    with requests_mock.Mocker() as m:
        m.get(api_url, status_code=404)

        # Call the get_api_response function
        api_response = get_api_response(api_url)

    # Assert that the response is None for a failed API call
    assert api_response is None
