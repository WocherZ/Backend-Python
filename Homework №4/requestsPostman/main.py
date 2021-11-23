import requests

# http://127.0.0.1:8000/shop/
# http://127.0.0.1:8000/shop/category/
# http://127.0.0.1:8000/shop/category/123/
# http://127.0.0.1:8000/user/cart
url = "http://127.0.0.1:8000/shop/category/123/"

# GET request
r = requests.get(url)

print(r.text)

# POST request
r1 = requests.post(url, data={'key': 'value'})

print(r1.text)
