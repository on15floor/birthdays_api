import requests
import json

url = 'http://localhost:8888'

url += '/v1/version'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

if __name__ == '__main__':
    response = requests.get(url, headers=headers)
    print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))
