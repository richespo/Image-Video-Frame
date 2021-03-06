# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame_resizer.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDir, QObject
from PIL import Image
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QFileDialog
import os


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 130, 350, 301))
        self.textEdit.setObjectName("textEdit")
        self.pbImageDirectory = QtWidgets.QPushButton(self.centralwidget)
        self.pbImageDirectory.setGeometry(QtCore.QRect(30, 70, 161, 32))
        self.pbImageDirectory.setObjectName("pbImageDirectory")
        self.pbImageDirectory.clicked.connect(self.getImageDirectory)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 269, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def scaleImage(self, im):
        #get image size
        width, height = im.size
        #get screen size
        screen = QGuiApplication.primaryScreen()
        screenGeometry = screen.geometry()
        screen_y = screenGeometry.height()
        screen_x = screenGeometry.width()
        #if image size = scren size return
        if width == screen_x and height == screen_y:
            return im
        if width > height:                         #landscape
            if height > screen_y:                  #scale down
                ratio = height / screen_y
                new_height = int(height / ratio)
                new_width = int(width / ratio)     # scale the height
                new_image = im.resize((new_width, new_height), Image.ANTIALIAS)          # resized before crop
                if new_width > screen_x:                                               # width needs to be cropped
                    increment = (new_width - screen_x) / 2                             # crop 1/2 oversize from each side
                    box = (int(increment), 0, int(new_width - increment), int(screen_y))      # desired size
                    new_image = new_image.crop(box)
                return  new_image
            else:                                                                       #scale up
                ratio = screen_y / height
                new_height = int(height * ratio)
                new_width = int(width * ratio)
                new_image = im.resize((new_width, new_height), Image.ANTIALIAS)
                if new_width > screen_x:                                               # height needs to be cropped
                    increment = (new_width - screen_x) / 2                             # crop 1/2 oversize from each side
                    box = (int(increment), 0, int(new_width-increment), int(screen_y))      # desired size
                    new_image = new_image.crop(box)
                return  new_image
        else:                                                                           #portrait
            if height > screen_y:                                                       #scale down
                ratio = height / screen_y
                new_width = width / ratio
                new_image = im.resize((int(new_width), screen_y), Image.ANTIALIAS)
            else:                                                                        #scale up
                ratio = screen_y / height
                new_width = width * ratio
                new_image = im.resize((int(new_width), screen_y), Image.ANTIALIAS)
        return new_image

    def getImageDirectory(self):
        fdialog = QFileDialog()
        fdialog.setFileMode(QFileDialog.DirectoryOnly)
        file_name = QFileDialog.getExistingDirectory(None, 'Choose Directory', "/Users/rich")
        image_list = [os.path.join(file_name, f) for f in os.listdir(file_name) if f.endswith('.jpg')]
        number_converted = 0
        for img in image_list:
            self.next_image = Image.open(img)
            self.textEdit.insertPlainText("Opening %s\n" % img)
            resized_image = ui.scaleImage(self.next_image)
            resized_image.save(img)
            self.textEdit.insertPlainText("Saving %s\n" % img)
            number_converted += 1
        self.textEdit.insertPlainText("Converted %d of %d\n" % (number_converted, len(image_list)))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Photo Frame Image Resizer"))
        self.pbImageDirectory.setText(_translate("MainWindow", "Image Directory"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
