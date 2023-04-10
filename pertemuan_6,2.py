import requests
from pprint import pprint

r = requests.get('https://jsonplaceholder.typicode.com/pos/101')
data = r.json()
pprint(data)

post = {
    'body' : "Lorem ipsum",
    'title' : "Title",
    'userId' : 5,
}

req = requests.post('https://jsonplaceholder.typicode.com/posts/5', json=post)
print(req.json())

update_post = post 
update_post['id'] = 5

rep = requests.put(
    'https://jsonplaceholder.typicode.com/posts/5', json=updae_post)
print(req.json())  