from PIL import Image, ImageFilter
import sys
import os
import cv2

# Vérification des arguments
if len(sys.argv) != 2:
    print("Utilisation : python f_median.py le_chemin.jpg")
    sys.exit(1)

image_path = sys.argv[1]
#taille_noyau = int(sys.argv[2]) --> 3 ok, 9 c'était trop

# Ouverture de l'image
image = Image.open(image_path) 

filtered_image = image.filter(ImageFilter.MedianFilter(size=3))

# Nom du fichier d'entrée sans l'extension
nom_fichier_base, extension = os.path.splitext(os.path.basename(image_path))

# Création du nouveau nom de fichier pour l'image de sortie
nom_image_sortie = "../imgoutdenoised/" + nom_fichier_base + "_f_median.jpg"

# Enregistrement de l'image modifiée
filtered_image.save(nom_image_sortie)
