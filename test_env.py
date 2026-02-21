import os
from dotenv import load_dotenv

# 1. Load the hidden .env file into memory
load_dotenv()

# 2. Grab the specific secret we want
secret = os.getenv("MY_SECRET_PASSWORD")

# 3. Print it to prove it works
if secret:
    print(f"✅ Success! The secret password is: {secret}")
else:
    print("❌ Uh oh, I couldn't find the .env file or the password.")