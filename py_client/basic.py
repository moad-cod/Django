import requests

endpoint = "http://localhost:8000/api/"

# HTTP Request -> HTML
# REST API HTTP Request -> JSON (JavaScript Object Notation)

get_response = requests.get(endpoint, params={"abc": 123}, json={"query": "Hellow World"}) # API (Application Programming Interface) -> Web Api
print(get_response.headers)
print(get_response.text)


# print(get_response.json()) # print raw text response