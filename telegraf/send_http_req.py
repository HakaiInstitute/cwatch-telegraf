import sys
import requests
import json
import os

url = os.environ.get('PLAUSIBLE_URL','http://plausible.server.cioospacific.ca/api/event')

for line in sys.stdin:
    sys.stdout.write(line)
    json_obj = json.loads(line)
    headers = {
      "User-Agent": json_obj['agent'],
      "X-Forwarded-For": json_obj['host'],
      "Content-Type": "application/json"
    }
    x = requests.post(url, json = json_obj, headers = headers)
    sys.stdout.write(x.text)



