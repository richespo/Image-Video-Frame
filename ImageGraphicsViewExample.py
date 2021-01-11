import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PIL import Image
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QFileDialog, QGraphicsPixmapItem, QGraphicsScene, QDesktopWidget


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        sizeObject = QDesktopWidget().screenGeometry(-1)
        screen_y, screen_x = sizeObject.height(), sizeObject.width()
      #  print(" Screen size : "  + str(sizeObject.height()) + "x"  + str(sizeObject.width()))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(screen_x, screen_y)
        MainWindow.setMaximumSize(QtCore.QSize(screen_x, screen_y))
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, screen_x, screen_y))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setHorizontalScrollBarPolicy(1);
        self.graphicsView.setVerticalScrollBarPolicy(1);
        print(self.graphicsView.horizontalScrollBarPolicy() )
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 24))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuOpen.addAction(self.actionOpen)
        self.menubar.addAction(self.menuOpen.menuAction())
        self.actionOpen.triggered.connect(self.mymenu)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Viewer"))
        self.menuOpen.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))

  #  @pyqtSlot
    def mymenu(self):
        fileName = QFileDialog.getOpenFileName(None, "Open File", "C:", "Image files (*.jpg *.bmp *.jpeg)");
        # im = Image.open(fileName)
        # width, height = im.size

        pix = QPixmap(fileName[0])
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene(self)
        scene.addItem(item)
        self.graphicsView.setScene(scene)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())