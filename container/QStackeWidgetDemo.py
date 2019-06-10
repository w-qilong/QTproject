

'''堆栈窗口控件'''
import sys
from PyQt5.QtCore import  *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class  StackeWidget(QWidget):
    def __init__(self):
        super(StackeWidget, self).__init__()
        self.setWindowTitle('堆栈窗口控件')

        self.list=QListWidget()
        self.list.insertItem(0,'1')
        self.list.insertItem(1,'1')
        self.list.insertItem(2,'2')

        self.stack1=QWidget()
        self.stack2=QWidget()
        self.stack3=QWidget()

        self.stack=QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hbox=QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addWidget(self.stack)
        self.setLayout(hbox)
        self.tab1ui()
        self.tab2ui()
        self.tab3ui()
        self.list.currentRowChanged.connect(self.display)

    def tab2ui(self):
        layout = QFormLayout()
        layout.addRow('姓名2', QLineEdit())
        layout.addRow('学号2', QLineEdit())
        self.stack2.setLayout(layout)

    def tab1ui(self):
        layout = QFormLayout()
        layout.addRow('姓名', QLineEdit())
        layout.addRow('学号', QLineEdit())
        self.stack1.setLayout(layout)

    def tab3ui(self):
        layout = QFormLayout()
        layout.addRow('姓名3', QLineEdit())
        layout.addRow('学号3', QLineEdit())
        self.stack3.setLayout(layout)
    def display(self,index):
        self.stack.setCurrentIndex(index)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=StackeWidget()
    window.show()
    sys.exit(app.exec_())