
import requests

BASE="http://localhost:8000"
print(requests.get(BASE+"/").json())
print(requests.get(BASE+"/discover/").json())
print(requests.post(BASE+"/verify-number/", json={"number":"+911234567890"}).json())
print(requests.post(BASE+"/simswap/", json={"number":"+911234567890"}).json())
