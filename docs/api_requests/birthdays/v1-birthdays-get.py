import requests
import json

url = 'http://localhost:8888'

url += '/v1/birthdays/get'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'auth-token': '15c1ee7a-bb97-42ef-a3ca-4c226543028e',
}

if __name__ == '__main__':
    response = requests.get(url, headers=headers)
    print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))
