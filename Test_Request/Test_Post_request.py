import requests


url = ("http://localhost:8000/loaddata")

response = requests.post(url)

print(response.content)
print(response.status_code)
