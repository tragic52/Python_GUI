import sys,ast,os
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QLineEdit 
from PyQt5.QtGui import QIcon
import file

def show_hide(w):
    #输入框捕获账号
    username = QLineEdit("",w)
    username.setPlaceholderText("请输入账号")
    username.setGeometry(100,70,200,30)
    #输入框捕获密码
    password = QLineEdit("",w)
    password.setPlaceholderText("请输入密码")
    password.setGeometry(100,110,200,30)

    #提示信息
    me = QLabel("",w)
    me.setText(r"<a href='https://mi.gotarget.top'>使用详情</a>")
    me.setOpenExternalLinks(True)
    me.setGeometry(100,150,160,40)

    #采用二次函数，有效捕获用户输入数据，随后创建文件并修改信息
    def creat_file():
        u_name = username.text()
        u_word = password.text()
        cr = file.file_change()
        cr.creat(u_name,u_word)
        #输出账密文件创建后的提示信息
        tips.setText("账号已经记录，请关闭此窗口重启")
    
    cr_btn = QPushButton("登录",w)
    cr_btn.clicked.connect(creat_file)
    cr_btn.setGeometry(30,90,60,40)
   
if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(400,300)
    w.setWindowTitle("运动刷步")
    w.setWindowIcon(QIcon("ico.jpg"))

    tips = QLabel("",w)
    tips.setGeometry(40,20,280,40)


    error = QLabel("",w)
    error.setGeometry(40,100,280,40)




    if not os.access("./passwd.txt", os.F_OK):
        show_hide(w)
    if os.access("./passwd.txt", os.F_OK):
        code = QLabel("响应状态：",w)
        code.setGeometry(40,30,80,40)
        code_change = QLabel("",w)
        code_change.setGeometry(40,55,80,40)
    
        step = QLabel("当前步数:",w)
        step.setGeometry(200,30,80,40)
        step_change = QLabel("",w)
        step_change.setGeometry(200,55,80,40)

        min = QLabel("最小值:",w)
        max = QLabel("最大值:",w)
        min.setGeometry(40,165,50,40)
        max.setGeometry(40,205,50,40)

        min_step = QLineEdit("",w)
        min_step.setPlaceholderText("请输入步数的最小值")
        min_step.setGeometry(100,170,200,30)
        
        max_step = QLineEdit("",w)
        max_step.setPlaceholderText("请输入步数的最大值")
        max_step.setGeometry(100,210,200,30)
    
        def on_button_clicked():
            min = int(min_step.text())
            max = int(max_step.text())
            s = file.file_change()
            resp = s.read_file().go(min,max)
            
            #将响应结果转换成字典
            dict = ast.literal_eval(resp)
            if dict["code"] == "200":
                code_change.setText("刷步成功")
            else:
                code_change.setText("请检查账密")
            step_change.setText(dict["step"])
        
        def show_error(error):
            error.setText("账号已经删除，请关闭此窗口重启")
        
        def delete_file():
            os.remove("./passwd.txt")
            #这是一个信息提示框
            show_error(error)
            
        #点击按钮后触发事件
        btn = QPushButton("提交",w)
        btn.setGeometry(40,250,60,40)
        btn.clicked.connect(on_button_clicked)

        change_btn = QPushButton("删除用户",w)
        change_btn.setGeometry(220,250,80,40)
        change_btn.clicked.connect(delete_file)
        
    w.show()

    app.exec()