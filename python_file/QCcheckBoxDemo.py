'''复选框控件使用
QCheckBox复选框控件
3中状态
未选中：0
半选中：1
选中：2
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class  QCheckboxdemo(QWidget):
    def __init__(self):
        super(QCheckboxdemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("复选框控件")

        layout=QHBoxLayout()
        self.sb=QSpinBox()
        self.checkbox1=QCheckBox("checkbox1")
        #设置checkbox处于选中状态
        self.checkbox1.setChecked(True)
        self.checkbox1.stateChanged.connect(lambda :self.checkboxstate(self.checkbox1))
        layout.addWidget(self.checkbox1)

        self.checkbox2= QCheckBox("checkbox2")
        self.checkbox2.stateChanged.connect(lambda: self.checkboxstate( self.checkbox2))
        layout.addWidget(self.checkbox2)

        self.checkbox3 = QCheckBox("半选中")
        # 设置checkbox处于选中状态
        self.checkbox3.setTristate(True)
        self.checkbox3.setCheckState(Qt.PartiallyChecked)
        self.checkbox3.stateChanged.connect(lambda: self.checkboxstate( self.checkbox3))
        layout.addWidget(self.checkbox3)

        self.setLayout(layout)

    def checkboxstate(self,cb):
        checkstate1=self.checkbox1.text()+',ischecked='+str(self.checkbox1.isChecked())+'\n'
        checkstate2 = self.checkbox2.text() + ',ischecked=' + str(self.checkbox2.isChecked()) + '\n'
        checkstate3 = self.checkbox3.text() + ',ischecked=' + str(self.checkbox3.isChecked()) + '\n'
        print(checkstate1+checkstate2+checkstate3)

if __name__ == '__main__':
    app=QApplication (sys.argv)
    window=QCheckboxdemo()
    window.show()
    sys.exit(app.exec_())