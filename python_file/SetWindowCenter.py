import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget
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
        '''设置窗体居中'''
    def setcenter(self):
        screen = QDesktopWidget().screenGeometry()#获取屏幕坐标系
        size = self.geometry()#获取窗体坐标系
        '''使用move方法移动窗体'''
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

if __name__ == '__main__':#只有执行本python文件时会执行，调用该文件时不会执行
    app=QApplication(sys.argv)
    window=createwindow()
    window.setcenter()
    window.show()
    sys.exit(app.exec_())



