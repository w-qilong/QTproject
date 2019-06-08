'''输入对话框QFontDialog'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class Qfontdialog(QWidget):
    def __init__(self):
        super(Qfontdialog, self).__init__()
        self.initui()
    def initui(self):
        self.setWindowTitle('Qfontdialog demo选择字体')
        self.resize(300,400)
        layout=QVBoxLayout()
        self.label=QLabel("测试字体")
        self.button=QPushButton('选择字体')
        self.button.clicked.connect(self.selectfont)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)
    def selectfont(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.label.setFont(font)
if __name__ == '__main__':
    app=QApplication (sys.argv)
    window=Qfontdialog()
    window.show()
    sys.exit(app.exec_())