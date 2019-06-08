import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

'''
在工具栏中添加工具按钮时，默认不显示文字，添加的文字作为tooltip提示信息
'''

class Toolbar(QMainWindow):
    def  __init__(self):
        super(Toolbar, self).__init__()
        self.iniui()
    def iniui(self):
        self.setWindowTitle("toolbar demo ")
        self.resize(300,400)

        tb1=self.addToolBar('file')
        new=QAction(QIcon(r'D:\QTproject\Image\python_text_x_64px_8857_easyicon.net.png'),'new',self)
        tb1.addAction(new)
        open = QAction(QIcon(r'D:\QTproject\Image\python_text_x_64px_8857_easyicon.net.png'), 'open', self)
        tb1.addAction(open )

if __name__ == '__main__':
    app=QApplication (sys.argv)
    window=Toolbar()
    window.show()
    sys.exit(app.exec_())
