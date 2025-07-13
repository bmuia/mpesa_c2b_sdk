from .auth import get_access_tokens
from .config import BASE_URL
import requests


def register_url(short_code, response_type, confirmation_url, validation_url):
    """
    Registers application's Confirmation and Validation URLs with Safaricom's C2B API.

    Parameters:
    - short_code: Your Paybill or Buy Goods short code (assigned by Safaricom)
    - response_type: "Completed" or "Cancelled" (how Safaricom handles timeout responses)
    - confirmation_url: Public URL that will receive payment confirmations (POST)
    - validation_url: Public URL that will handle payment validations (POST)

    Returns:
    - JSON response from Safaricom API
    """

    # Fetch the OAuth access token
    access_token = get_access_tokens()

    # Set Authorization header with Bearer token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Build the request payload
    payload = {
        "ShortCode": short_code,
        "ResponseType": response_type,
        "ConfirmationURL": confirmation_url,
        "ValidationURL": validation_url
    }

    # Register URLs endpoint
    url = f"{BASE_URL}mpesa/c2b/v1/registerurl"

    # Send POST request to Safaricom API
    response = requests.post(url, headers=headers, json=payload)

    # Return the JSON response
    return response.json()



def simulate(short_code, command_id, amount, phone_number, account_ref):
    """
    Simulates a C2B transaction for testing purposes using Safaricom's sandbox.

    Parameters:
    - short_code: Your Paybill or Buy Goods short code (e.g., 600999 for sandbox)
    - command_id: Usually "CustomerPayBillOnline" or "CustomerBuyGoodsOnline"
    - amount: Amount to be sent in the transaction
    - phone_number: The MSISDN (e.g., 254712345678) simulating the payment
    - account_ref: Reference number for the bill (any string like 'INV001')

    Returns:
    - JSON response from Safaricom API
    """

    # Get the access token
    access_token = get_access_tokens()
    
    # Prepare headers
    headers = {
        'Authorization': f"Bearer {access_token}",
        'Content-Type': 'application/json'
    }

    # Prepare payload 
    payload = {
        "ShortCode": short_code,
        "CommandID": command_id,
        "Amount": amount,
        "Msisdn": phone_number,
        "BillRefNumber": account_ref
    }

    # Simulation endpoint
    url = f"{BASE_URL}/mpesa/c2b/v1/simulate"

    # Make the POST request
    response = requests.post(url, headers=headers, json=payload)

    return response.json()
