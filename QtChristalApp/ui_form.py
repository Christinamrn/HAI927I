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
        self.tabWidget.setGeometry(QRect(670, 30, 691, 421))
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
        self.pushButton.setGeometry(QRect(590, 360, 75, 24))
        self.horizontalLayoutWidget = QWidget(self.Filtres)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(60, 60, 251, 128))
        self.hLay_filtres = QHBoxLayout(self.horizontalLayoutWidget)
        self.hLay_filtres.setObjectName(u"hLay_filtres")
        self.hLay_filtres.setContentsMargins(0, 0, 0, 0)
        self.vLa_filtres = QVBoxLayout()
        self.vLa_filtres.setObjectName(u"vLa_filtres")
        self.radio_bilateral = QRadioButton(self.horizontalLayoutWidget)
        self.radio_bilateral.setObjectName(u"radio_bilateral")

        self.vLa_filtres.addWidget(self.radio_bilateral)

        self.radio_gaussien = QRadioButton(self.horizontalLayoutWidget)
        self.radio_gaussien.setObjectName(u"radio_gaussien")

        self.vLa_filtres.addWidget(self.radio_gaussien)

        self.radio_median = QRadioButton(self.horizontalLayoutWidget)
        self.radio_median.setObjectName(u"radio_median")

        self.vLa_filtres.addWidget(self.radio_median)

        self.radio_moyenneur = QRadioButton(self.horizontalLayoutWidget)
        self.radio_moyenneur.setObjectName(u"radio_moyenneur")

        self.vLa_filtres.addWidget(self.radio_moyenneur)


        self.hLay_filtres.addLayout(self.vLa_filtres)

        self.radio_laplacien = QRadioButton(self.horizontalLayoutWidget)
        self.radio_laplacien.setObjectName(u"radio_laplacien")

        self.hLay_filtres.addWidget(self.radio_laplacien)

        self.verticalLayoutWidget_4 = QWidget(self.Filtres)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(350, 30, 160, 291))
        self.vLay_options = QVBoxLayout(self.verticalLayoutWidget_4)
        self.vLay_options.setObjectName(u"vLay_options")
        self.vLay_options.setContentsMargins(0, 0, 0, 0)
        self.vLay_radius = QVBoxLayout()
        self.vLay_radius.setObjectName(u"vLay_radius")
        self.label_3 = QLabel(self.verticalLayoutWidget_4)
        self.label_3.setObjectName(u"label_3")

        self.vLay_radius.addWidget(self.label_3)

        self.slider_radius = QSlider(self.verticalLayoutWidget_4)
        self.slider_radius.setObjectName(u"slider_radius")
        self.slider_radius.setOrientation(Qt.Horizontal)

        self.vLay_radius.addWidget(self.slider_radius)


        self.vLay_options.addLayout(self.vLay_radius)

        self.vLay_ecart_type = QVBoxLayout()
        self.vLay_ecart_type.setObjectName(u"vLay_ecart_type")
        self.label = QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName(u"label")

        self.vLay_ecart_type.addWidget(self.label)

        self.slider_ecart_type = QSlider(self.verticalLayoutWidget_4)
        self.slider_ecart_type.setObjectName(u"slider_ecart_type")
        self.slider_ecart_type.setOrientation(Qt.Horizontal)

        self.vLay_ecart_type.addWidget(self.slider_ecart_type)


        self.vLay_options.addLayout(self.vLay_ecart_type)

        self.vLay_diametre = QVBoxLayout()
        self.vLay_diametre.setObjectName(u"vLay_diametre")
        self.label_4 = QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")

        self.vLay_diametre.addWidget(self.label_4)

        self.slider_diametre = QSlider(self.verticalLayoutWidget_4)
        self.slider_diametre.setObjectName(u"slider_diametre")
        self.slider_diametre.setOrientation(Qt.Horizontal)

        self.vLay_diametre.addWidget(self.slider_diametre)


        self.vLay_options.addLayout(self.vLay_diametre)

        self.vLay_var_spatiale = QVBoxLayout()
        self.vLay_var_spatiale.setObjectName(u"vLay_var_spatiale")
        self.label_5 = QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")

        self.vLay_var_spatiale.addWidget(self.label_5)

        self.slider_var_spatiale = QSlider(self.verticalLayoutWidget_4)
        self.slider_var_spatiale.setObjectName(u"slider_var_spatiale")
        self.slider_var_spatiale.setOrientation(Qt.Horizontal)

        self.vLay_var_spatiale.addWidget(self.slider_var_spatiale)


        self.vLay_options.addLayout(self.vLay_var_spatiale)

        self.vLay_var_couleur = QVBoxLayout()
        self.vLay_var_couleur.setObjectName(u"vLay_var_couleur")
        self.label_2 = QLabel(self.verticalLayoutWidget_4)
        self.label_2.setObjectName(u"label_2")

        self.vLay_var_couleur.addWidget(self.label_2)

        self.slider_var_couleur = QSlider(self.verticalLayoutWidget_4)
        self.slider_var_couleur.setObjectName(u"slider_var_couleur")
        self.slider_var_couleur.setOrientation(Qt.Horizontal)

        self.vLay_var_couleur.addWidget(self.slider_var_couleur)


        self.vLay_options.addLayout(self.vLay_var_couleur)

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
        self.radio_bilateral.setText(QCoreApplication.translate("MainWindow", u"Filtrage Bilat\u00e9ral", None))
        self.radio_gaussien.setText(QCoreApplication.translate("MainWindow", u"Filtrage Gaussien", None))
        self.radio_median.setText(QCoreApplication.translate("MainWindow", u"Filtrage M\u00e9dian", None))
        self.radio_moyenneur.setText(QCoreApplication.translate("MainWindow", u"Filtrage Moyenneur", None))
        self.radio_laplacien.setText(QCoreApplication.translate("MainWindow", u"Filtrage Laplacien", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Taille noyau :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ecart-type :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Taille voisinage :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Variance spatiale :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Variance couleur :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Filtres), QCoreApplication.translate("MainWindow", u"Filtrages", None))
    # retranslateUi

