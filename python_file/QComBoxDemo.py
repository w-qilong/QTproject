'''下拉列表控件combox'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class comboxdemo(QWidget):
    def __init__(self):
        super(comboxdemo, self).__init__()
        self.initUI()
    def  initUI(self):
        self.lable=QLabel("请选择编程语言")

        self.setWindowTitle("comboxdemo")
        self.resize(300,300)
        self.cb=QComboBox()
        self.cb.addItems(["c#","c++","c","python","javascript"])
        self.cb.currentIndexChanged.connect(self.selectionchanged)

        layout=QVBoxLayout()
        layout.addWidget(self.lable)
        layout.addWidget(self.cb)
        self.setLayout(layout)
    def selectionchanged(self):
        self.lable.setText(self.cb.currentText())
        self.lable.adjustSize()

        for count in range(self.cb.count()):
            print('item'+str(count)+'='+self.cb.itemText(count))
        print('current index','selection changed',self.cb.currentText())


if __name__ == '__main__':
    app=QApplication (sys.argv)
    window=comboxdemo()
    window.show()
    sys.exit(app.exec_())