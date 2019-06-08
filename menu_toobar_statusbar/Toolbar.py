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
        tb1.addAction(open)
        #可以设置同时显示文字和图标
        tb1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        #可以创建多个菜单栏，他们会显示在同一行，但是采用不同的菜单栏进行区分
        tb2 = self.addToolBar('file')
        new = QAction(QIcon(r'D:\QTproject\Image\python_text_x_64px_8857_easyicon.net.png'), 'new', self)
        tb2.addAction(new)
        open = QAction(QIcon(r'D:\QTproject\Image\python_text_x_64px_8857_easyicon.net.png'), 'open', self)
        tb2.addAction(open)
        # 可以设置同时显示文字和图标
        tb2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        tb1.actionTriggered.connect(self.toolbtpressed)
        tb2.actionTriggered.connect(self.toolbtpressed)
    def toolbtpressed(self,a):
       print('被点击的是：',a.text())


if __name__ == '__main__':
    app=QApplication (sys.argv)
    window=Toolbar()
    window.show()
    sys.exit(app.exec_())
