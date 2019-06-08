'''让控件支持拖拽动作
A.setDropEnable(True)
B.setAcceptDrops(True)

B需要两个事件
1.dragEnterEvent 将A托到B
2.dropEvent 在B的区域放下A时触发

'''
'''下拉列表控件combox'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Mycombox(QComboBox):
    def __init__(self):
        super(Mycombox, self).__init__()
        self.setAcceptDrops(True)
    def dragEnterEvent(self, e):
        print(e)
        if  e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e):
        self.addItem(e.mimeData().text())

class DragDropDemo(QWidget):
    def __init__(self):
        super(DragDropDemo, self).__init__()
        self.initUI()
    def  initUI(self):
        self.setWindowTitle("DragDropDemo")
        layout=QFormLayout()
        layout.addWidget(QLabel('请将左侧的文本拖动到右边的下拉列表中'))
        lineedit=QLineEdit()
        lineedit.setDragEnabled(True)#设置文本框可以拖动

        combox=Mycombox()
        layout.addRow(lineedit,combox)
        self.setLayout(layout)

if __name__ == '__main__':
    app=QApplication (sys.argv)
    window=DragDropDemo()
    window.show()
    sys.exit(app.exec_())

