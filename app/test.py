import requests


res = requests.post("http://localhost:5000/reflect", json={"csrf": "1234"})

print(res.status_code)
print(res.content)