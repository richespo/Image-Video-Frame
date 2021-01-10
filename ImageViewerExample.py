from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(766, 569)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 61, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 641, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(25, 71, 721, 491))
        self.graphicsView.setSizeIncrement(QtCore.QSize(0, 0))
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.graphicsView.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(670, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Image Viewer"))
        self.label.setText(_translate("Dialog", "Image Path"))
        self.pushButton.setText(_translate("Dialog", "open"))

#from image_viewer import *
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPixmap
import os
import sys
class My_Application(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.checkPath)
    def checkPath(self):
        image_path = self.ui.lineEdit.text()
        if os.path.isfile(image_path):
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QPixmap(image_path)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.ui.graphicsView.setScene(scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    class_instance = My_Application()
    class_instance.show()
    sys.exit(app.exec_())