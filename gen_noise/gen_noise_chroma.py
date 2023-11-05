from PIL import Image
import random
import sys
import os
import numpy as np

# Vérification des arguments
if len(sys.argv) != 3:
    print("Utilisation : python gen_noise_chroma.py le_chemin.jpg écart_type(ex: 20)")
    sys.exit(1)

image_path = sys.argv[1]
ecart_type = float(sys.argv[2])

# Ouverture de l'image
image = Image.open(image_path)

# Dimensions de l'image
largeur, hauteur = image.size

# Parcours de chaque pixel de l'image
for x in range(largeur):
    for y in range(hauteur):
        # Génération de valeurs de bruit gaussien pour RGB
        bruit_r = int(np.random.normal(0, ecart_type))
        bruit_g = int(np.random.normal(0, ecart_type))
        bruit_b = int(np.random.normal(0, ecart_type))

        # Application du bruit
        pixel = image.getpixel((x, y))
        r, g, b = pixel
        new_r = max(0, min(r + bruit_r, 255))
        new_g = max(0, min(g + bruit_g, 255))
        new_b = max(0, min(b + bruit_b, 255))
        new_pixel = (new_r, new_g, new_b)

        image.putpixel((x, y), new_pixel)

# Nom du fichier d'entrée sans l'extension
nom_fichier_base, extension = os.path.splitext(os.path.basename(image_path))

# Création du nouveau nom de fichier pour l'image de sortie
nom_image_sortie = "../imgoutnoised/" + nom_fichier_base + f"_bruit_chromatique_{int(ecart_type)}.jpg"

# Enregistrement de l'image modifiée
image.save(nom_image_sortie)
