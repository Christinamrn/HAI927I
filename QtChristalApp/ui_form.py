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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1043)
        MainWindow.setMinimumSize(QSize(1920, 1000))
        MainWindow.setMaximumSize(QSize(1920, 1043))
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1920, 1000))
        self.centralwidget.setMaximumSize(QSize(1920, 1000))
        self.centralwidget.setStyleSheet(u"")
        self.frame_ImgIn = QFrame(self.centralwidget)
        self.frame_ImgIn.setObjectName(u"frame_ImgIn")
        self.frame_ImgIn.setEnabled(True)
        self.frame_ImgIn.setGeometry(QRect(105, 450, 500, 500))
        self.frame_ImgIn.setFrameShape(QFrame.StyledPanel)
        self.frame_ImgIn.setFrameShadow(QFrame.Raised)
        self.label_ImgIn = QLabel(self.frame_ImgIn)
        self.label_ImgIn.setObjectName(u"label_ImgIn")
        self.label_ImgIn.setGeometry(QRect(0, 0, 500, 500))
        self.label_ImgIn.setAlignment(Qt.AlignCenter)
        self.frame_ImgOut = QFrame(self.centralwidget)
        self.frame_ImgOut.setObjectName(u"frame_ImgOut")
        self.frame_ImgOut.setGeometry(QRect(1315, 450, 500, 500))
        self.frame_ImgOut.setFrameShape(QFrame.StyledPanel)
        self.frame_ImgOut.setFrameShadow(QFrame.Raised)
        self.label_ImgOut = QLabel(self.frame_ImgOut)
        self.label_ImgOut.setObjectName(u"label_ImgOut")
        self.label_ImgOut.setGeometry(QRect(0, 0, 500, 500))
        self.label_ImgOut.setAlignment(Qt.AlignCenter)
        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1920, 1000))
        self.background.setMinimumSize(QSize(1920, 1000))
        self.background.setMaximumSize(QSize(1920, 1000))
        self.background.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.217, y1:0.943182, x2:0.792038, y2:0.017, stop:0 rgba(243, 231, 233, 255), stop:1 rgba(227, 238, 255, 255));")
        self.background.setFrameShape(QFrame.NoFrame)
        self.frame_ouvertureImg = QFrame(self.centralwidget)
        self.frame_ouvertureImg.setObjectName(u"frame_ouvertureImg")
        self.frame_ouvertureImg.setGeometry(QRect(155, 100, 400, 200))
        self.frame_ouvertureImg.setAutoFillBackground(False)
        self.frame_ouvertureImg.setFrameShape(QFrame.NoFrame)
        self.frame_ouvertureImg.setFrameShadow(QFrame.Plain)
        self.labeltext_chemin = QLabel(self.frame_ouvertureImg)
        self.labeltext_chemin.setObjectName(u"labeltext_chemin")
        self.labeltext_chemin.setGeometry(QRect(50, 80, 300, 40))
        self.labeltext_chemin.setAutoFillBackground(False)
        self.labeltext_chemin.setStyleSheet(u"border: 2px inset #32194d; ")
        self.labeltext_chemin.setFrameShape(QFrame.Box)
        self.labeltext_chemin.setFrameShadow(QFrame.Plain)
        self.labeltext_chemin.setScaledContents(True)
        self.labeltext_chemin.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.labeltext_chemin.setWordWrap(False)
        self.labeltext_chemin.setMargin(5)
        self.bouton_ouvrirImgIn = QPushButton(self.frame_ouvertureImg)
        self.bouton_ouvrirImgIn.setObjectName(u"bouton_ouvrirImgIn")
        self.bouton_ouvrirImgIn.setGeometry(QRect(160, 150, 75, 24))
        self.bouton_ouvrirImgIn.setAutoFillBackground(False)
        self.bouton_ouvrirImgIn.setCheckable(False)
        self.label_background = QLabel(self.frame_ouvertureImg)
        self.label_background.setObjectName(u"label_background")
        self.label_background.setGeometry(QRect(0, 0, 400, 200))
        self.label_background.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px inset #32194d; \n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_barre_taches_5 = QFrame(self.frame_ouvertureImg)
        self.frame_barre_taches_5.setObjectName(u"frame_barre_taches_5")
        self.frame_barre_taches_5.setGeometry(QRect(0, 0, 400, 30))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_barre_taches_5.sizePolicy().hasHeightForWidth())
        self.frame_barre_taches_5.setSizePolicy(sizePolicy)
        self.frame_barre_taches_5.setLayoutDirection(Qt.LeftToRight)
        self.frame_barre_taches_5.setStyleSheet(u"border: 2px inset #32194d; \n"
"border-top-left-radius: 0;\n"
"border-top-right-radius: 0;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0;")
        self.frame_barre_taches_5.setFrameShape(QFrame.NoFrame)
        self.frame_barre_taches_5.setFrameShadow(QFrame.Plain)
        self.horizontalLayoutWidget_11 = QWidget(self.frame_barre_taches_5)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(0, 0, 401, 31))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_19 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_19)

        self.label_textebarre_5 = QLabel(self.horizontalLayoutWidget_11)
        self.label_textebarre_5.setObjectName(u"label_textebarre_5")
        self.label_textebarre_5.setStyleSheet(u"border:0;\n"
"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.label_textebarre_5)

        self.bouton_rouge_5 = QFrame(self.horizontalLayoutWidget_11)
        self.bouton_rouge_5.setObjectName(u"bouton_rouge_5")
        self.bouton_rouge_5.setMaximumSize(QSize(15, 15))
        self.bouton_rouge_5.setStyleSheet(u"border-radius: 7px;\n"
"background-color: #d46464;")
        self.bouton_rouge_5.setFrameShape(QFrame.StyledPanel)
        self.bouton_rouge_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.bouton_rouge_5)

        self.horizontalSpacer_20 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_20)

        self.label_barretaches_background_5 = QLabel(self.frame_ouvertureImg)
        self.label_barretaches_background_5.setObjectName(u"label_barretaches_background_5")
        self.label_barretaches_background_5.setGeometry(QRect(0, 0, 401, 30))
        self.label_barretaches_background_5.setStyleSheet(u"background-color: #fff3b0;")
        self.label_background.raise_()
        self.label_barretaches_background_5.raise_()
        self.labeltext_chemin.raise_()
        self.bouton_ouvrirImgIn.raise_()
        self.frame_barre_taches_5.raise_()
        self.frame_ImgNoisy = QFrame(self.centralwidget)
        self.frame_ImgNoisy.setObjectName(u"frame_ImgNoisy")
        self.frame_ImgNoisy.setEnabled(True)
        self.frame_ImgNoisy.setGeometry(QRect(710, 450, 500, 500))
        self.frame_ImgNoisy.setFrameShape(QFrame.StyledPanel)
        self.frame_ImgNoisy.setFrameShadow(QFrame.Raised)
        self.label_ImgNoisy = QLabel(self.frame_ImgNoisy)
        self.label_ImgNoisy.setObjectName(u"label_ImgNoisy")
        self.label_ImgNoisy.setGeometry(QRect(0, 0, 500, 500))
        self.label_ImgNoisy.setAlignment(Qt.AlignCenter)
        self.frame_ImgIn_background = QFrame(self.centralwidget)
        self.frame_ImgIn_background.setObjectName(u"frame_ImgIn_background")
        self.frame_ImgIn_background.setGeometry(QRect(80, 400, 550, 570))
        self.frame_ImgIn_background.setAutoFillBackground(False)
        self.frame_ImgIn_background.setFrameShape(QFrame.NoFrame)
        self.frame_ImgIn_background.setFrameShadow(QFrame.Plain)
        self.label_ImgIn_background = QLabel(self.frame_ImgIn_background)
        self.label_ImgIn_background.setObjectName(u"label_ImgIn_background")
        self.label_ImgIn_background.setGeometry(QRect(0, 0, 550, 570))
        self.label_ImgIn_background.setAutoFillBackground(False)
        self.label_ImgIn_background.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px inset #32194d; \n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_barre_taches = QFrame(self.frame_ImgIn_background)
        self.frame_barre_taches.setObjectName(u"frame_barre_taches")
        self.frame_barre_taches.setGeometry(QRect(0, 0, 550, 30))
        sizePolicy.setHeightForWidth(self.frame_barre_taches.sizePolicy().hasHeightForWidth())
        self.frame_barre_taches.setSizePolicy(sizePolicy)
        self.frame_barre_taches.setLayoutDirection(Qt.LeftToRight)
        self.frame_barre_taches.setStyleSheet(u"border: 2px inset #32194d; \n"
"border-top-left-radius: 0;\n"
"border-top-right-radius: 0;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0;")
        self.frame_barre_taches.setFrameShape(QFrame.NoFrame)
        self.frame_barre_taches.setFrameShadow(QFrame.Plain)
        self.horizontalLayoutWidget_7 = QWidget(self.frame_barre_taches)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 551, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.label_textebarre = QLabel(self.horizontalLayoutWidget_7)
        self.label_textebarre.setObjectName(u"label_textebarre")
        self.label_textebarre.setStyleSheet(u"border:0;\n"
"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.label_textebarre)

        self.bouton_rouge = QFrame(self.horizontalLayoutWidget_7)
        self.bouton_rouge.setObjectName(u"bouton_rouge")
        self.bouton_rouge.setMaximumSize(QSize(15, 15))
        self.bouton_rouge.setStyleSheet(u"border-radius: 7px;\n"
"background-color: #d46464;")
        self.bouton_rouge.setFrameShape(QFrame.StyledPanel)
        self.bouton_rouge.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.bouton_rouge)

        self.horizontalSpacer_12 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)

        self.label_barretaches_background = QLabel(self.frame_ImgIn_background)
        self.label_barretaches_background.setObjectName(u"label_barretaches_background")
        self.label_barretaches_background.setGeometry(QRect(0, 0, 550, 30))
        self.label_barretaches_background.setStyleSheet(u"background-color: #d1d1f0;")
        self.label_ImgIn_background.raise_()
        self.label_barretaches_background.raise_()
        self.frame_barre_taches.raise_()
        self.frame_ImgNoisy_background = QFrame(self.centralwidget)
        self.frame_ImgNoisy_background.setObjectName(u"frame_ImgNoisy_background")
        self.frame_ImgNoisy_background.setGeometry(QRect(685, 400, 550, 570))
        self.frame_ImgNoisy_background.setAutoFillBackground(False)
        self.frame_ImgNoisy_background.setFrameShape(QFrame.NoFrame)
        self.frame_ImgNoisy_background.setFrameShadow(QFrame.Plain)
        self.label_ImgNoisy_background = QLabel(self.frame_ImgNoisy_background)
        self.label_ImgNoisy_background.setObjectName(u"label_ImgNoisy_background")
        self.label_ImgNoisy_background.setGeometry(QRect(0, 0, 550, 570))
        self.label_ImgNoisy_background.setAutoFillBackground(False)
        self.label_ImgNoisy_background.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px inset #32194d; \n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_barre_taches_3 = QFrame(self.frame_ImgNoisy_background)
        self.frame_barre_taches_3.setObjectName(u"frame_barre_taches_3")
        self.frame_barre_taches_3.setGeometry(QRect(0, 0, 550, 30))
        sizePolicy.setHeightForWidth(self.frame_barre_taches_3.sizePolicy().hasHeightForWidth())
        self.frame_barre_taches_3.setSizePolicy(sizePolicy)
        self.frame_barre_taches_3.setLayoutDirection(Qt.LeftToRight)
        self.frame_barre_taches_3.setStyleSheet(u"border: 2px inset #32194d; \n"
"border-top-left-radius: 0;\n"
"border-top-right-radius: 0;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0;")
        self.frame_barre_taches_3.setFrameShape(QFrame.NoFrame)
        self.frame_barre_taches_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayoutWidget_9 = QWidget(self.frame_barre_taches_3)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(0, 0, 551, 31))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)

        self.label_textebarre_3 = QLabel(self.horizontalLayoutWidget_9)
        self.label_textebarre_3.setObjectName(u"label_textebarre_3")
        self.label_textebarre_3.setStyleSheet(u"border:0;\n"
"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.label_textebarre_3)

        self.bouton_save_ImgNoisy = QPushButton(self.horizontalLayoutWidget_9)
        self.bouton_save_ImgNoisy.setObjectName(u"bouton_save_ImgNoisy")
        self.bouton_save_ImgNoisy.setMaximumSize(QSize(100, 20))
        self.bouton_save_ImgNoisy.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.bouton_save_ImgNoisy)

        self.bouton_rouge_3 = QFrame(self.horizontalLayoutWidget_9)
        self.bouton_rouge_3.setObjectName(u"bouton_rouge_3")
        self.bouton_rouge_3.setMaximumSize(QSize(15, 15))
        self.bouton_rouge_3.setStyleSheet(u"border-radius: 7px;\n"
"background-color: #d46464;")
        self.bouton_rouge_3.setFrameShape(QFrame.StyledPanel)
        self.bouton_rouge_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.bouton_rouge_3)

        self.horizontalSpacer_16 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_16)

        self.label_barretaches_background_3 = QLabel(self.frame_ImgNoisy_background)
        self.label_barretaches_background_3.setObjectName(u"label_barretaches_background_3")
        self.label_barretaches_background_3.setGeometry(QRect(0, 0, 550, 30))
        self.label_barretaches_background_3.setStyleSheet(u"background-color: #f5cac3;")
        self.label_ImgNoisy_background.raise_()
        self.label_barretaches_background_3.raise_()
        self.frame_barre_taches_3.raise_()
        self.frame_ImgOut_background = QFrame(self.centralwidget)
        self.frame_ImgOut_background.setObjectName(u"frame_ImgOut_background")
        self.frame_ImgOut_background.setGeometry(QRect(1290, 400, 550, 570))
        self.frame_ImgOut_background.setAutoFillBackground(False)
        self.frame_ImgOut_background.setFrameShape(QFrame.NoFrame)
        self.frame_ImgOut_background.setFrameShadow(QFrame.Plain)
        self.label_ImgOut_background = QLabel(self.frame_ImgOut_background)
        self.label_ImgOut_background.setObjectName(u"label_ImgOut_background")
        self.label_ImgOut_background.setGeometry(QRect(0, 0, 550, 570))
        self.label_ImgOut_background.setAutoFillBackground(False)
        self.label_ImgOut_background.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px inset #32194d; \n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_barre_taches_4 = QFrame(self.frame_ImgOut_background)
        self.frame_barre_taches_4.setObjectName(u"frame_barre_taches_4")
        self.frame_barre_taches_4.setGeometry(QRect(0, 0, 550, 30))
        sizePolicy.setHeightForWidth(self.frame_barre_taches_4.sizePolicy().hasHeightForWidth())
        self.frame_barre_taches_4.setSizePolicy(sizePolicy)
        self.frame_barre_taches_4.setLayoutDirection(Qt.LeftToRight)
        self.frame_barre_taches_4.setStyleSheet(u"border: 2px inset #32194d; \n"
"border-top-left-radius: 0;\n"
"border-top-right-radius: 0;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0;")
        self.frame_barre_taches_4.setFrameShape(QFrame.NoFrame)
        self.frame_barre_taches_4.setFrameShadow(QFrame.Plain)
        self.horizontalLayoutWidget_10 = QWidget(self.frame_barre_taches_4)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(0, 0, 551, 31))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_17)

        self.label_textebarre_4 = QLabel(self.horizontalLayoutWidget_10)
        self.label_textebarre_4.setObjectName(u"label_textebarre_4")
        self.label_textebarre_4.setStyleSheet(u"border:0;\n"
"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"")

        self.horizontalLayout_9.addWidget(self.label_textebarre_4)

        self.bouton_save_ImgOut = QPushButton(self.horizontalLayoutWidget_10)
        self.bouton_save_ImgOut.setObjectName(u"bouton_save_ImgOut")
        self.bouton_save_ImgOut.setMaximumSize(QSize(100, 20))
        self.bouton_save_ImgOut.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.bouton_save_ImgOut)

        self.bouton_rouge_4 = QFrame(self.horizontalLayoutWidget_10)
        self.bouton_rouge_4.setObjectName(u"bouton_rouge_4")
        self.bouton_rouge_4.setMaximumSize(QSize(15, 15))
        self.bouton_rouge_4.setStyleSheet(u"border-radius: 7px;\n"
"background-color: #d46464;")
        self.bouton_rouge_4.setFrameShape(QFrame.StyledPanel)
        self.bouton_rouge_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.bouton_rouge_4)

        self.horizontalSpacer_18 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_18)

        self.label_barretaches_background_4 = QLabel(self.frame_ImgOut_background)
        self.label_barretaches_background_4.setObjectName(u"label_barretaches_background_4")
        self.label_barretaches_background_4.setGeometry(QRect(0, 0, 550, 30))
        self.label_barretaches_background_4.setStyleSheet(u"background-color: #cad2c5;")
        self.label_ImgOut_background.raise_()
        self.label_barretaches_background_4.raise_()
        self.frame_barre_taches_4.raise_()
        self.frame_tabWidget = QFrame(self.centralwidget)
        self.frame_tabWidget.setObjectName(u"frame_tabWidget")
        self.frame_tabWidget.setGeometry(QRect(650, 30, 620, 320))
        self.frame_tabWidget.setFrameShape(QFrame.StyledPanel)
        self.frame_tabWidget.setFrameShadow(QFrame.Raised)
        self.tabWidget_cfg = QTabWidget(self.frame_tabWidget)
        self.tabWidget_cfg.setObjectName(u"tabWidget_cfg")
        self.tabWidget_cfg.setEnabled(True)
        self.tabWidget_cfg.setGeometry(QRect(10, 40, 600, 261))
        self.tabWidget_cfg.setAutoFillBackground(False)
        self.tabWidget_cfg.setStyleSheet(u"")
        self.GenBruit = QWidget()
        self.GenBruit.setObjectName(u"GenBruit")
        self.gridLayoutWidget = QWidget(self.GenBruit)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(120, 40, 361, 116))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bouton_poivresel = QPushButton(self.gridLayoutWidget)
        self.bouton_poivresel.setObjectName(u"bouton_poivresel")
        self.bouton_poivresel.setEnabled(True)

        self.gridLayout.addWidget(self.bouton_poivresel, 1, 2, 1, 1)

        self.bouton_chromatique = QPushButton(self.gridLayoutWidget)
        self.bouton_chromatique.setObjectName(u"bouton_chromatique")

        self.gridLayout.addWidget(self.bouton_chromatique, 0, 3, 1, 1)

        self.bouton_gaussien = QPushButton(self.gridLayoutWidget)
        self.bouton_gaussien.setObjectName(u"bouton_gaussien")

        self.gridLayout.addWidget(self.bouton_gaussien, 0, 2, 1, 1)

        self.vLay_ecart_type = QVBoxLayout()
        self.vLay_ecart_type.setObjectName(u"vLay_ecart_type")
        self.vLay_ecart_type.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_ecart_type = QLabel(self.gridLayoutWidget)
        self.label_ecart_type.setObjectName(u"label_ecart_type")

        self.vLay_ecart_type.addWidget(self.label_ecart_type)

        self.slider_ecart_type = QSlider(self.gridLayoutWidget)
        self.slider_ecart_type.setObjectName(u"slider_ecart_type")
        self.slider_ecart_type.setOrientation(Qt.Horizontal)

        self.vLay_ecart_type.addWidget(self.slider_ecart_type)


        self.gridLayout.addLayout(self.vLay_ecart_type, 0, 0, 1, 1)

        self.vLay_densite = QVBoxLayout()
        self.vLay_densite.setObjectName(u"vLay_densite")
        self.label_densite = QLabel(self.gridLayoutWidget)
        self.label_densite.setObjectName(u"label_densite")

        self.vLay_densite.addWidget(self.label_densite)

        self.slider_densite = QSlider(self.gridLayoutWidget)
        self.slider_densite.setObjectName(u"slider_densite")
        self.slider_densite.setOrientation(Qt.Horizontal)

        self.vLay_densite.addWidget(self.slider_densite)


        self.gridLayout.addLayout(self.vLay_densite, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.bouton_deja_bruitee = QPushButton(self.GenBruit)
        self.bouton_deja_bruitee.setObjectName(u"bouton_deja_bruitee")
        self.bouton_deja_bruitee.setGeometry(QRect(230, 200, 131, 24))
        self.tabWidget_cfg.addTab(self.GenBruit, "")
        self.Filtres = QWidget()
        self.Filtres.setObjectName(u"Filtres")
        self.bouton_valider = QPushButton(self.Filtres)
        self.bouton_valider.setObjectName(u"bouton_valider")
        self.bouton_valider.setGeometry(QRect(510, 190, 75, 24))
        self.horizontalLayoutWidget = QWidget(self.Filtres)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 251, 128))
        self.hLay_filtres = QHBoxLayout(self.horizontalLayoutWidget)
        self.hLay_filtres.setObjectName(u"hLay_filtres")
        self.hLay_filtres.setContentsMargins(0, 0, 0, 0)
        self.vLa_filtres = QVBoxLayout()
        self.vLa_filtres.setObjectName(u"vLa_filtres")
        self.radio_gaussien = QRadioButton(self.horizontalLayoutWidget)
        self.radio_gaussien.setObjectName(u"radio_gaussien")

        self.vLa_filtres.addWidget(self.radio_gaussien)

        self.radio_moyenneur = QRadioButton(self.horizontalLayoutWidget)
        self.radio_moyenneur.setObjectName(u"radio_moyenneur")

        self.vLa_filtres.addWidget(self.radio_moyenneur)

        self.radio_bilateral = QRadioButton(self.horizontalLayoutWidget)
        self.radio_bilateral.setObjectName(u"radio_bilateral")

        self.vLa_filtres.addWidget(self.radio_bilateral)

        self.radio_median = QRadioButton(self.horizontalLayoutWidget)
        self.radio_median.setObjectName(u"radio_median")

        self.vLa_filtres.addWidget(self.radio_median)

        self.radio_papier = QRadioButton(self.horizontalLayoutWidget)
        self.radio_papier.setObjectName(u"radio_papier")

        self.vLa_filtres.addWidget(self.radio_papier)


        self.hLay_filtres.addLayout(self.vLa_filtres)

        self.radio_laplacien = QRadioButton(self.horizontalLayoutWidget)
        self.radio_laplacien.setObjectName(u"radio_laplacien")

        self.hLay_filtres.addWidget(self.radio_laplacien)

        self.label_papier = QLabel(self.Filtres)
        self.label_papier.setObjectName(u"label_papier")
        self.label_papier.setGeometry(QRect(10, 150, 251, 61))
        self.gridLayoutWidget_2 = QWidget(self.Filtres)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(270, 10, 321, 176))
        self.gLay_options_filter = QGridLayout(self.gridLayoutWidget_2)
        self.gLay_options_filter.setObjectName(u"gLay_options_filter")
        self.gLay_options_filter.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gLay_options_filter.setContentsMargins(0, 0, 0, 0)
        self.vLay_var_spatiale = QVBoxLayout()
        self.vLay_var_spatiale.setObjectName(u"vLay_var_spatiale")
        self.label_var_spatiale = QLabel(self.gridLayoutWidget_2)
        self.label_var_spatiale.setObjectName(u"label_var_spatiale")

        self.vLay_var_spatiale.addWidget(self.label_var_spatiale)

        self.slider_var_spatiale = QSlider(self.gridLayoutWidget_2)
        self.slider_var_spatiale.setObjectName(u"slider_var_spatiale")
        self.slider_var_spatiale.setOrientation(Qt.Horizontal)

        self.vLay_var_spatiale.addWidget(self.slider_var_spatiale)


        self.gLay_options_filter.addLayout(self.vLay_var_spatiale, 1, 1, 1, 1)

        self.vLay_diametre = QVBoxLayout()
        self.vLay_diametre.setObjectName(u"vLay_diametre")
        self.label_diametre = QLabel(self.gridLayoutWidget_2)
        self.label_diametre.setObjectName(u"label_diametre")
        self.label_diametre.setEnabled(True)

        self.vLay_diametre.addWidget(self.label_diametre)

        self.slider_diametre = QSlider(self.gridLayoutWidget_2)
        self.slider_diametre.setObjectName(u"slider_diametre")
        self.slider_diametre.setEnabled(True)
        self.slider_diametre.setOrientation(Qt.Horizontal)

        self.vLay_diametre.addWidget(self.slider_diametre)


        self.gLay_options_filter.addLayout(self.vLay_diametre, 0, 1, 1, 1)

        self.vLay_taille = QVBoxLayout()
        self.vLay_taille.setObjectName(u"vLay_taille")
        self.label_taille = QLabel(self.gridLayoutWidget_2)
        self.label_taille.setObjectName(u"label_taille")

        self.vLay_taille.addWidget(self.label_taille)

        self.slider_taille = QSlider(self.gridLayoutWidget_2)
        self.slider_taille.setObjectName(u"slider_taille")
        self.slider_taille.setOrientation(Qt.Horizontal)

        self.vLay_taille.addWidget(self.slider_taille)


        self.gLay_options_filter.addLayout(self.vLay_taille, 1, 0, 1, 1)

        self.vLay_radius = QVBoxLayout()
        self.vLay_radius.setObjectName(u"vLay_radius")
        self.label_radius = QLabel(self.gridLayoutWidget_2)
        self.label_radius.setObjectName(u"label_radius")

        self.vLay_radius.addWidget(self.label_radius)

        self.slider_radius = QSlider(self.gridLayoutWidget_2)
        self.slider_radius.setObjectName(u"slider_radius")
        self.slider_radius.setOrientation(Qt.Horizontal)
        self.slider_radius.setInvertedControls(False)
        self.slider_radius.setTickPosition(QSlider.NoTicks)

        self.vLay_radius.addWidget(self.slider_radius)


        self.gLay_options_filter.addLayout(self.vLay_radius, 0, 0, 1, 1)

        self.vLay_var_couleur = QVBoxLayout()
        self.vLay_var_couleur.setObjectName(u"vLay_var_couleur")
        self.label_var_couleur = QLabel(self.gridLayoutWidget_2)
        self.label_var_couleur.setObjectName(u"label_var_couleur")

        self.vLay_var_couleur.addWidget(self.label_var_couleur)

        self.slider_var_couleur = QSlider(self.gridLayoutWidget_2)
        self.slider_var_couleur.setObjectName(u"slider_var_couleur")
        self.slider_var_couleur.setOrientation(Qt.Horizontal)

        self.vLay_var_couleur.addWidget(self.slider_var_couleur)


        self.gLay_options_filter.addLayout(self.vLay_var_couleur, 2, 1, 1, 1)

        self.tabWidget_cfg.addTab(self.Filtres, "")
        self.ReseauNeurone = QWidget()
        self.ReseauNeurone.setObjectName(u"ReseauNeurone")
        self.bouton_MPRNet = QPushButton(self.ReseauNeurone)
        self.bouton_MPRNet.setObjectName(u"bouton_MPRNet")
        self.bouton_MPRNet.setGeometry(QRect(260, 80, 75, 24))
        self.tabWidget_cfg.addTab(self.ReseauNeurone, "")
        self.label_background_2 = QLabel(self.frame_tabWidget)
        self.label_background_2.setObjectName(u"label_background_2")
        self.label_background_2.setGeometry(QRect(0, 0, 620, 320))
        self.label_background_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px inset #32194d; \n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_barretaches_background_6 = QLabel(self.frame_tabWidget)
        self.label_barretaches_background_6.setObjectName(u"label_barretaches_background_6")
        self.label_barretaches_background_6.setGeometry(QRect(0, 0, 620, 30))
        self.label_barretaches_background_6.setStyleSheet(u"background-color: #bde0fe;")
        self.frame_barre_taches_6 = QFrame(self.frame_tabWidget)
        self.frame_barre_taches_6.setObjectName(u"frame_barre_taches_6")
        self.frame_barre_taches_6.setGeometry(QRect(0, 0, 620, 30))
        sizePolicy.setHeightForWidth(self.frame_barre_taches_6.sizePolicy().hasHeightForWidth())
        self.frame_barre_taches_6.setSizePolicy(sizePolicy)
        self.frame_barre_taches_6.setLayoutDirection(Qt.LeftToRight)
        self.frame_barre_taches_6.setStyleSheet(u"border: 2px inset #32194d; \n"
"border-top-left-radius: 0;\n"
"border-top-right-radius: 0;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0;")
        self.frame_barre_taches_6.setFrameShape(QFrame.NoFrame)
        self.frame_barre_taches_6.setFrameShadow(QFrame.Plain)
        self.horizontalLayoutWidget_13 = QWidget(self.frame_barre_taches_6)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(0, 0, 621, 31))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_23 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_23)

        self.label_textebarre_7 = QLabel(self.horizontalLayoutWidget_13)
        self.label_textebarre_7.setObjectName(u"label_textebarre_7")
        self.label_textebarre_7.setStyleSheet(u"border:0;\n"
"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"")

        self.horizontalLayout_12.addWidget(self.label_textebarre_7)

        self.bouton_rouge_7 = QFrame(self.horizontalLayoutWidget_13)
        self.bouton_rouge_7.setObjectName(u"bouton_rouge_7")
        self.bouton_rouge_7.setMaximumSize(QSize(15, 15))
        self.bouton_rouge_7.setStyleSheet(u"border-radius: 7px;\n"
"background-color: #d46464;")
        self.bouton_rouge_7.setFrameShape(QFrame.StyledPanel)
        self.bouton_rouge_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.bouton_rouge_7)

        self.horizontalSpacer_24 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_24)

        self.label_background_2.raise_()
        self.tabWidget_cfg.raise_()
        self.label_barretaches_background_6.raise_()
        self.frame_barre_taches_6.raise_()
        self.frame_metriques = QFrame(self.centralwidget)
        self.frame_metriques.setObjectName(u"frame_metriques")
        self.frame_metriques.setGeometry(QRect(1355, 100, 400, 200))
        self.frame_metriques.setFrameShape(QFrame.StyledPanel)
        self.frame_metriques.setFrameShadow(QFrame.Raised)
        self.label_background_3 = QLabel(self.frame_metriques)
        self.label_background_3.setObjectName(u"label_background_3")
        self.label_background_3.setGeometry(QRect(0, 0, 400, 200))
        self.label_background_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px inset #32194d; \n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_barretaches_background_7 = QLabel(self.frame_metriques)
        self.label_barretaches_background_7.setObjectName(u"label_barretaches_background_7")
        self.label_barretaches_background_7.setGeometry(QRect(0, 0, 401, 30))
        self.label_barretaches_background_7.setStyleSheet(u"background-color: #f2cc8f;")
        self.frame_barre_taches_7 = QFrame(self.frame_metriques)
        self.frame_barre_taches_7.setObjectName(u"frame_barre_taches_7")
        self.frame_barre_taches_7.setGeometry(QRect(0, 0, 400, 30))
        sizePolicy.setHeightForWidth(self.frame_barre_taches_7.sizePolicy().hasHeightForWidth())
        self.frame_barre_taches_7.setSizePolicy(sizePolicy)
        self.frame_barre_taches_7.setLayoutDirection(Qt.LeftToRight)
        self.frame_barre_taches_7.setStyleSheet(u"border: 2px inset #32194d; \n"
"border-top-left-radius: 0;\n"
"border-top-right-radius: 0;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0;")
        self.frame_barre_taches_7.setFrameShape(QFrame.NoFrame)
        self.frame_barre_taches_7.setFrameShadow(QFrame.Plain)
        self.horizontalLayoutWidget_14 = QWidget(self.frame_barre_taches_7)
        self.horizontalLayoutWidget_14.setObjectName(u"horizontalLayoutWidget_14")
        self.horizontalLayoutWidget_14.setGeometry(QRect(0, 0, 401, 31))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_25 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_25)

        self.label_textebarre_8 = QLabel(self.horizontalLayoutWidget_14)
        self.label_textebarre_8.setObjectName(u"label_textebarre_8")
        self.label_textebarre_8.setStyleSheet(u"border:0;\n"
"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"")

        self.horizontalLayout_13.addWidget(self.label_textebarre_8)

        self.bouton_rouge_8 = QFrame(self.horizontalLayoutWidget_14)
        self.bouton_rouge_8.setObjectName(u"bouton_rouge_8")
        self.bouton_rouge_8.setMaximumSize(QSize(15, 15))
        self.bouton_rouge_8.setStyleSheet(u"border-radius: 7px;\n"
"background-color: #d46464;")
        self.bouton_rouge_8.setFrameShape(QFrame.StyledPanel)
        self.bouton_rouge_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.bouton_rouge_8)

        self.horizontalSpacer_26 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_26)

        self.tabWidget_Mesure = QTabWidget(self.frame_metriques)
        self.tabWidget_Mesure.setObjectName(u"tabWidget_Mesure")
        self.tabWidget_Mesure.setGeometry(QRect(50, 40, 300, 150))
        self.tabWidget_Mesure.setTabPosition(QTabWidget.North)
        self.tabWidget_Mesure.setTabShape(QTabWidget.Rounded)
        self.tabWidget_Mesure.setElideMode(Qt.ElideNone)
        self.tabWidget_Mesure.setDocumentMode(False)
        self.tabWidget_Mesure.setTabsClosable(False)
        self.tabWidget_Mesure.setMovable(False)
        self.PSNR = QWidget()
        self.PSNR.setObjectName(u"PSNR")
        self.horizontalLayoutWidget_2 = QWidget(self.PSNR)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(60, 40, 161, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_PSNR = QLabel(self.horizontalLayoutWidget_2)
        self.label_PSNR.setObjectName(u"label_PSNR")
        self.label_PSNR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_PSNR)

        self.horizontalSpacer_2 = QSpacerItem(15, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.tabWidget_Mesure.addTab(self.PSNR, "")
        self.SSIM = QWidget()
        self.SSIM.setObjectName(u"SSIM")
        self.label_SSIM = QLabel(self.SSIM)
        self.label_SSIM.setObjectName(u"label_SSIM")
        self.label_SSIM.setGeometry(QRect(130, 30, 49, 21))
        self.label = QLabel(self.SSIM)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 280, 50))
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.tabWidget_Mesure.addTab(self.SSIM, "")
        self.label_titre = QLabel(self.centralwidget)
        self.label_titre.setObjectName(u"label_titre")
        self.label_titre.setGeometry(QRect(1720, 0, 201, 71))
        font = QFont()
        font.setFamilies([u"Meow Script"])
        font.setPointSize(40)
        self.label_titre.setFont(font)
        self.label_titre.setStyleSheet(u"color: grey;")
        self.label_titre.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.background.raise_()
        self.frame_ImgOut_background.raise_()
        self.frame_ImgNoisy_background.raise_()
        self.frame_ImgIn_background.raise_()
        self.frame_ImgIn.raise_()
        self.frame_ImgOut.raise_()
        self.frame_ouvertureImg.raise_()
        self.frame_ImgNoisy.raise_()
        self.frame_tabWidget.raise_()
        self.frame_metriques.raise_()
        self.label_titre.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_cfg.setCurrentIndex(0)
        self.tabWidget_Mesure.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Christal", None))
        self.label_ImgIn.setText(QCoreApplication.translate("MainWindow", u"Ouvrir une image...", None))
        self.label_ImgOut.setText(QCoreApplication.translate("MainWindow", u"Appliquer une modification...", None))
        self.background.setText("")
        self.labeltext_chemin.setText(QCoreApplication.translate("MainWindow", u"Chemin du fichier ", None))
        self.bouton_ouvrirImgIn.setText(QCoreApplication.translate("MainWindow", u"Ouvrir image", None))
        self.label_textebarre_5.setText(QCoreApplication.translate("MainWindow", u"Ouvrir une image", None))
        self.label_barretaches_background_5.setText("")
        self.label_ImgNoisy.setText(QCoreApplication.translate("MainWindow", u"Appliquer une modification", None))
        self.label_textebarre.setText(QCoreApplication.translate("MainWindow", u"Image Originale", None))
        self.label_barretaches_background.setText("")
        self.label_textebarre_3.setText(QCoreApplication.translate("MainWindow", u"Image Bruit\u00e9e", None))
        self.bouton_save_ImgNoisy.setText(QCoreApplication.translate("MainWindow", u"Sauvegarder", None))
        self.label_barretaches_background_3.setText("")
        self.label_textebarre_4.setText(QCoreApplication.translate("MainWindow", u"Image D\u00e9bruit\u00e9e", None))
        self.bouton_save_ImgOut.setText(QCoreApplication.translate("MainWindow", u"Sauvegarder", None))
        self.label_barretaches_background_4.setText("")
        self.bouton_poivresel.setText(QCoreApplication.translate("MainWindow", u"PoivreEtSel", None))
        self.bouton_chromatique.setText(QCoreApplication.translate("MainWindow", u"Chromatique", None))
        self.bouton_gaussien.setText(QCoreApplication.translate("MainWindow", u"Gaussien", None))
        self.label_ecart_type.setText(QCoreApplication.translate("MainWindow", u"Ecart-type :", None))
        self.label_densite.setText(QCoreApplication.translate("MainWindow", u"Densit\u00e9 :", None))
        self.bouton_deja_bruitee.setText(QCoreApplication.translate("MainWindow", u"Image d\u00e9j\u00e0 bruit\u00e9e", None))
        self.tabWidget_cfg.setTabText(self.tabWidget_cfg.indexOf(self.GenBruit), QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rateur de bruit", None))
        self.bouton_valider.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.radio_gaussien.setText(QCoreApplication.translate("MainWindow", u"Filtrage Gaussien", None))
        self.radio_moyenneur.setText(QCoreApplication.translate("MainWindow", u"Filtrage Moyenneur", None))
        self.radio_bilateral.setText(QCoreApplication.translate("MainWindow", u"Filtrage Bilat\u00e9ral", None))
        self.radio_median.setText(QCoreApplication.translate("MainWindow", u"Filtrage M\u00e9dian", None))
        self.radio_papier.setText(QCoreApplication.translate("MainWindow", u"Filtrage Papier*", None))
        self.radio_laplacien.setText(QCoreApplication.translate("MainWindow", u"Filtrage Laplacien", None))
        self.label_papier.setText(QCoreApplication.translate("MainWindow", u"*Filtrage Papier : m\u00e9thode impl\u00e9ment\u00e9e", None))
        self.label_var_spatiale.setText(QCoreApplication.translate("MainWindow", u"Variance spatiale :", None))
        self.label_diametre.setText(QCoreApplication.translate("MainWindow", u"Diam\u00e8tre voisinage :", None))
        self.label_taille.setText(QCoreApplication.translate("MainWindow", u"Taille voisinage :", None))
        self.label_radius.setText(QCoreApplication.translate("MainWindow", u"Taille noyau :", None))
        self.label_var_couleur.setText(QCoreApplication.translate("MainWindow", u"Variance couleur :", None))
        self.tabWidget_cfg.setTabText(self.tabWidget_cfg.indexOf(self.Filtres), QCoreApplication.translate("MainWindow", u"Filtrages", None))
        self.bouton_MPRNet.setText(QCoreApplication.translate("MainWindow", u"MPRNet", None))
        self.tabWidget_cfg.setTabText(self.tabWidget_cfg.indexOf(self.ReseauNeurone), QCoreApplication.translate("MainWindow", u"R\u00e9seau de neurones", None))
        self.label_barretaches_background_6.setText("")
        self.label_textebarre_7.setText(QCoreApplication.translate("MainWindow", u"Outils", None))
        self.label_background_3.setText("")
        self.label_barretaches_background_7.setText("")
        self.label_textebarre_8.setText(QCoreApplication.translate("MainWindow", u"M\u00e9triques", None))
        self.label_PSNR.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"dB", None))
        self.tabWidget_Mesure.setTabText(self.tabWidget_Mesure.indexOf(self.PSNR), QCoreApplication.translate("MainWindow", u"PSNR", None))
        self.label_SSIM.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Un coefficient de 1 indique une similarit\u00e9 parfaite entre les deux images.", None))
        self.tabWidget_Mesure.setTabText(self.tabWidget_Mesure.indexOf(self.SSIM), QCoreApplication.translate("MainWindow", u"SSIM", None))
        self.label_titre.setText(QCoreApplication.translate("MainWindow", u"Christal", None))
    # retranslateUi

