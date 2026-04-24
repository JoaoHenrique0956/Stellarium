import requests

URL = "http://10.41.82.206:8090/api/stelproperty/list"

r = requests.get(URL)
data = r.json()

"""for key in data.keys():
    if any(x in key.lower() for x in ["atmos", "land", "sky"]):
        print(key)"""


r = requests.get("http://10.41.82.206:8090/api/stelproperty/list")
print(r.text)