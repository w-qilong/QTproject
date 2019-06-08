'''为控件添加提示信息'''
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHBoxLayout,QWidget,QPushButton,QToolTip
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
class tooltipform(QMainWindow):
    def __init__(self):
        super(tooltipform, self).__init__()
        self.setWindowTitle("hello")
        self.setGeometry(200,200,300,300)
        self.button1=QPushButton()
        self.button1.setText("鼠标在我这会显示提示信息")
        self.button1.setToolTip("提示信息")
        # 将按钮放到布局上
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainframe = QWidget()
        mainframe.setLayout(layout)

        self.setCentralWidget(mainframe)
        self.button1.setIcon(QIcon("D:\QTproject\Image\python_text_x_64px_8857_easyicon.net.png"))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=tooltipform()
    window.show()
    sys.exit(app.exec_())