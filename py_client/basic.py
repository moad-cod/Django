import requests

endpoint = "http://localhost:8000/api/"

# HTTP Request -> HTML
# REST API HTTP Request -> JSON (JavaScript Object Notation)

get_response = requests.get(endpoint) # API (Application Programming Interface) -> Web Api
print(get_response.json()['message']) # print raw text response