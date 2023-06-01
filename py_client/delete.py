import requests

product_id = input("input product id: ")
try:
    product_id = int(product_id)
except:
    product_id = None
    print("id must be an integer {product_id}")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code == 204)
