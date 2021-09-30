import requests
import json

url = 'http://localhost:8888'

url += '/v1/admin/get_statistic'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'auth-token': 'f498cdfa-45d1-4c81-8f8c-8f482ed18dee',
}

if __name__ == '__main__':
    response = requests.get(url, headers=headers)
    print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))
