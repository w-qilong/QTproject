'''创建菜单栏'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class menu(QMainWindow):
    def __init__(self):
        super(menu, self).__init__()
        bar=self.menuBar()#获取菜单栏

        file=bar.addMenu('文件')
        file.addAction('新建')

        save=QAction('保存',self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        save.triggered.connect(self.process)
    def process(self,a):
        print(self.sender().text())
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=menu()
    window.show()
    sys.exit(app.exec_())