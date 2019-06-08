import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class Qmessagebox(QWidget):
    def __init__(self):
        super(Qmessagebox, self).__init__()
        self.initui()
    def initui(self):
        self.setWindowTitle("QMessageBox Demo")
        self.resize(300,400)
        layot=QVBoxLayout()
        pushbutton1=QPushButton('显示关于对话框')
        pushbutton1.clicked.connect(self.showmessagebox)
        pushbutton2= QPushButton('显示消息对话框')
        pushbutton2.clicked.connect(self.showmessagebox)
        pushbutton3 = QPushButton('显示错误对话框')
        pushbutton3.clicked.connect(self.showmessagebox)
        pushbutton4 = QPushButton('显示警告对话框')
        pushbutton4.clicked.connect(self.showmessagebox)
        pushbutton5 = QPushButton('显示提问对话框')
        pushbutton5.clicked.connect(self.showmessagebox)
        layot.addWidget(pushbutton1)
        layot.addWidget(pushbutton2)
        layot.addWidget(pushbutton3)
        layot.addWidget(pushbutton4)
        layot.addWidget(pushbutton5)
        self.setLayout(layot)
    def showmessagebox(self):
        text=self.sender().text()
        if text=='显示关于对话框':
            QMessageBox.about(self,'关于','这是一个关于对话框')
        if text=='显示消息对话框':
            QMessageBox.information(self,'消息','这是一个消息对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if text=='显示错误对话框':
            QMessageBox.critical(self,'错误','这是一个错误对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if text=='显示警告对话框':
            QMessageBox.warning(self,'警告','这是一个警告对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if text=='显示提问对话框':
            QMessageBox.question(self,'提问','这是一个提问对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)


if __name__ == '__main__':
    app=QApplication (sys.argv)
    window=Qmessagebox()
    window.show()
    sys.exit(app.exec_())