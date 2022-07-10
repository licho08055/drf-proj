import requests


endpoint = " http://127.0.0.1:8000/api/products/create/"

data = {
    "title":"than gang me",
    "content":"oral",
    "price":22.44,
    "sale_price":"99.22"
    
    
}

get_response = requests.get(endpoint, json=data)
print(get_response.json())