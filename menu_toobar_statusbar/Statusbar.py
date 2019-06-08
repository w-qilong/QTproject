import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

'''
在工具栏中添加工具按钮时，默认不显示文字，添加的文字作为tooltip提示信息
'''

class Statusbar(QMainWindow):
    def  __init__(self):
        super(Statusbar, self).__init__()
        self.iniui()
    def iniui(self):
        self.setWindowTitle("toolbar demo ")
        self.resize(300,400)


        bar=self.menuBar()
        file= bar.addMenu('File')
        file.addAction('show')
        file.triggered.connect(self.processtrigger)
        self.setCentralWidget(QTextEdit())
        self.statusBar=QStatusBar()
        self.setStatusBar(self.statusBar)
    def processtrigger(self,q):
        if q.text()=='show':
            self.statusBar.showMessage(q.text()+'菜单被点击了',5000)
if __name__ == '__main__':
    app=QApplication (sys.argv)
    window=Statusbar()
    window.show()
    sys.exit(app.exec_())
