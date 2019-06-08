'''QDialog'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class QDialogdemo(QMainWindow):
    def __init__(self):
        super(QDialogdemo, self).__init__()
        self.initui()
    def initui(self):
        self.setWindowTitle("QDialogDEMO")
        self.resize(300,400)
        self.button1=QPushButton(self)
        self.button1.setText('弹出对话框')
        self.move(50,50)
        self.button1.clicked.connect(self.clickbutton)
    def clickbutton(self):
        dialoag=QDialog()
        dialoag.setWindowTitle('childDialog')
        pushbutton=QPushButton('确定',dialoag)
        dialoag.move(50,50)
        pushbutton.clicked.connect(dialoag.close)
        #设置dialog模式,设置为当子窗体显示时，父窗体无法
        dialoag.setWindowModality(Qt.ApplicationModal)
        dialoag.exec()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=QDialogdemo()
    window.show()
    sys.exit(app.exec_())