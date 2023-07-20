import requests

def get_api_response(url):
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Assuming the API returns JSON data, you can access it as a Python dictionary
            data = response.json()
            return data
        else:
            print(f"API call failed with status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error occurred during API call: {e}")
        return None

if __name__ == "__main__":
    # Example API URL: JSONPlaceholder API provides fake data for testing
    api_url = "https://jsonplaceholder.typicode.com/posts"

    # Make the API call and get the response
    api_response = get_api_response(api_url)

    if api_response:
        # Print the response data
        print(api_response)
    else:
        print("API call failed.")
