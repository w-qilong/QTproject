import sys
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtWidgets,QtPrintSupport
from PyQt5.QtPrintSupport import  QPageSetupDialog,QPrinter,QPrintDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
'''使用打印机对话框'''
class PrintDialog(QMainWindow):
    def __init__(self):
        super(PrintDialog, self).__init__()
        self.printer=QPrinter()

        self.initui()
    def initui(self):
        self.setGeometry(300,300,500,400)
        self.setWindowTitle('打印对话框')
        self.editor=QTextEdit(self)
        self.editor.setGeometry(20,20,300,270)

        self.openbutton= QPushButton('打开文件',self)
        self.openbutton.move(350,20)
        self.openbutton.clicked.connect(self.openfile)


        self.settingbutton=QPushButton('打印设置',self)
        self.settingbutton.move(350,50)
        self.settingbutton.clicked.connect(self.showsettingDialog)

        self.printbutton=QPushButton('打印文档',self)
        self.printbutton.move(350,80)
        self.printbutton.clicked.connect(self.showprintdialog)


#打开文件
    def openfile(self):
        fname=QFileDialog.getOpenFileName(self,'打开文件','./')
        if fname[0]:
            with open(fname[0],'r',encoding='utf-8',errors='ignore') as f:
                self.editor.setText(f.read())

    #显示设置打印对话框
    def showsettingDialog(self):
        printdialog=QPageSetupDialog(self.printer,self)
        printdialog.exec()

    #显示打印对话框
    def showprintdialog(self):
        printdialog=QPrintDialog(self.printer,self)
        if printdialog.Accepted==printdialog.exec():
            self.editor.print(self.printer)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=PrintDialog()
    window.show()
    sys.exit(app.exec_())
