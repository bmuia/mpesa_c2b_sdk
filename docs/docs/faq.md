# FAQ

### ❓ Does this package support real payments?

**Not yet.** Support for real payments will be introduced in the next release version. Stay tuned!

---

### ❓ How do I test payments?

Use the sandbox environment by setting `ENVIRONMENT=sandbox` in your configuration. This allows you to simulate payments without triggering real transactions.

---

### ❓ Can I customize the phone number used?

Yes. The `simulate` function accepts a phone number parameter, allowing you to specify any valid test MSISDN (e.g., `2547XXXXXXXX`).

---

### ❓ Can I customize the transaction amount?

Absolutely. You define the transaction amount in the `simulate` function as per your testing requirements.

---

### ❓ Can I store transaction details?

The SDK does not store transaction details by default. It's up to the developer to handle and persist the responses based on their application needs.
