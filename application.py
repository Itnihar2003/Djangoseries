import requests
url="http://127.0.0.1:8000/singstudent/1"
pop=requests.get(url=url)
show= pop.json()
print(show)