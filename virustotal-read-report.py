import requests
import os

api_key = os.environ.get("VIRUSTOTAL_API_KEY")

if not api_key:
    raise ValueError("VIRUSTOTAL_API_KEY is not set in Environment Variables")

def get_analysis_report(analysis_id):
    url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
    headers = {"x-apikey": api_key}
    return requests.get(url, headers=headers).json()

user_analysis_id = input("Enter analysis id: ")

report = get_analysis_report(user_analysis_id)
print(report["data"])


