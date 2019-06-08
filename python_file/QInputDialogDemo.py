'''输入对话框QInputDialog'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class Qinputdialog(QWidget):
    def __init__(self):
        super(Qinputdialog, self).__init__()
        self.initui()
    def initui(self):
        self.setWindowTitle('Qinputdialog demo输入对话框')
        self.resize(300,400)
        layout=QFormLayout()

        self.button1=QPushButton('获取列表中的选项')
        self.button1.clicked.connect(self.getItem)
        self.lineEdit1=QLineEdit()
        layout.addRow(self.button1,self.lineEdit1)

        self.button2 = QPushButton('获取字符串')
        self.button2.clicked.connect(self.getText)
        self.lineEdit2 = QLineEdit()
        layout.addRow(self.button2, self.lineEdit2)

        self.button3 = QPushButton('获取数字')
        self.button3.clicked.connect(self.getInt)
        self.lineEdit3 = QLineEdit()
        layout.addRow(self.button3, self.lineEdit3)

        self.setLayout(layout)

    def getItem(self):
        items=['c','c++','python']
        item,ok=QInputDialog.getItem(self,'请选择编程语言','语言列表',items)
        if ok and item:
            self.lineEdit1.setText(item)
    def getText(self):
        text,ok=QInputDialog.getText(self,'文本输入框','请输入字符串')
        if ok and text:
            self.lineEdit2.setText(text)
    def getInt(self):
        int,ok=QInputDialog.getInt(self,'数字输入框','请输入数字')
        if ok and int:
            self.lineEdit3.setText(str(int))


if __name__ == '__main__':
    app=QApplication (sys.argv)
    window=Qinputdialog()
    window.show()
    sys.exit(app.exec_())