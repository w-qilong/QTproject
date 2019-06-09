'''显示二维表数据'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
class Tableview(QWidget):
    def __init__(self):
        super(Tableview, self).__init__()
        self.setWindowTitle('QTableView表格视图控件演示')
        self.resize(500,300)

        self.model=QStandardItemModel(4,3)
        self.model.setHorizontalHeaderLabels(['id','姓名','年龄'])

        #在是用tableview控件时，需要将tableview和Model关联
        self.tableview=QTableView()
        self.tableview.setModel(self.model)

        layout=QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)
if __name__ == '__main__':
    app=QApplication (sys.argv)
    window=Tableview()
    window.show()
    sys.exit(app.exec_())