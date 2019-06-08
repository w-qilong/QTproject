'''QColorDialog颜色对话框'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class QcoloRdialog(QWidget):
    def __init__(self):
        super(QcoloRdialog, self).__init__()
        self.initui()
    def initui(self):
        self.setWindowTitle('Qcolotdialog demo选择颜色')
        self.resize(300,400)
        layout=QVBoxLayout()

        self.button=QPushButton('选择颜色')
        self.button.clicked.connect(self.getcolor)
        layout.addWidget(self.button)

        self.label=QLabel('测试颜色')
        layout.addWidget(self.label)

        self.setLayout(layout)
    def getcolor(self):
        text=self.sender().text()
        if text=='选择颜色':
            color=QColorDialog.getColor()
            p=QPalette()#palette 调色板
            p.setColor(QPalette.WindowText,color)
            self.label.setPalette(p)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=QcoloRdialog()
    window.show()
    sys.exit(app.exec_())
