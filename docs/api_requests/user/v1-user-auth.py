import requests
import json

url = 'http://localhost:8888'

url += '/v1/user/auth'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
data_admin = {
    'email': 'a.anisimov@lab15.ru',
    'password': 'AdminPassword123',
}
data_user = {
    'email': 's.ivanov@lab15.ru',
    'password': 'UserPassword123',
}

if __name__ == '__main__':
    response = requests.post(url, headers=headers, data=data_user)
    print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))
