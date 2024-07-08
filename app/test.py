import requests

url = "http://localhost:5000/reflect"

res = requests.post(url, json={"csrf": "1234"})

print("Requesting the following url:", url)

print("\nServer status code:", res.status_code)
print("Server response:", res.content)