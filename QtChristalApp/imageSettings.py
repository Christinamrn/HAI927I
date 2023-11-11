# This Python file uses the following encoding: utf-8

import os
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap

def display_image(self):
    # Charger l'image depuis un fichier
    image_path = os.path.join(os.path.dirname(__file__), 'chemin_vers_votre_image.jpg')

    # Vérifie si le fichier image existe
    if os.path.exists(image_path):
        pixmap = QPixmap(image_path)
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setGeometry(10, 10, 300, 200)  # Position et taille du QLabel
    else:
        print("Fichier image introuvable.")

