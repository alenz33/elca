

from PyQt4.QtCore import pyqtSignature as qtsig
from PyQt4.QtGui import QMainWindow, QFileDialog, QMessageBox

from util import loadUi

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi(self, 'mainwindow.ui')

    def on_filePushButton_clicked(self, checked=False):
        filename = QFileDialog.getOpenFileName(self)

    @qtsig('')
    def on_actionAbout_triggered(self):
        QMessageBox.about(self, 'About elca', 'stuff')

    @qtsig('')
    def on_actionAboutQt_triggered(self):
        QMessageBox.aboutQt(self)
