import requests

url = "https://www.hadithgpt.com/api/context"
headers = {
    "Content-Type": "application/json",
}

payload = {
    "question": "visiting the sick",
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed with status code:", response.status_code)