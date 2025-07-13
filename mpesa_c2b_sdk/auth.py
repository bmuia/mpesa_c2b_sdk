from .config import CONSUMER_KEY, CONSUMER_SECRET, BASE_URL
import base64
import requests


def get_access_tokens():
    """
    Generate an OAuth access token from Safaricom's M-Pesa API.

    This token is required to authenticate all subsequent API requests.
    """

    # Combine consumer key and secret into a single string as required by OAuth 2.0 spec
    credentials = f"{CONSUMER_KEY}:{CONSUMER_SECRET}"

    # Encode the credentials using base64 (this is what Safaricom API expects)
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    # Set the HTTP Authorization header with encoded credentials
    headers = {
        "Authorization": f"Basic {encoded_credentials}"
    }

    # URL to request an access token (grant_type must be 'client_credentials')
    url = f"{BASE_URL}oauth/v1/generate?grant_type=client_credentials"

    # Make the GET request to Safaricom to obtain the access token
    response = requests.get(url, headers=headers)

    # Parse the JSON response from Safaricom
    response_json = response.json()

    # Check if the access_token key exists in the response
    if "access_token" not in response_json:
        raise Exception(f"Error fetching access_token: {response_json}")

    # Return the token so it can be used in authenticated API calls
    return response_json["access_token"]
