from PIL import Image
import random
import sys
import os
import numpy as np

# Vérification des arguments
if len(sys.argv) != 3:
    print("Utilisation : python gen_noise_gauss.py le_chemin.jpg écart_type(ex : 20)")
    sys.exit(1)

image_path = sys.argv[1]
ecart_type = float(sys.argv[2])

# Ouverture de l'image
image = Image.open(image_path).convert("L")  # Convertion de l'image en niveaux de gris si elle est en RGB

# Dimensions de l'image
largeur, hauteur = image.size

# Parcours de chaque pixel de l'image
for x in range(largeur):
    for y in range(hauteur):
        # Génération d'une valeur de bruit gaussien
        bruit = int(np.random.normal(0, ecart_type))

        # Application du bruit
        pixel = image.getpixel((x, y))
        new_pixel = max(0, min(pixel + bruit, 255)) 
        image.putpixel((x, y), new_pixel)

# Nom du fichier d'entrée sans l'extension
nom_fichier_base, extension = os.path.splitext(os.path.basename(image_path))

# Création du nouveau nom de fichier pour l'image de sortie
nom_image_sortie = "../imgoutnoised/" + nom_fichier_base + f"_bruit_gaussien_{int(ecart_type)}.jpg"

# Enregistrement de l'image modifiée
image.save(nom_image_sortie)
