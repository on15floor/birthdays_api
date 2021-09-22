import requests
import json

url = 'http://localhost:8888'

url += '/v1/admin/delete_user'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'auth-token': '6fd56840-fe22-49a7-a49b-a62050018adb',
}
data = {
    'email': 'm.petrob@list.ru',
}

if __name__ == '__main__':
    response = requests.post(url, headers=headers, data=data)
    print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))
