'''容纳多文档的窗口
Q
'''
import sys
from   PyQt5.QtCore import *
from PyQt5.QtGui import  *
from  PyQt5.QtWidgets import  *

class MultiWindowsdemo(QMainWindow):
    count=0#用于记录当前的窗口总数
    def __init__(self):
        super(MultiWindowsdemo, self).__init__()
        self.setWindowTitle('容纳多文档的窗口')
        self.mdi=QMdiArea()
        self.setCentralWidget(self.mdi)
        bar=self.menuBar()
        file=bar.addMenu('file')#添加父级菜单
        file.addAction('new')#添加子级菜单
        file.addAction('cascade')
        file.addAction('tiled')

        file.triggered.connect(self.windowaction)
    def windowaction(self,q):
        print(q.text())
        if  q.text()=='new':
            MultiWindowsdemo.count=MultiWindowsdemo.count+1
            sub=QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle('子窗口'+str(MultiWindowsdemo.count))
            self.mdi.addSubWindow(sub )
            sub.show()
        elif q.text()=='cascade':
            self.mdi.cascadeSubWindows()
        elif q.text()=='tiled':
            self.mdi.tileSubWindows()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=MultiWindowsdemo()
    window.show()
    sys.exit(app.exec_())
