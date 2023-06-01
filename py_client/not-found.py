import requests

endpoint = "http://localhost:8000/api/products/1thtu87568gu"

get_response = requests.get(endpoint)
print(get_response.json())
