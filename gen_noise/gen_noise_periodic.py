from PIL import Image
import sys
import os
import numpy as np

# Vérification des arguments
if len(sys.argv) != 4:
    print("Utilisation : python gen_periodic.py le_chemin.jpg largeur_bande(ex: 50) période(ex: 100)")
    sys.exit(1)

image_path = sys.argv[1]
band_width = int(sys.argv[2])
period = int(sys.argv[3])

# Ouverture de l'image
image = Image.open(image_path)

# Dimensions de l'image
largeur, hauteur = image.size

# Parcours de chaque pixel de l'image
for x in range(largeur):
    for y in range(hauteur):
        # Calcul de la valeur de la sinusoïde pour RGB
        phase = x / period  # Utilisation de la coordonnée x comme phase
        amplitude = band_width  # Amplitude du bruit

        bruit_r = int(amplitude * np.sin(2 * np.pi * phase))
        bruit_g = int(amplitude * np.sin(2 * np.pi * phase))
        bruit_b = int(amplitude * np.sin(2 * np.pi * phase))

        # Application du bruit à chaque canal de couleur
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
nom_image_sortie = "../imgoutnoised/" + nom_fichier_base + "_bruit_periodique.jpg"

# Enregistrement de l'image modifiée
image.save(nom_image_sortie)
