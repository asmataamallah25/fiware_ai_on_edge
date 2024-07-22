import requests

# Define the API endpoint and parameters
url = "https://api.open-meteo.com/v1/forecast"

# Load parameters 
with open('config.json', 'r') as f:
    params = json.load(f)

try:
    # Make the API request
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Print the raw response content for debugging
    print("Response content:")
    print(response.text)

    # Parse the JSON response
    data = response.json()
    print("\nParsed JSON data:")
    print(data)  # Print the parsed JSON data

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except requests.exceptions.JSONDecodeError as e:
    print(f"JSON decode error: {e}")
    print("Raw response content:")
    print(response.text)