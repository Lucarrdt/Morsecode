import requests

response = requests.get('https://www.google.com')

response_json = response.json()

print(response_json)