import requests
url = 'https://api.github.com/emojis'
responses = requests.get(url)
request = responses.request
request.url
print(request.url)
print(request.method)
print(request.headers)
print(responses.status_code)
print(responses.headers.get('Content-Type'))
emojis = responses.json()
print(emojis["partying_face"])
