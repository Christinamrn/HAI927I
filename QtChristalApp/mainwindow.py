# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PySide6.QtGui import QPixmap
from PIL import Image
from imageSettings import *
from imageGenNoises import *

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #--------------
        #INITIALISATION
        #--------------

        #Variables Booléennes
        self.ImageInIsSet = False
        self.ImageNdg = False
        self.ImageModified = False

        #Variables quantitatives
        self.ecart_type = 20
        self.densite = 0.01

        #Lien entre les boutons UI et les fonctions
        self.ui.bouton_ouvrirImgIn.clicked.connect(self.ouvrirImage)

        #Ne pas autoriser le changement d'état des boutons
        self.ui.bouton_poivresel.setVisible(False)
        self.ui.bouton_gaussien.setVisible(False)
        self.ui.bouton_chromatique.setVisible(False)
        self.ui.bouton_poivresel.setEnabled(False)
        self.ui.bouton_gaussien.setEnabled(False)
        self.ui.bouton_chromatique.setEnabled(False)



    def ouvrirImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Sélectionner une image", "", "Images (*.png *.jpg *.jpeg *.gif *.bmp)", options=options)
        if fileName:
            #Affichage du chemin de l'image sur l'UI
            self.ui.labeltext_chemin.setText(fileName)
            #Conversion Image en QPixmap
            pixmap = QPixmap(fileName)
            #Affichage de l'image dans un label
            self.ui.label_ImgIn.setPixmap(pixmap)
            self.ui.label_ImgIn.setScaledContents(True)
            image = ouvrirImageIn(fileName)
            ImageInSet = True
            self.ImageNdg = IsNdg(image)

            #Lien entre les boutons liés à "image" et les fonctions
            #self.ui.bouton_poivresel.connect(bruit_poivre_et_sel)
            #self.ui.bouton_gaussien.connect(bruit_gaussien)
            self.ui.bouton_chromatique.clicked.connect(lambda : bruit_chromatique(image, self.ecart_type, self.ImageModified))

            #Si l'image d'origine existe
            if(self.ImageInIsSet):
                if(self.ImageNdg):
                    self.ui.bouton_poivresel.setEnabled(True)
                    self.ui.bouton_gaussien.setEnabled(True)
                else:
                    self.ui.bouton_chromatique.setVisible(True)
                    self.ui.bouton_chromatique.setEnabled(True)

            if (self.ImageModified):
                affichageImageOut

    def affichageImageOut(self):
        chemin_dossier_temp = tempfile.gettempdir() + "\ImgChristalTmp.jpg"
        pixmap = QPixmap(chemin_dossier_temp)
        self.ui.label_ImgOut.setPixmap(pixmap)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
