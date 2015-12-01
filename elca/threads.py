import time
from PyQt4.QtCore import QThread, pyqtSignal

class PushThread(QThread):
    doneRatioChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self._shouldStop = False

    def run(self):
        for i in range(100):
            if self._shouldStop:
                break

            # do sth

            self.doneRatioChanged.emit(i)
            time.sleep(0.5)

    def start(self, prio=QThread.InheritPriority):
        self._shouldStop = False
        QThread.start(self, prio)

    def quit(self):
        self._shouldStop = True
        QThread.quit(self)
