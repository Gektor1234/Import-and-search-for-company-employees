import requests
#api url

url = "http://localhost:8000/information%20by%20name%20or%20surname/Ivan"
url2 = "http://localhost:8000/information%20by%20name%20or%20surname/Burcev"

#Get Request(должен быть 200)
response_by_name = requests.get(url)
response_by_surname = requests.get(url2)

print(response_by_name)
print(response_by_surname)


#Display Response (отображаем данные)
print(response_by_name.content)
print(response_by_surname.content)
