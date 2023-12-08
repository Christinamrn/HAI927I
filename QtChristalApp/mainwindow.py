# This Python file uses the following encoding: utf-8
import sys
import os
import cv2
import tempfile

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QDialog
from PySide6.QtGui import QPixmap, QImage, QTransform
from PySide6.QtCore import QObject, Slot, Qt, QSize, QStandardPaths
#from PyQt6.QtCore import QObject, pyqtSlot, Qt, QSize
from PIL import Image
from imageSettings import *
from imageGenNoises import *
from imageFiltresTrad import *
from imageMesure import *
from imageMPRNet import with_MPRNet

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
        self.move(0, 0)
        #Mesure des frames des Imgs In/Out
        self.largeur_frame = self.ui.frame_ImgIn.width()
        self.hauteur_frame = self.ui.frame_ImgIn.height()

        #Image origine
        self.ImageIn = None
        self.ImageIn_path = None

        #Chemin Images Temporaires
        #self.chemin_dossier_temp = None
        #self.chemin_dossier_temp_noisy = None

        #Configuration nom des fichiers à sauvegarder
        self.ext_bruit = None
        self.ext_filtre = None

        #Variables Booléennes
        self.ImageInIsSet = False
        self.ImageNdg = False
        self.ImageIsAlreadyNoisy = False
        self.ImageIsFiltered = False

        #Variables quantitatives
        self.noise_ecart_type = 20
        self.noise_densite = 0.01

        self.choix_filtre = 1
        self.filter_ecart_type = 20
        self.filter_radius = 1
        self.filter_taille = 3
        self.filter_diameter = 9
        self.filter_var_couleur = 75
        self.filter_var_spatiale = 75

        self.metric_PSNR = None
        self.metric_SSIM = None

        #Initialisation params
        # OUTILS BRUITS/FILTRES
        self.ui.tabWidget_cfg.setVisible(False)
        self.ui.tabWidget_cfg.setCurrentIndex(0) #Démarrage position sur onglet "gen bruit"
        self.ui.tabWidget_cfg.setTabEnabled(1, False)
        self.ui.tabWidget_cfg.setTabEnabled(2, False)

        # PSNR/SSIM/etc...
        self.ui.tabWidget_Mesure.setVisible(False)

        #Sliders GENERATEURS BRUIT
        # -- ecart_type
        self.ui.slider_ecart_type.setMinimum(1)
        self.ui.slider_ecart_type.setMaximum(100)
        self.ui.slider_ecart_type.setValue(self.noise_ecart_type)
        self.ui.slider_ecart_type.valueChanged.connect(self.update_ecart_type)
        self.ui.label_ecart_type.setText(f"Écart-type : {self.ui.slider_ecart_type.value()}")
        # -- densite
        self.ui.slider_densite.setMinimum(1)
        self.ui.slider_densite.setMaximum(10)
        self.ui.slider_diametre.setSingleStep(1)
        self.ui.slider_densite.setValue(int(self.noise_densite * 100))
        self.ui.slider_densite.valueChanged.connect(self.update_densite)
        print(self.ui.slider_densite.value())
        self.ui.label_densite.setText(f"Densité : {self.noise_densite:.2f}")

        #Sliders FILTRES

        # -- radius
        self.ui.slider_radius.setMinimum(1)
        self.ui.slider_radius.setMaximum(5)
        self.ui.slider_radius.setValue(self.filter_radius)
        self.ui.slider_radius.valueChanged.connect(self.update_radius)
        self.ui.label_radius.setText(f"Taille noyau : {self.ui.slider_radius.value()}")
        # -- taille
        self.ui.slider_taille.setMinimum(3)
        self.ui.slider_taille.setMaximum(11)
        self.ui.slider_taille.setSingleStep(2)
        self.ui.slider_taille.setPageStep(2)
        self.ui.slider_taille.setTickInterval(2)
        self.ui.slider_taille.setValue(self.filter_taille)
        self.ui.slider_taille.valueChanged.connect(self.update_taille)
        self.ui.label_taille.setText(f"Taille voisinage : { self.ui.slider_taille.value()}")
        # -- diametre
        self.ui.slider_diametre.setMinimum(5)
        self.ui.slider_diametre.setMaximum(15)
        self.ui.slider_diametre.setSingleStep(2)
        self.ui.slider_diametre.setValue(self.filter_diameter)
        self.ui.slider_diametre.valueChanged.connect(self.update_diametre)
        self.ui.label_diametre.setText(f"Diamètre voisinage : {self.ui.slider_diametre.value()}")
        # -- var_couleur
        self.ui.slider_var_couleur.setMinimum(10)
        self.ui.slider_var_couleur.setMaximum(100)
        self.ui.slider_var_couleur.setValue(self.filter_var_couleur)
        self.ui.slider_var_couleur.valueChanged.connect(self.update_var_couleur)
        self.ui.label_var_couleur.setText(f"Variance couleur : {self.ui.slider_var_couleur.value()}")
        # -- var_spatiale
        self.ui.slider_var_spatiale.setMinimum(10)
        self.ui.slider_var_spatiale.setMaximum(100)
        self.ui.slider_var_spatiale.setValue(self.filter_var_spatiale)
        self.ui.slider_var_spatiale.valueChanged.connect(self.update_var_spatiale)
        self.ui.label_var_spatiale.setText(f"Variance spatiale : {self.ui.slider_var_spatiale.value()}")

        #Visibilité filtres
        self.set_choix_filtre_var(0)

        #Lien entre les boutons UI et les fonctions
        self.ui.bouton_ouvrirImgIn.clicked.connect(self.ouvrirImage)

        #Visibilité boutons Gen Noise
        self.ui.bouton_poivresel.setVisible(False)
        self.ui.bouton_gaussien.setVisible(False)
        self.ui.bouton_chromatique.setVisible(False)
        self.set_choix_noise(0)
        #self.ui.bouton_poivresel.setEnabled(False)
        #self.ui.bouton_gaussien.setEnabled(False)
        #self.ui.bouton_chromatique.setEnabled(False)
        #self.ui.bouton_afficher.clicked.connect(lambda : self.affichageImageOut())

        #Visibilité des fenêtres
        self.ui.frame_ImgIn_background.setVisible(False)
        self.ui.frame_ImgIn.setVisible(False)
        self.ui.frame_ImgNoisy_background.setVisible(False)
        self.ui.frame_ImgNoisy.setVisible(False)
        self.ui.frame_ImgOut_background.setVisible(False)
        self.ui.frame_ImgOut.setVisible(False)

        self.ui.frame_tabWidget.setVisible(False)
        self.ui.frame_metriques.setVisible(False)



    #------------------------
    # AFFICHAGE Image bruitée
    #------------------------

    def affichageImageNoisy(self):
        if(self.ImageIsAlreadyNoisy):
            self.ui.frame_ImgIn.setVisible(False)
            self.ui.frame_ImgIn_background.setVisible(False)
        else :
            self.ui.frame_ImgIn.setVisible(True)
            self.ui.frame_ImgIn_background.setVisible(True)
        chemin_dossier_temp_noisy = tempfile.gettempdir() + "\ImgChristalTmpNoisy.jpg"
        ImgNoisy = QImage(chemin_dossier_temp_noisy)
        largeur_ImgNoisy = ImgNoisy.width()
        hauteur_ImgNoisy = ImgNoisy.height()
        if largeur_ImgNoisy > hauteur_ImgNoisy :
            ImgNoisy = ImgNoisy.scaledToWidth(self.largeur_frame, Qt.SmoothTransformation)
        else:
            ImgNoisy = ImgNoisy.scaledToHeight(self.hauteur_frame, Qt.SmoothTransformation)
        self.ui.label_ImgNoisy.setPixmap(QPixmap.fromImage(ImgNoisy))

        self.ui.frame_ImgNoisy_background.setVisible(True)
        self.ui.frame_ImgNoisy.setVisible(True)

        image = ouvrirImageIn(chemin_dossier_temp_noisy)

        #Lien entre les boutons liés à "image" et les fonctions de filtrage
        self.ui.tabWidget_cfg.setTabEnabled(1, True)
        self.ui.tabWidget_cfg.setTabEnabled(2, True)
        self.ui.radio_gaussien.toggled.connect(lambda : self.set_choix_filtre(1))
        self.ui.radio_bilateral.toggled.connect(lambda : self.set_choix_filtre(2))
        self.ui.radio_moyenneur.toggled.connect(lambda : self.set_choix_filtre(3))
        self.ui.radio_median.toggled.connect(lambda : self.set_choix_filtre(4))
        self.ui.radio_laplacien.toggled.connect(lambda : self.set_choix_filtre(5))
        self.ui.radio_laplacien.setEnabled(False)
        self.ui.radio_papier.toggled.connect(lambda : self.set_choix_filtre(6))

        self.ui.bouton_valider.clicked.connect(lambda : self.valider_filtres(image, self.choix_filtre))

        self.ui.bouton_MPRNet.clicked.connect(lambda : with_MPRNet(image.filename, self))

        self.ui.bouton_save_ImgNoisy.clicked.connect(lambda : self.sauvegardeImage(image, 1))

        self.ui.frame_ImgOut_background.setVisible(False)
        self.ui.frame_ImgOut.setVisible(False)
        self.ui.frame_metriques.setVisible(False)

    #---------------------------------
    # AFFICHAGE Image Filtrée (Sortie)
    #---------------------------------

    def affichageImageOut(self):
        print("affichage...")
        chemin_dossier_temp = tempfile.gettempdir() + "\ImgChristalTmp.jpg"
        print(chemin_dossier_temp)
        ImgOut = QImage(chemin_dossier_temp)
        #Affichage de l'image dans un label, réglage des dimensions
        largeur_ImgOut = ImgOut.width()
        hauteur_ImgOut = ImgOut.height()
        if largeur_ImgOut > hauteur_ImgOut :
            ImgOut = ImgOut.scaledToWidth(self.largeur_frame, Qt.SmoothTransformation)
        else:
            ImgOut = ImgOut.scaledToHeight(self.hauteur_frame, Qt.SmoothTransformation)
        self.ui.label_ImgOut.setPixmap(QPixmap.fromImage(ImgOut))

        self.ui.frame_ImgOut_background.setVisible(True)
        self.ui.frame_ImgOut.setVisible(True)

        image_noisy = ouvrirImageIn(chemin_dossier_temp)

        if self.ImageIsFiltered == True: #Affichage Laplacien seulement si l'image a été filtrée une première fois par un autre filtrage
            self.ui.radio_laplacien.setEnabled(True)

        #Update de la mesure de l'image de base avec l'image de fin
        self.ui.frame_metriques.setVisible(True)
        self.update_metric(self.ImageIn)
        self.ui.tabWidget_Mesure.setVisible(True)

        self.ui.bouton_save_ImgOut.clicked.connect(lambda : self.sauvegardeImage(image_noisy, 2))


    # GENERATEURS BRUIT

    def update_ecart_type(self, value):
        self.noise_ecart_type = value
        self.ui.label_ecart_type.setText(f"Écart-type : {value}")

    def update_densite(self, value):
        self.noise_densite = value / 100.0
        self.ui.label_densite.setText(f"Densité : {self.noise_densite:.2f}")

    def set_choix_noise(self, choix):
        self.ui.slider_ecart_type.setEnabled(False)
        self.ui.slider_densite.setEnabled(False)
        if choix == 1:
            self.ui.slider_ecart_type.setEnabled(True)
            self.ui.slider_densite.setEnabled(True)
        elif choix == 2:
            self.ui.slider_densite.setEnabled(True)


    # FILTRES

    def set_choix_filtre(self, choix):
        self.choix_filtre = choix
        self.set_choix_filtre_var(choix)
        self.ui.bouton_valider.click()

    def set_choix_filtre_var(self, choix):
        #print("set_choix_filtre_var called with choix =", choix)
        self.ui.slider_radius.setEnabled(False)
        self.ui.slider_diametre.setEnabled(False)
        self.ui.slider_var_couleur.setEnabled(False)
        self.ui.slider_var_spatiale.setEnabled(False)
        self.ui.slider_taille.setEnabled(False)
        if choix == 1:
            self.ui.slider_radius.setEnabled(True)
        elif choix == 2:
            self.ui.slider_diametre.setEnabled(True)
            self.ui.slider_var_couleur.setEnabled(True)
            self.ui.slider_var_spatiale.setEnabled(True)
        elif choix == 3:
            self.ui.slider_radius.setEnabled(True)
        elif choix == 4:
            self.ui.slider_taille.setEnabled(True)

    def update_radius(self, value):
        self.filter_radius = value
        self.ui.label_radius.setText(f"Taille noyau : {value}")
        self.ui.bouton_valider.click()

    def update_taille(self, value):
        self.filter_taille = value
        self.ui.label_taille.setText(f"Taille voisinage : {value}")
        self.ui.bouton_valider.click()

    def update_diametre(self, value):
        self.filter_diametre = value
        self.ui.label_diametre.setText(f"Diamètre voisinage : {value}")
        self.ui.bouton_valider.click()

    def update_var_couleur(self, value):
        self.filter_var_couleur = value
        self.ui.label_var_couleur.setText(f"Variance couleur : {value}")
        self.ui.bouton_valider.click()

    def update_var_spatiale(self, value):
        self.filter_var_spatiale = value
        self.ui.label_var_spatiale.setText(f"Variance spatiale : {value}")
        self.ui.bouton_valider.click()

    def valider_filtres(self, image, choix):
        if choix == 1:
            filtre_gaussien(image, self.filter_radius, self)
            self.ext_filtre = f"f_gaussien_{self.filter_radius}"
        elif choix == 2:
            filtre_bilateral(image.filename, self.filter_diameter, self.filter_var_couleur, self.filter_var_spatiale, self)
            self.ext_filtre = f"f_bilateral_{self.filter_diameter}_{self.filter_var_couleur}_{self.filter_var_spatiale}"
        elif choix == 3:
            filtre_moyenneur(image, self.filter_radius, self)
            self.ext_filtre = f"f_moyenneur_{self.filter_radius}"
        elif choix == 4:
            filtre_median(image, self.filter_taille, self)
            self.ext_filtre = f"f_median_{self.filter_taille}"
        elif choix == 5:
            chemin_dossier_temp_choix5 = tempfile.gettempdir() + "\ImgChristalTmp.jpg"
            imagetemp_choix5 = ouvrirImageIn(chemin_dossier_temp_choix5)
            filtre_laplacien(imagetemp_choix5, self)
            self.ext_filtre += "_f_laplacien"
        elif choix == 6:
            filtre_poissonDN(image.filename, self)
            self.ext_filtre = "f_EPDFP"

#        #Update de la mesure de l'image de base avec l'image de fin
#        self.update_metric(image)
#        self.ui.tabWidget_Mesure.setVisible(True)

    #---------
    # MESURES
    #---------

    def update_metric(self, image):
        self.metric_PSNR = calculPSNR(image)
        self.ui.label_PSNR.setText(f"{self.metric_PSNR:.2f}")
        self.metric_SSIM = calculSSIM(image)
        self.ui.label_SSIM.setText(f"{self.metric_SSIM:.2f}")

    #------------------
    # SAUVEGARDE images
    #------------------

    def sauvegardeImage(self, image, mode):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        base_name = os.path.splitext(os.path.basename(self.ImageIn_path))[0]
        if(mode == 1):
            mode_nom = "bruitée"
            setup_file_name = f"{base_name}_{self.ext_bruit}"
            #mettre chemin
            #image.open(self.chemin_dossier_tmp_noisy)
        elif(mode == 2):
            mode_nom = "débruitée"
            setup_file_name = f"{base_name}_{self.ext_bruit}_{self.ext_filtre}"

            #mettre chemin
            #image.open(self.chemin_dossier_temp)
        file_name, _ = QFileDialog.getSaveFileName(self, "Enregistrer l'image " + mode_nom, os.path.join(self.ImageIn_path, f"{setup_file_name}.jpg"), "Images (*.jpg)", options=options)

        if file_name:
            image.save(file_name)
            print(f"L'image a été enregistrée sous {file_name}")

    #---------------------
    #   OUVERTURE Image In
    #---------------------

    def ouvrirImage(self):
        options = QFileDialog.Options()
        dossierimage_path = QStandardPaths.writableLocation(QStandardPaths.PicturesLocation)
        fileName, _ = QFileDialog.getOpenFileName(self, "Sélectionner une image", dossierimage_path, "Images (*.jpg *.jpeg)", options=options)
        if fileName:
            #Affichage du chemin de l'image sur l'UI
            self.ImageIn_path = fileName
            self.ui.labeltext_chemin.setText(fileName)
            #Conversion Image en QPixmap
            ImgIn = QImage(fileName)
            #Affichage de l'image dans un label, réglage des dimensions
            largeur_ImgIn = ImgIn.width()
            hauteur_ImgIn = ImgIn.height()
            if largeur_ImgIn > hauteur_ImgIn :
                ImgIn = ImgIn.scaledToWidth(self.largeur_frame, Qt.SmoothTransformation)
            else:
                ImgIn = ImgIn.scaledToHeight(self.hauteur_frame, Qt.SmoothTransformation)
            self.ui.label_ImgIn.setPixmap(QPixmap.fromImage(ImgIn))

            self.ui.frame_ImgIn_background.setVisible(True)
            self.ui.frame_ImgIn.setVisible(True)
            self.ui.frame_ImgNoisy_background.setVisible(False)
            self.ui.frame_ImgNoisy.setVisible(False)
            self.ui.frame_ImgOut_background.setVisible(False)
            self.ui.frame_ImgOut.setVisible(False)

            #Définition de l'image en PIL
            image = ouvrirImageIn(fileName)

            self.ImageInIsSet = True
            self.ImageIn = image
            self.ImageNdg = IsNdg(image)

            #Si l'image d'origine est définie
            if(self.ImageInIsSet):
                self.ui.tabWidget_cfg.setVisible(True) #Affichage fenêtre des outils de modifications
                #Gen Noise
                if(self.ImageNdg):  #Image en niveaux de gris
                    self.ui.bouton_poivresel.setVisible(True)
                    self.ui.bouton_gaussien.setVisible(True)
                    self.set_choix_noise(1)
                else:               #Image en couleurs
                    self.ui.bouton_chromatique.setVisible(True)
                    self.ui.bouton_gaussien.setVisible(True)
                    self.ui.bouton_poivresel.setVisible(True)
                    self.set_choix_noise(1)
                #Filtres

            #Lien entre les boutons liés à "image" et les fonctions de bruitage
            self.ui.frame_tabWidget.setVisible(True)
            self.ui.bouton_poivresel.clicked.connect(lambda : bruit_poivre_et_sel(image, self.noise_densite, self))
            self.ui.bouton_gaussien.clicked.connect(lambda : bruit_gaussien(image, self.noise_ecart_type, self))
            self.ui.bouton_chromatique.clicked.connect(lambda : bruit_chromatique(image, self.noise_ecart_type, self))
            self.ui.bouton_deja_bruitee.clicked.connect(lambda : deja_bruitee(image, self))

            self.ui.frame_metriques.setVisible(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
