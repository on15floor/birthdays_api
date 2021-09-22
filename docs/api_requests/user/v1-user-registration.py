import requests
import json

url = 'http://localhost:8888'

url += '/v1/user/registration'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'email': 'm.petrob@list.ru',
    # 'email': 'a.anisimov@lab15.ru',
    'password': 'Password123',
    'first_name': 'Михаил',
    'last_name': 'Петров',
}

if __name__ == '__main__':
    response = requests.post(url, headers=headers, data=data)
    print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))
