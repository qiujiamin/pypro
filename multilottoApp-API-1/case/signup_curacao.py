import  requests
# 调试用
url = "https://h5app-dev.multilotto.net/api/jsuser/signup"
data = {
	"access_token":"",
	"address":"Guimiao+New+VillageHouhai+Avenue",
	"address2":"testad2",
	"affiliatecode":"",
	"casinoversion":"3.2.0",
	"city":"shenzhen",
	"country":"MN",
	"countryName":"Mongolida",
	"currency":"EUR",
	"dateofbirth":"1999-01-03",
	"email": "ml01@gmail.com",
	"external_identifier": "",
	"external_typeid": "",
	"fillinAddressStr": "Guimiao New VillageHouhai Avenue ,Nanshan,AAA",
	"firstname": "mljj",
	"gender": "m",
	"language": "EN",
	"lastname": "qiujj",
	"password": "Aa123456",
	"phonrPrefix": "82",
	"platform": "3000",
	"postcode": "AAA",
	"pushid": "a7b69ace-4b6d-49e4-8ef4-077c58a182b3",
	"pushproject": "curacao",
	"curacao": "192.168.22.151",
	"subchannel": "1004",
	"uniq": "D69DE874-EA21-40A7-8DA3-8FDE0BC5DE62",
	"usercheck": "",
	"userid": "",
	"username": "",
	"version": "3.2.0",
	"tel": ""
}
# data = {
# 	"pushproject": "curacao",
# 	"password": "Aa123456",
# 	"source": "",
# 	"email": "ml01@gmail.com",
# 	"userid": "",
# 	"uniq": "android_7a4193a1-0462-44f7-b2c3-7a1ac0c9361d_1568707560122",
# 	"useragent": "MI 6 ",
# 	"platform": "4000",
# 	"osversion": "5.1.1",
# 	"country": "ML",
# 	"affiliatecode": "",
# 	"remote_addr": "172.17.100.15",
# 	"version": "3.2.0",
# 	"resolution": "900x1600",
# 	"language": "EN",
# 	"currency": "EUR",
# 	"pushid": "fb26b96a-53e2-40ff-b20d-1cbecff49b79",
# 	"subchannel": "1005",
# 	"usercheck": ""
# }
header = {
    "accept":"*/*",
    "content-type":"application/json; charset=UTF-8",
    "content-length":"442",
    "accept-encoding":"gzip",
    "user-agent":"okhttp/3.8.1"

}
res = requests.post(url,data,header).json()
print(res)


# url1 = "https://h5app-dev.multilotto.com/en/touch/dashboard/mygames/active/?version=2.9.0"
# data1 = {}
# url1 = "https://h5app-dev.multilotto.com/en/touch/auth/applogin/"+userid+"/"+usercheck+"?url=touch/dashboard/mygames/active/&version=2.6.1"
# print(url1)
# res1 = requests.get(url1)
# print(res1)