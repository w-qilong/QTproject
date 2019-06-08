'''设置窗体图标'''
'''退出应用程序'''
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHBoxLayout,QWidget,QPushButton
from PyQt5.QtGui import QIcon
class createwindow (QMainWindow):
    #构造函数
    def __init__(self):
        super(createwindow, self).__init__()
        #set window name
        self.setWindowTitle("firstwindow")
        #设置窗体图标
        self.setWindowIcon(QIcon("python_text_x_64px_8857_easyicon.net.png"))
       #设置窗体位置及大小
        self.setGeometry(200,200,400,300)

if __name__ == '__main__':#只有执行本python文件时会执行，调用该文件时不会执行
    app=QApplication(sys.argv)
    window=createwindow()
    window.show()
    sys.exit(app.exec_())



