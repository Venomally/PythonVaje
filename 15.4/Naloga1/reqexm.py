import requests
import json

res_post = requests.post('http://127.0.0.1:1234/welcome')
res_get = requests.get('http://127.0.0.1:1234/welcome')

res_get.text, res_post.text

res = requests.get('http://149.62.71.186:1234/welcome')
res = requests.post('http://149.62.71.186:1234/welcome')
res_post = requests.post('http://127.0.0.1:1234/puttext', data = 'osmosem')
res_post.text
res_post = requests.post('http://127.0.0.1:1234/postjson', json={'name': 'Martin', 'surname' : 'Brešar'})
res_post.text
res_get = requests.get('http://149.62.71.186:1234/welcome')
res_get.text
