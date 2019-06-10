import  sys
from  PyQt5.QtWidgets import QWidget,QTableWidget,QHBoxLayout,QApplication,QTableWidgetItem,QComboBox,QPushButton
class PlaceControlIncell(QWidget):
    def __init__(self):
        super(PlaceControlIncell, self).__init__()
        self.initui()
    def initui(self):
        self.setWindowTitle('在单元格中放置控件')
        self.resize(430,300)
        layout=QHBoxLayout()
        tablewidget=QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)

        layout.addWidget(tablewidget)
        tablewidget.setHorizontalHeaderLabels(['name','gender','weight'])
        textitem=QTableWidgetItem('spider')
        tablewidget.setItem(0,0,textitem)

        combox=QComboBox()
        combox.addItem('male')
        combox.addItem('female')

        #QSS
        combox.setStyleSheet('QComboBox(margin:3px)')

        tablewidget.setCellWidget(0,1,combox)

        editbutton=QPushButton('change')
        editbutton.setDown(True)
        editbutton.setStyleSheet('QPushButton{margin:3px}')
        tablewidget.setCellWidget(0,2,editbutton)

        self.setLayout(layout)

if __name__ == '__main__':
    app=QApplication (sys.argv)
    window=PlaceControlIncell()
    window.show()
    sys.exit(app.exec_())

