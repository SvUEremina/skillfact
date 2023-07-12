import requests

#res = requests.put(url, data=data)

params = {
  'status': 'available'
}

headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
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

res2 = requests.put(f'https://petstore.swagger.io/v2/user/svsaz', json=data)

print(res2.status_code)
print(res2.text)
print(res2.json())
print(type(res2.json()))
