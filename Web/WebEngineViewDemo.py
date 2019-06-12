'''使用web浏览器控件显示网页
'''


import sys
from   PyQt5.QtCore import *
from PyQt5.QtGui import  *
from  PyQt5.QtWidgets import  *
from   PyQt5.QtWebEngineWidgets import *

class webengineview(QMainWindow):
    def __init__(self):
        super(webengineview, self).__init__()
        self.setWindowTitle('打开外部网页demo')
        self.setGeometry(5,30,1355,730)
        self.browser=QWebEngineView()
        self.browser.load(QUrl('https://www.jd.com'))
        self.setCentralWidget(self.browser)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=webengineview()
    window.show()
    sys.exit(app.exec_())
