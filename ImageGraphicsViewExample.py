import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QFileDialog, QGraphicsPixmapItem, QGraphicsScene, QDesktopWidget

screen_x, screen_y = 1280, 800
im = Image.new("RGB", (1280, 800), "black")
new_image = Image.new("RGB", (1280, 800), "black")

def scaleImage(im):
    width, height = im.size
    #screen_x, screen_y = ui.returnScreenSize()
    if width == screen_x and height == screen_y:
        return im
    if width > height:                                                          #landscape
        if height > screen_y:                                                    #scale down
            ratio = height / screen_y
            new_height = int(height / ratio)
            new_width = int(width / ratio)# scale the height
            new_image = im.resize((new_width, new_height), Image.ANTIALIAS)          # resized before crop
            if new_width > screen_x:                                               # height needs to be cropped
                increment = (new_width - screen_x) / 2                             # crop 1/2 oversize from each side
                box = (int(increment), 0, int(screen_x-increment), int(screen_y))      # desired size
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


class portrait_doubler():
    firstImage = None
    return_image = None
    blank_image = Image.new("RGB", (screen_x, screen_y), "black")

    def stitch_em(self,portrait_image):
        if self.firstImage == None:
            self.firstImage = portrait_image
            return None
        else:
            if self.first_image.size[0] + portrait_image.size[0] < screen_x:
                border = (screen_x-(self.first_image.size[0]+portrait_image.size[0]))/3
                self.blank_image.paste(self.first_image, (int(border),0))
                self.blank_image.paste(portrait_image, ((int(border)+int(border)+self.first_image.size[0]), 0))
                self.return_image = self.blank_image
                self.GOT_FIRST_IMAGE = False
                self.blank_image = Image.new("RGB", (screen_x, screen_y), "black")
                self.first_image = self.blank_image
                return self.return_image
            elif self.first_image.size[0] + portrait_image.size[0] == screen_x:
                self.blank_image.paste(self.first_image, (0,0))
                self.blank_image.paste(portrait_image, ((self.first_image.size[0], 0)))
                self.return_image = self.blank_image
                self.GOT_FIRST_IMAGE = False
                self.blank_image = Image.new("RGB", (screen_x, screen_y), "black")
                self.first_image = self.blank_image
                return self.return_image
            else:                           #add code for width too wide
                if self.first_image.size[0] > screen_x/2:
                    xtra = self.first_image.size[0] - screen_x/2
                    chop = int(xtra/2)
                    box = (chop, 0, int(chop+(screen_x/2)), screen_y)
                    self.first_image = self.first_image.crop(box)
                if portrait_image.size[0] > screen_x/2:
                    xtra = portrait_image.size[0] - screen_x/2
                    chop = int(xtra/2)
                    box = (chop, 0, int(chop+(screen_x/2)), screen_y)
                    portrait_image = portrait_image.crop(box)
                self.blank_image.paste(self.first_image, (0,0))
                self.blank_image.paste(portrait_image, ((self.first_image.size[0], 0)))
                self.return_image = self.blank_image
                self.GOT_FIRST_IMAGE = False
                self.first_image = self.blank_image

                self.blank_image = Image.new("RGB", (screen_x, screen_y), "black")
                return self.return_image





class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        screen_y, screen_x = self.returnScreenSize()
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
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 24))
        # self.menubar.setObjectName("menubar")
        # self.menuOpen = QtWidgets.QMenu(self.menubar)
        # self.menuOpen.setObjectName("menuOpen")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        # self.actionOpen = QtWidgets.QAction(MainWindow)
        # self.actionOpen.setObjectName("actionOpen")
        # self.menuOpen.addAction(self.actionOpen)
        # self.menubar.addAction(self.menuOpen.menuAction())
        # self.actionOpen.triggered.connect(self.mymenu)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Viewer"))
        # self.menuOpen.setTitle(_translate("MainWindow", "File"))
        # self.actionOpen.setText(_translate("MainWindow", "Open"))

    def returnScreenSize(self):
        sizeObject = QDesktopWidget().screenGeometry(-1)
        return  sizeObject.width(), sizeObject.height()

    def mousePressEvent(self, e):
        print("mousePressEvent")

  #  @pyqtSlot


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    screen_x, screen_y = ui.returnScreenSize()
    doubler = portrait_doubler()

    image_list = [os.path.join("C:\\Users\\riche\\PycharmProjects\\Image-Video-Frame", f) for f in os.listdir("C:\\Users\\riche\PycharmProjects\\Image-Video-Frame") if f.endswith('.jpg')]
    for img in image_list:
        next_image = Image.open(img)
        new_image = scaleImage(img)
        width, height = new_image.size
        if height > width:
            stitched_image = doubler.stitch_em(new_image)
            if stitched_image == None:
                continue
            else:
                new_image = stitched_image

    # im = Image.open('em7.jpg', 'r')
    # new_image = scaleImage(im)
    # new_image.save('em7.jpg')
    # pix = QPixmap('em7.jpg')
    # item = QGraphicsPixmapItem(pix)
    # scene = QGraphicsScene()
    # scene.addItem(item)
    # ui.graphicsView.setScene(scene)


    MainWindow.show()
    sys.exit(app.exec_())