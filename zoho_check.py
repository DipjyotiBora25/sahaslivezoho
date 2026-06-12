import os
import re
import requests

# Load .env
env = {}
with open('.env', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        m = re.match(r'([^=]+)=(?:\"(.*)\"|(.*))', line)
        if m:
            key = m.group(1).strip()
            val = m.group(2) if m.group(2) is not None else m.group(3)
            env[key] = val

ZOHO_REFRESH_TOKEN = env.get('ZOHO_REFRESH_TOKEN')
ZOHO_CLIENT_ID = env.get('ZOHO_CLIENT_ID')
ZOHO_CLIENT_SECRET = env.get('ZOHO_CLIENT_SECRET')
ZOHO_TOKEN_URL = env.get('ZOHO_TOKEN_URL', 'https://accounts.zoho.com/oauth/v2/token')
ZOHO_ORG_ID = env.get('ZOHO_ORG_ID')

print('Using token url:', ZOHO_TOKEN_URL)
print('Org ID:', ZOHO_ORG_ID)

if not all([ZOHO_REFRESH_TOKEN, ZOHO_CLIENT_ID, ZOHO_CLIENT_SECRET, ZOHO_ORG_ID]):
    print('\nMissing one or more required vars:')
    for k in ['ZOHO_REFRESH_TOKEN','ZOHO_CLIENT_ID','ZOHO_CLIENT_SECRET','ZOHO_ORG_ID']:
        print(f' - {k}:', 'OK' if env.get(k) else 'MISSING')
    raise SystemExit(1)

# Exchange refresh token for access token
params = {
    'refresh_token': ZOHO_REFRESH_TOKEN,
    'client_id': ZOHO_CLIENT_ID,
    'client_secret': ZOHO_CLIENT_SECRET,
    'grant_type': 'refresh_token'
}
print('\nRequesting access token using refresh token...')
resp = requests.post(ZOHO_TOKEN_URL, data=params)
print('Token endpoint status:', resp.status_code)
try:
    j = resp.json()
    print('Token endpoint response:', j)
except Exception:
    print('Non-JSON token response:', resp.text[:500])
    raise SystemExit(1)

if 'access_token' not in j:
    print('\nFailed to obtain access token. Response:', j)
    raise SystemExit(1)

access_token = j['access_token']
print('\nObtained access token (len):', len(access_token))

# Try fetching invoices
headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}
url = f'https://www.zohoapis.com/books/v3/invoices?organization_id={ZOHO_ORG_ID}&per_page=1'
print('\nCalling invoices endpoint:', url)
r = requests.get(url, headers=headers)
print('Invoices endpoint status:', r.status_code)
try:
    print('Invoices response JSON:', r.json())
except Exception:
    print('Invoices raw response:', r.text[:1000])

print('\nDone')
