import requests

# =================================================================
# 1. FILL THIS IN WITH YOUR FRESH CODE (Expires in 10 minutes!)
# =================================================================
AUTHORIZATION_CODE = "1000.31bbb8df547cba5ffb05a559649a27f1.8174b49b1938d662f16777aff1db0dcc"

# =================================================================
# 2. KEEP THESE EXACTLY AS THEY ARE (Since they finally worked!)
# =================================================================
CLIENT_ID = "1000.T6CA5QCKE0ZD8W9PPMY3819F81K6MB"  # Using your ID from the image
CLIENT_SECRET = "3496f7aeb48ee952e457511d479daae7c6f27816f8"

# We are using .in because it's the right endpoint for your region
TOKEN_URL = "https://accounts.zoho.com/oauth/v2/token"

payload = {
    "code": AUTHORIZATION_CODE,
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "redirect_uri": "http://localhost:8080/zoho_oauth/callback",
    "grant_type": "authorization_code"
}

print("Sending request to Zoho to fetch tokens...")
response = requests.post(TOKEN_URL, data=payload)

# Safely handle the response without crashing if it's not JSON
try:
    data = response.json()
    if "refresh_token" in data:
        print("\n🎉 SUCCESS! Here is your token:")
        print("-" * 60)
        print(f"REFRESH_TOKEN : {data.get('refresh_token')}")
        print("-" * 60)
        print("Copy the long string above into your Streamlit secrets file.")
    else:
        print("\n❌ Zoho replied, but did not return a refresh token. Response:")
        print(data)
except Exception:
    print(f"\n❌ Server did not return JSON. HTTP Status Code: {response.status_code}")
    print("Raw Response text below:")
    print(response.text[:500])  # Print first 500 characters of the error page