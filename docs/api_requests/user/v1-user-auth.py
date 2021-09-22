import requests
import json

url = 'http://localhost:8888'

url += '/v1/user/auth'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'email': 'a.anisimov@lab15.ru',
    'password': 'AdminPassword123',
}

if __name__ == '__main__':
    response = requests.post(url, headers=headers, data=data)
    print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))
