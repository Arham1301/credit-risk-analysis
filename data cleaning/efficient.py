import requests

# Specify the API endpoint URL
api_url = 'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}'  # Replace with your API endpoint

try:
    # Make a GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Print the response data
        print("Response data:")
        print(data)
    else:
        print(f"Request failed with status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")

