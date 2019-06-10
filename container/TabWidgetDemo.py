import sys
from PyQt5.QtCore import  *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TabWidget(QTabWidget):
    def __init__(self,parent=None):
        super(TabWidget, self).__init__(parent)
        self.setWindowTitle('tabwidget demo')
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()

        self.addTab(self.tab1,'选项卡1')
        self.addTab(self.tab2,'选项卡2')
        self.addTab(self.tab3,'选项卡3')

        button1=QPushButton('1',self.tab1)
        button2 = QPushButton('2', self.tab2)
        button3 = QPushButton('3', self.tab3)

        self.tab1ui()

    def tab1ui(self):
        layout=QFormLayout()
        layout.addRow('姓名',QLineEdit())
        layout.addRow('学号', QLineEdit())
        self.tab1.setLayout(layout)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=TabWidget()
    window.show()
    sys.exit(app.exec_())