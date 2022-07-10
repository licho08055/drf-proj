import requests


 
endpoint =   "http://127.0.0.1:8000/api/products/5/update/"
data={
    'title': ' badmuqs',
    'content':'pet',
    'price': 3.33,
    'sale_price':44.4,
}

get_response = requests.put(endpoint, json=data )
print(get_response.json() ) 