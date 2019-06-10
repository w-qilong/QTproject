'''

停靠控件
'''

import sys
from PyQt5.QtCore import  *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DockDemo(QMainWindow):
    def __init__(self):
        super(DockDemo, self).__init__()

        self.setWindowTitle('停靠控件')
        layout=QHBoxLayout()
        self.items=QDockWidget('dockable',self)
        self.listwidget=QListWidget()
        self.listwidget.addItem('item1')
        self.listwidget.addItem('item2')
        self.listwidget.addItem('item3')

        self.items.setWidget(self.listwidget)
        self.setCentralWidget(QLineEdit())
        self.addDockWidget(Qt.RightDockWidgetArea,self.items)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=DockDemo()
    window.show()
    sys.exit(app.exec_())