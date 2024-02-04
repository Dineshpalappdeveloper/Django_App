import requests

enpoints = "http://127.0.0.1:8000/car/list"

getresponse = requests.get(enpoints)
print(getresponse.json())
print(getresponse.status_code)
