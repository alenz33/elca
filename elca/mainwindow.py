

from PyQt4.QtCore import pyqtSignature as qtsig
from PyQt4.QtGui import QMainWindow, QFileDialog, QMessageBox

from elca.util import loadUi
from elca.threads import PushThread

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi(self, 'mainwindow.ui')

        self._pushThread = PushThread()
        self._pushThread.doneRatioChanged.connect(self.progressBar.setValue)

    def on_filePushButton_clicked(self, checked=False):
        filename = QFileDialog.getOpenFileName(self)

    def on_sendPushButton_clicked(self, checked=False):
        self._pushThread.start()

    def on_cancelPushButton_clicked(self, checked=False):
        self._pushThread.quit()

    @qtsig('')
    def on_actionAbout_triggered(self):
        QMessageBox.about(self, 'About elca', 'stuff')

    @qtsig('')
    def on_actionAboutQt_triggered(self):
        QMessageBox.aboutQt(self)
