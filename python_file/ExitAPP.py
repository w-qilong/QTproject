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
        #set window size
        self.resize(400,300)
        #添加状态栏
        self.status=self.statusBar()
        #显示提示信息
        self.status.showMessage("提示信息",5000)

        #add button
        self.button1=QPushButton("退出应用程序")
        #将信号与槽函数连接
        self.button1.clicked.connect(self.onClick_Button)
        #将按钮放到布局上
        layout=QHBoxLayout()
        layout.addWidget(self.button1)

        mainframe=QWidget()
        mainframe.setLayout(layout)

        self.setCentralWidget(mainframe)


    '''定义button单击事件,相当于槽函数'''
    def onClick_Button(self):
        sender=self.sender()
        print(sender.text()+"按钮被点下")
        app=QApplication.instance()
        #退出应用程序
        app.quit()

if __name__ == '__main__':#只有执行本python文件时会执行，调用该文件时不会执行
    app=QApplication(sys.argv)
    window=createwindow()
    window.show()

    sys.exit(app.exec_())



