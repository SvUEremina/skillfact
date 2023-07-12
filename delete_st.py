import requests

#res = requests.delete(url, **kwargs)

params = {
  'status': 'available'
}

headers = {
  'accept': 'application/json',
}

data = {
  "id": 0,
  "username": "svsaz",
  "firstName": "sonya",
  "lastName": "Milk",
  "email": "sv123@mail.ru",
  "password": "somi5555",
  "phone": "89121234567",
  "userStatus": 0
}

res1 = requests.delete(f'https://petstore.swagger.io/v2/user/svsaz', headers=headers, json=data)
print(res1.status_code)
print(res1.text)
print(res1.json())
print(type(res1.json()))
