import sys
import requests
import json
import os

url = os.environ.get(
    'GA_URL', 'http://www.google-analytics.com/mp/collect')
secret = os.environ.get(
    'GA_API_SECRET')
id = os.environ.get(
    'GA_MEASUREMENT_ID')

full_url = f"{url}?api_secret={secret}&measurement_id={id}"

for line in sys.stdin:
    sys.stdout.write(line)
    json_obj = json.loads(line)
    headers = {
      # "User-Agent": json_obj['agent'],
      # "X-Forwarded-For": json_obj['host'],
      "Content-Type": "application/json"
    }
    x = requests.post(full_url, json=json_obj, headers=headers)
    sys.stdout.write(x.text)



