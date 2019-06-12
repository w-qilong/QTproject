'''滚动条控件，
1.通过滚动条值的变化控制其他控件的状态变化

2.通过滚动条值的变化来控制控件的位置
'''

import sys
from   PyQt5.QtCore import *
from PyQt5.QtGui import  *
from  PyQt5.QtWidgets import  *

class QScrollBardeomo(QWidget):
    def __init__(self):
        super(QScrollBardeomo, self).__init__()
        self.iniui()

    def iniui(self):
        pass