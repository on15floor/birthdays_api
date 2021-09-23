import requests
import json

url = 'http://localhost:8888'

url += '/v1/birthdays/del'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'auth-token': '15c1ee7a-bb97-42ef-a3ca-4c226543028e',
}
data = {
    'birthday_id': 10,
}

if __name__ == '__main__':
    response = requests.post(url, headers=headers, data=data)
    print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))
