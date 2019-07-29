import requests

r = requests.get("https://h5app-dev.multilotto.net:443/api/user/getvalidcountries")
print(r.status_code)
print(r.text)