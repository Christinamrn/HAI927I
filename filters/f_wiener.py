import cv2
import sys
import os

# Vérification des arguments
if len(sys.argv) != 4:
    print("Utilisation : python f_wiener.py le_chemin.jpg noise_variance")
    sys.exit(1)

image_path = sys.argv[1]

# Estimation de la puissance spectrale du bruit (variance du bruit)
noise_var = float(sys.argv[2])

# Chargement de l'image en niveaux de gris
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Appliquer le filtre de Wiener
restored_image = cv2.ximgproc.createFastNonLocalDenoising(2, 7, 21)
restored_image = restored_image.compute(image, noise_var)

# Nom du fichier d'entrée sans l'extension
nom_fichier_base, extension = os.path.splitext(os.path.basename(image_path))

# Création du nouveau nom de fichier pour l'image de sortie
nom_image_sortie = "../imgoutdenoised/" + nom_fichier_base + f"_wiener_{noise_var}.jpg"

# Enregistrement de l'image restaurée
cv2.imwrite(nom_image_sortie, restored_image)
