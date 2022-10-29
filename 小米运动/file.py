"""
这是一个文件读写的工具类
"""
from mimetypes import init
import os
import re
import exercise

class file_change():
    #判断文件存在与否
    def creat(self,username,password):
        # if not os.access("./passwd.txt", os.F_OK):                                          #文件不存在
        with open("./passwd.txt",mode="w",encoding="utf-8") as fw:
            n = "username:"+username
            p = "password:"+password

            fw.write(n)
            fw.write('\n')    #写入换行
            fw.write(p)   
    def read_file(self):
        if os.access("./passwd.txt", os.F_OK):          #文件存在
            with open("./passwd.txt",mode="r",encoding="utf-8") as f:
                str = f.read()
                f.close()

                #匹配字符串中的账号和密码
                for i in re.finditer(r"(?<=username:).+",str):
                        username = i.group()
                for i in re.finditer(r"(?<=password:).+",str):
                        password = i.group()
                #文件存在时读取文件内容，创建一个锻炼对象
                return exercise.step_change(username,password)


if __name__ == "__main__":
    s = file_change("15190277635","a1662857630")
    s.creat()
    m = s.read_file()
    m.go(5860,5870)
    print(type(m))

