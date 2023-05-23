# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
from ShowapiRequest import ShowapiRequest


r = ShowapiRequest("http://route.showapi.com/852-1","926147","b461cf485c7b48a598064fe428b88ac5" )
res = r.post()
print(res.text)