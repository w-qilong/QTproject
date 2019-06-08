'''输入对话框QFontDialog'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class Qfiledialog(QWidget):
    def __init__(self):
        super(Qfiledialog, self).__init__()
        self.initui()
    def initui(self):
        self.setWindowTitle('Qfiledialog demo文件对话框')
        self.resize(300,400)
        layout=QVBoxLayout()

        self.button=QPushButton()
        self.button.setText('选择图像文件')
        self.button.clicked.connect(self.selectimagefile)
        layout.addWidget(self.button)

        self.imagelabel=QLabel()
        layout.addWidget(self.imagelabel)

        self.button1 = QPushButton()
        self.button1.setText('选择文本文件')
        self.button1.clicked.connect(self.selecttextfile)
        layout.addWidget(self.button1)

        self.contents=QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)


    def selectimagefile(self):
        fname,_= QFileDialog.getOpenFileName(self,'打开文件','.','图像文件(*.jpg *.png)')
        self.imagelabel.setPixmap(QPixmap(fname))

    def selecttextfile(self):
        dialog=QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec():
            filenames=dialog.selectedFiles()
            f=open(filenames[0],'r',encoding='utf-8')
            with  f:
                data=f.read()
                self.contents.setText(data)



if __name__ == '__main__':
    app=QApplication (sys.argv)
    window=Qfiledialog()
    window.show()
    sys.exit(app.exec_())