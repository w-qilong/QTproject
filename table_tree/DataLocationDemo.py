'''定位表格中满足条件的数据
在表格中快速定位到特定的行
1.数据的定位：findItems 返回一个列表
2.如果找到了满足条件的单元格，会定位到单元格所在的行：setSliderPosition(row)
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys

class Datalocation(QWidget):
    def __init__(self):
        super(Datalocation, self).__init__()
        self.initUI()
    def  initUI(self):
        self.setWindowTitle('DataLocation demo')
        self.resize(600,800)

        layout=QHBoxLayout()
        table=QTableWidget()
        table.setRowCount(40)
        table.setColumnCount(4)
        for i in range(40):
            for j in range(4):
                itemcontent='(%d,%d)' %(i,j)
                table.setItem(i,j,QTableWidgetItem(itemcontent))
        layout.addWidget(table)
        self.setLayout(layout)

        '''搜索满足条件的cell'''
        text='(3,1)'
        items=table.findItems(text,QtCore.Qt.MatchExactly)#设置为精确搜索,也可以使用其他的定位模式
        if len(items)>0:
            item=items[0]
            item.setBackground(QColor(0,255,0))
            item.setForeground(QColor(0,0,255))

            row=item.row()
            #定位到指定行
            table.verticalScrollBar().setSliderPosition(row)
        else:
            pass
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Datalocation()
    window.show()
    sys.exit(app.exec_())