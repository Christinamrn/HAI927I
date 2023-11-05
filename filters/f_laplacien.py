from PIL import Image, ImageFilter, ImageChops
import sys
import os

# Vérification des arguments
if len(sys.argv) != 2:
    print("Utilisation : python f_laplacien.py le_chemin.jpg")
    sys.exit(1)

image_path = sys.argv[1]

# Ouverture de l'image
image = Image.open(image_path)

# Générer le filtre Laplacien pour accentuer les contours
laplacian_filter = image.filter(ImageFilter.FIND_EDGES)

# Appliquer filtre
filtered_image = ImageChops.add(image, laplacian_filter, scale=1.0, offset=0)

# Nom du fichier d'entrée sans l'extension
nom_fichier_base, extension = os.path.splitext(os.path.basename(image_path))

# Création du nouveau nom de fichier pour l'image de sortie
nom_image_sortie = "../imgoutdenoised/" + nom_fichier_base + "_laplacien.jpg"

# Enregistrement de l'image modifiée
filtered_image.save(nom_image_sortie)
