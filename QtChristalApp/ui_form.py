# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QSize(1920, 1080))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.bouton_ouvrirImgIn = QPushButton(self.centralwidget)
        self.bouton_ouvrirImgIn.setObjectName(u"bouton_ouvrirImgIn")
        self.bouton_ouvrirImgIn.setGeometry(QRect(90, 50, 75, 24))
        self.frame_ImgIn = QFrame(self.centralwidget)
        self.frame_ImgIn.setObjectName(u"frame_ImgIn")
        self.frame_ImgIn.setEnabled(True)
        self.frame_ImgIn.setGeometry(QRect(80, 210, 500, 500))
        self.frame_ImgIn.setFrameShape(QFrame.StyledPanel)
        self.frame_ImgIn.setFrameShadow(QFrame.Raised)
        self.label_ImgIn = QLabel(self.frame_ImgIn)
        self.label_ImgIn.setObjectName(u"label_ImgIn")
        self.label_ImgIn.setGeometry(QRect(0, 0, 500, 500))
        self.label_ImgIn.setAlignment(Qt.AlignCenter)
        self.labeltext_chemin = QLabel(self.centralwidget)
        self.labeltext_chemin.setObjectName(u"labeltext_chemin")
        self.labeltext_chemin.setGeometry(QRect(200, 40, 391, 41))
        self.frame_ImgOut = QFrame(self.centralwidget)
        self.frame_ImgOut.setObjectName(u"frame_ImgOut")
        self.frame_ImgOut.setGeometry(QRect(710, 210, 500, 500))
        self.frame_ImgOut.setFrameShape(QFrame.StyledPanel)
        self.frame_ImgOut.setFrameShadow(QFrame.Raised)
        self.label_ImgOut = QLabel(self.frame_ImgOut)
        self.label_ImgOut.setObjectName(u"label_ImgOut")
        self.label_ImgOut.setGeometry(QRect(0, 0, 500, 500))
        self.label_ImgOut.setAlignment(Qt.AlignCenter)
        self.bouton_poivresel = QPushButton(self.centralwidget)
        self.bouton_poivresel.setObjectName(u"bouton_poivresel")
        self.bouton_poivresel.setEnabled(True)
        self.bouton_poivresel.setGeometry(QRect(720, 100, 75, 24))
        self.bouton_gaussien = QPushButton(self.centralwidget)
        self.bouton_gaussien.setObjectName(u"bouton_gaussien")
        self.bouton_gaussien.setGeometry(QRect(720, 130, 75, 24))
        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1920, 1080))
        self.background.setMinimumSize(QSize(1920, 1080))
        self.background.setMaximumSize(QSize(1920, 1080))
        self.background.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.217, y1:0.943182, x2:0.792038, y2:0.017, stop:0 rgba(243, 231, 233, 255), stop:1 rgba(227, 238, 255, 255));")
        self.bouton_chromatique = QPushButton(self.centralwidget)
        self.bouton_chromatique.setObjectName(u"bouton_chromatique")
        self.bouton_chromatique.setGeometry(QRect(720, 70, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.background.raise_()
        self.bouton_ouvrirImgIn.raise_()
        self.frame_ImgIn.raise_()
        self.labeltext_chemin.raise_()
        self.frame_ImgOut.raise_()
        self.bouton_poivresel.raise_()
        self.bouton_gaussien.raise_()
        self.bouton_chromatique.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Christal", None))
        self.bouton_ouvrirImgIn.setText(QCoreApplication.translate("MainWindow", u"Ouvrir image", None))
        self.label_ImgIn.setText(QCoreApplication.translate("MainWindow", u"Ouvrir une image...", None))
        self.labeltext_chemin.setText(QCoreApplication.translate("MainWindow", u"Chemin du fichier ", None))
        self.label_ImgOut.setText(QCoreApplication.translate("MainWindow", u"Appliquer une modification...", None))
        self.bouton_poivresel.setText(QCoreApplication.translate("MainWindow", u"PoivreEtSel", None))
        self.bouton_gaussien.setText(QCoreApplication.translate("MainWindow", u"Gaussien", None))
        self.background.setText("")
        self.bouton_chromatique.setText(QCoreApplication.translate("MainWindow", u"Chromatique", None))
    # retranslateUi

