# Getting Started

## Prerequisites

Before installing and using the SDK, ensure you have the following:

- ✅ **Python 3.7+** installed on your system.
- 🌐 **Public URLs for confirmation and validation** (required by Safaricom to receive transaction callbacks).
- 🔐 **Safaricom Developer Credentials** (Consumer Key and Consumer Secret).
- 🧪 For testing: an account on [Safaricom Developer Portal](https://developer.safaricom.co.ke/) with access to the sandbox environment.
- ⚙️ A `.env` file in your project root with the following content:

```env
ENVIRONMENT=sandbox
# Sandbox credentials
CONSUMER_KEY_SANDBOX=your_sandbox_key
CONSUMER_SECRET_SANDBOX=your_sandbox_secret
BASE_URL_SANDBOX=[https://sandbox.safaricom.co.ke/](https://sandbox.safaricom.co.ke/)
```

---

## Installation

Install the SDK via pip:

```bash
pip install mpesa-c2b-sdk
```

## Quick Example
```python
from mpesa_c2b_sdk.payments import register_url, simulate

# Register confirmation and validation URLs
register_url(
    short_code="600584",
    response_type="Completed",
    confirmation_url="https://yourdomain.com/confirmation",
    validation_url="https://yourdomain.com/validation"
)

# Simulate a C2B payment (sandbox only)
simulate(
    short_code="600584",
    command_id="CustomerPayBillOnline",
    amount=100,
    phone_number="2547XXXXXXXX",
    account_ref="INV001"
)

```


## 📌 Important Note for Local Testing

When testing locally (e.g., using `http://localhost:8000/...`), **Safaricom's servers cannot access your confirmation and validation endpoints** because they must be publicly accessible.

### ✅ Recommended Solution

Use [ngrok](https://ngrok.com/) to expose your local server to the internet.

### Steps:

1. Install and start ngrok:

```bash
ngrok http 8000
```

2. ngrok will give you a public URL like:

```bash
https://your-ngrok-subdomain.ngrok.io
``` 

3. Replace your local callback URLs with the public ones in your code:

```bash
confirmation_url = "https://your-ngrok-subdomain.ngrok.io/api/confirmation/"
validation_url = "https://your-ngrok-subdomain.ngrok.io/api/validation/"
```

This will allow Safaricom to send real-time callback data to your local app during sandbox testing.