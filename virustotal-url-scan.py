import requests
import os

api_key = os.environ.get("VIRUSTOTAL_API_KEY")

if not api_key:
    raise ValueError("VIRUSTOTAL_API_KEY is not set in Environment Variables")

data = {"url": "URLToScan"}
headers = {"x-apikey": api_key}
        
response = requests.post("https://www.virustotal.com/api/v3/urls", data=data, headers=headers)

if response.ok:
    print("Request was successful")
    print(response.json())
else:
    print("Problem with request")
    print(response.json())
