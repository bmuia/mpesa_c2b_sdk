import os
from dotenv import load_dotenv

load_dotenv()

env = os.getenv("ENVIRONMENT", "sandbox").lower()

if env == "production":
    CONSUMER_KEY = os.getenv("CONSUMER_KEY_PROD")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET_PROD")
    BASE_URL = os.getenv("BASE_URL_PROD")
else:
    CONSUMER_KEY = os.getenv("CONSUMER_KEY_SANDBOX")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET_SANDBOX")
    BASE_URL = os.getenv("BASE_URL_SANDBOX")
