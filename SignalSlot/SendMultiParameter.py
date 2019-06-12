'''定义传递多个参数的信号'''
from PyQt5.QtCore import *

class sendsignal(QObject):
    #定义一个信号
    sendmsg=pyqtSignal(int,int,int )
    def run(self):
        self.sendmsg.emit(1,2,3)
class slot(QObject):
    def printmes(self,a,b,c):
        print(a,b,c)
if __name__ == '__main__':
        send=sendsignal()
        slot=slot()
        send.sendmsg.connect(slot.printmes)
        send.run()