from PIL import Image, ImageFilter
import sys
import os
import cv2

# Vérification des arguments
if len(sys.argv) != 5:
    print("Utilisation : python f_bilateral.py le_chemin.jpg diamètre var_couleurs var_spatiales")
    sys.exit(1)

image_path = sys.argv[1]

# Paramètres du filtre bilatéral (valeurs typiques)
diameter = int(sys.argv[2]) #9
sigma_color = int(sys.argv[3]) #75
sigma_space = int(sys.argv[4]) #75

# Ouverture de l'image
image = cv2.imread(image_path)

# Appliquer le filtre bilatéral
filtered_image = cv2.bilateralFilter(image, d=diameter, sigmaColor=sigma_color, sigmaSpace=sigma_space)

# Nom du fichier d'entrée sans l'extension
nom_fichier_base, extension = os.path.splitext(os.path.basename(image_path))

# Création du nouveau nom de fichier pour l'image de sortie
nom_image_sortie = "../imgoutdenoised/" + nom_fichier_base + f"_bilateral_{diameter}_{sigma_color}_{sigma_space}.jpg"

# Enregistrement de l'image modifiée
cv2.imwrite(nom_image_sortie, filtered_image)
