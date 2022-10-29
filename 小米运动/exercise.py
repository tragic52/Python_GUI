#API请求接口：     https://apis.jxcxin.cn/api/mi?user=15190277635&password=a1662857630&step=8091
"""
这是一个娱乐性质的项目:运动刷步数

"""
from mimetypes import init
import requests
from random import randint

class step_change():
    def __init__(self,username,password):
       self.username = username
       self.password = password
    
    def go(self,min,max):    
        url = "https://apis.jxcxin.cn/api/mi"
        step = randint(min,max)
        #添加请求信息
        param = {
            "user" : self.username,
            "password" : self.password,
            "step" : step,
        }

        resp = requests.get(url,params=param)
        return(resp.text)

# if __name__ == "__main__":
#     m = step_change("151902777635","a1662857630")
#     print(type(m))