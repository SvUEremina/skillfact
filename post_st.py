import requests

#res = requests.post(url, headers=headers, data=data)
#data = {‘key1’: ‘value1’, ‘key2’: ‘value2’}.

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

res1 = requests.post(f'https://petstore.swagger.io/v2/user', headers=headers, json=data)
print(res1.status_code)
print(res1.text)
print(res1.json())
print(type(res1.json()))
