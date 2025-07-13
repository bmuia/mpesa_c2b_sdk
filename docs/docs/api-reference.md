# API Reference

##  `register_url(short_code, response_type, confirmation_url, validation_url)`
Registers Confirmation and Validation URLs with Safaricom's C2B API.

### Parameters
- `short_code` (str): Paybill or Buy Goods shortcode
- `response_type` (str): "Completed" or "Cancelled"
- `confirmation_url` (str): URL to receive confirmation POST requests
- `validation_url` (str): URL to receive validation POST requests

### Returns

- JSON response from Safaricom API. Example:

```json
{
  "ConversationID": "AG_20230710_00006c77d4c123456789",
  "OriginatorCoversationID": "12345-67890-12345",
  "ResponseDescription": "Success"
}
```

---
## `simulate(short_code, command_id, amount, phone_number, account_ref)`

Simulates a C2B transaction in the sandbox.

### Parameters

- `short_code` (str): Paybill or Buy Goods shortcode
- `command_id` (str): Usually "CustomerPayBillOnline"
- `amount` (int/float): Transaction amount
- `phone_number` (str): Phone number making the payment
- `account_ref` (str): Reference for the transaction

### Returns

- JSON response from Safaricom API. Example:

```json
{
  "ConversationID": "AG_20230710_00006c77d4c123456789",
  "OriginatorCoversationID": "23456-78901-23456",
  "ResponseDescription": "Accept the service request successfully."
}
```
