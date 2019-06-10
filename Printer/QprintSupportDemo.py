import sys
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtWidgets,QtPrintSupport
from PyQt5.QtPrintSupport import  QPageSetupDialog,QPrinter,QPrintDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
'''使用打印机'''
class PrintSupport(QMainWindow):
    def __init__(self):
        super(PrintSupport, self).__init__()
        self.initui()
    def initui(self):
        self.setGeometry(500,200,300,300)
        self.buton=QPushButton('将QTestEdit控件中的内容打印',self)
        self.buton.setGeometry(20,20,260,30)
        self.editor=QTextEdit('默认文本',self)
        self.editor.setGeometry(20,60,260,200)
        self.buton.clicked.connect(self.print)
    def print(self):
        printer=QtPrintSupport.QPrinter()
        painter=QtGui.QPainter()
        #将绘制目标输出重定向到打印机
        screen=self.editor.grab()
        painter.drawPixmap(10,10,screen)
        painter.end()
        print('print')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=PrintSupport()
    window.show()
    sys.exit(app.exec_())



