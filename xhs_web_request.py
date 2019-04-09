from urllib. request import ProxyHandler, build_opener
import requests

proxy ='127.0.0.1:9743'

proxies = {
    'http':'http://' + proxy,
    'https':'https://' + proxy
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

try:
    response = requests.get('http://httpbin.org/get', proxies=proxies, headers=headers)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)