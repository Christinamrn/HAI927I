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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

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
        self.frame_ImgIn.setGeometry(QRect(80, 420, 500, 500))
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
        self.frame_ImgOut.setGeometry(QRect(710, 420, 500, 500))
        self.frame_ImgOut.setFrameShape(QFrame.StyledPanel)
        self.frame_ImgOut.setFrameShadow(QFrame.Raised)
        self.label_ImgOut = QLabel(self.frame_ImgOut)
        self.label_ImgOut.setObjectName(u"label_ImgOut")
        self.label_ImgOut.setGeometry(QRect(-10, 0, 500, 500))
        self.label_ImgOut.setAlignment(Qt.AlignCenter)
        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1920, 1080))
        self.background.setMinimumSize(QSize(1920, 1080))
        self.background.setMaximumSize(QSize(1920, 1080))
        self.background.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.217, y1:0.943182, x2:0.792038, y2:0.017, stop:0 rgba(243, 231, 233, 255), stop:1 rgba(227, 238, 255, 255));")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(710, 20, 501, 291))
        self.GenBruit = QWidget()
        self.GenBruit.setObjectName(u"GenBruit")
        self.bouton_gaussien = QPushButton(self.GenBruit)
        self.bouton_gaussien.setObjectName(u"bouton_gaussien")
        self.bouton_gaussien.setGeometry(QRect(120, 100, 75, 24))
        self.bouton_poivresel = QPushButton(self.GenBruit)
        self.bouton_poivresel.setObjectName(u"bouton_poivresel")
        self.bouton_poivresel.setEnabled(True)
        self.bouton_poivresel.setGeometry(QRect(120, 70, 75, 24))
        self.bouton_chromatique = QPushButton(self.GenBruit)
        self.bouton_chromatique.setObjectName(u"bouton_chromatique")
        self.bouton_chromatique.setGeometry(QRect(120, 40, 75, 24))
        self.tabWidget.addTab(self.GenBruit, "")
        self.Filtres = QWidget()
        self.Filtres.setObjectName(u"Filtres")
        self.pushButton = QPushButton(self.Filtres)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(390, 220, 75, 24))
        self.horizontalLayoutWidget = QWidget(self.Filtres)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(60, 60, 251, 128))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_5 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout.addWidget(self.radioButton_5)

        self.radioButton = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout.addWidget(self.radioButton_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.radioButton_4 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout.addWidget(self.radioButton_4)

        self.slider_ecart_type = QSlider(self.Filtres)
        self.slider_ecart_type.setObjectName(u"slider_ecart_type")
        self.slider_ecart_type.setGeometry(QRect(350, 70, 101, 22))
        self.slider_ecart_type.setOrientation(Qt.Horizontal)
        self.slider_var_couleur = QSlider(self.Filtres)
        self.slider_var_couleur.setObjectName(u"slider_var_couleur")
        self.slider_var_couleur.setGeometry(QRect(350, 110, 101, 21))
        self.slider_var_couleur.setOrientation(Qt.Horizontal)
        self.slider_radius = QSlider(self.Filtres)
        self.slider_radius.setObjectName(u"slider_radius")
        self.slider_radius.setGeometry(QRect(350, 150, 101, 22))
        self.slider_radius.setOrientation(Qt.Horizontal)
        self.tabWidget.addTab(self.Filtres, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.background.raise_()
        self.bouton_ouvrirImgIn.raise_()
        self.frame_ImgIn.raise_()
        self.labeltext_chemin.raise_()
        self.frame_ImgOut.raise_()
        self.tabWidget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Christal", None))
        self.bouton_ouvrirImgIn.setText(QCoreApplication.translate("MainWindow", u"Ouvrir image", None))
        self.label_ImgIn.setText(QCoreApplication.translate("MainWindow", u"Ouvrir une image...", None))
        self.labeltext_chemin.setText(QCoreApplication.translate("MainWindow", u"Chemin du fichier ", None))
        self.label_ImgOut.setText(QCoreApplication.translate("MainWindow", u"Appliquer une modification...", None))
        self.background.setText("")
        self.bouton_gaussien.setText(QCoreApplication.translate("MainWindow", u"Gaussien", None))
        self.bouton_poivresel.setText(QCoreApplication.translate("MainWindow", u"PoivreEtSel", None))
        self.bouton_chromatique.setText(QCoreApplication.translate("MainWindow", u"Chromatique", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GenBruit), QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rateur de bruit", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Filtrage ", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Filtrage Gaussien", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Filtrage M\u00e9dian", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Filtrage Moyenneur", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Filtrage Laplacien", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Filtres), QCoreApplication.translate("MainWindow", u"Filtrages", None))
    # retranslateUi

