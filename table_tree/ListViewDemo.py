'''显示单列数据'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QStringListModel
import sys
class ListView(QWidget):
    def __init__(self):
        super(ListView, self).__init__()
        listview=QListView()
        self.setWindowTitle('QListView表格视图控件演示')
        self.resize(500,300)

        layout=QVBoxLayout()
        listmode=QStringListModel()
        self.list=['列表项1','2','3']

        listmode.setStringList(self.list)
        listview.setModel(listmode)
        listview.clicked.connect(self.clicked)

        layout.addWidget(listview)
        self.setLayout(layout)

    def clicked(self,item):
        QMessageBox.information(self,'Qlistview','选择的是：'+self.list[item.row()])

if __name__ == '__main__':
    app=QApplication (sys.argv)
    window=ListView()
    window.show()
    sys.exit(app.exec_())