# MPESA C2B SDK

A simple Python SDK to help developers integrate with Safaricom’s Daraja API for Customer to Business (C2B) payments. Easily register your confirmation and validation URLs and simulate payments in the sandbox environment.

## Features

* Register Confirmation and Validation URLs
* Simulate C2B payments in sandbox
* Supports environment variables for configuration

## Installation

```bash
pip install mpesa-c2b-sdk
```

## Quick start
```python
from mpesa_c2b_sdk.payments import register_url, simulate

register_url(
    short_code="600584",
    response_type="Completed",
    confirmation_url="[https://yourdomain.com/confirmation](https://yourdomain.com/confirmation)",
    validation_url="[https://yourdomain.com/validation](https://yourdomain.com/validation)"
)

simulate(
    short_code="600584",
    command_id="CustomerPayBillOnline",
    amount=100,
    phone_number="2547XXXXXXXX",
    account_ref="INV001"
)
```

## Notes
1. When testing locally, use a tool like ngrok to expose your confirmation and validation URLs to the internet.

2. Set your environment (sandbox or production) and API credentials in a .env file.