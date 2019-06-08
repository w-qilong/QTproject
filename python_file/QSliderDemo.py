'''滑块控件'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class qsliderdemo(QWidget):
    def __init__(self):
        super(qsliderdemo, self).__init__()
        self.initUI()
    def  initUI(self):
        self.setWindowTitle('qslider')
        self.label=QLabel("hello world!")
        self.resize(300,700)
        layout=QVBoxLayout()
        layout.addWidget(self.label)

        #设置滑动条垂直或者水平
        self.slider=QSlider(Qt.Vertical)
        #设置滑动条最小值
        self.slider.setMinimum(10)
        #设置滑动条最大值
        self.slider.setMaximum(20)
        #设置步长
        self.slider.setSingleStep(2)
        #设置当前值
        self.slider.setValue(15)
        #设置刻度的位置
        self.slider.setTickPosition(QSlider.TicksLeft)
        #设置可读的间隔
        self.slider.setTickInterval(2)
        self.slider.valueChanged.connect(self.valuechanged)


        layout.addWidget(self.slider)
        self.setLayout(layout)
    def valuechanged(self):
        print('当前值为：%s' % self.slider.value())
        size=self.slider.value()
        self.label.setFont(QFont('Arial',size))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=qsliderdemo()
    window.show()
    sys.exit(app.exec_())