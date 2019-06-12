'''自定义信号
pyqtSignal（）
'''
from PyQt5.QtCore import *
class MyTypeSignal(QObject):
    #define signal
    sendmsg=pyqtSignal(object)
    def run(self):
        self.sendmsg.emit('hello world')
class MySlot(QObject):
    def get(self,msg):
        print('message:'+msg)
if __name__ == '__main__':
        send=MyTypeSignal()
        slot=MySlot()
        send.sendmsg.connect(slot.get)
        send.run()