from PIL import Image, ImageFilter, ImageChops, ImageOps
import sys
import os
import matplotlib.pyplot as plt

#Laplacien mais modifié

# Vérification des arguments
if len(sys.argv) != 2:
    print("Utilisation : python f_laplacien2.py le_chemin.jpg")
    sys.exit(1)

image_path = sys.argv[1]

# Ouverture de l'image
image = Image.open(image_path)

# Générer le filtre Laplacien pour accentuer les contours
laplacian_filter = image.filter(ImageFilter.FIND_EDGES)

threshold = 50
laplacian_filter = laplacian_filter.point(lambda p: p if p > threshold else 0)

largeur, hauteur = laplacian_filter.size
for x in range(largeur):
    for y in range(hauteur):
        if x < 1 or x >= largeur - 1 or y < 1 or y >= hauteur - 1:
            laplacian_filter.putpixel((x, y), 0)

laplacian_filter = laplacian_filter.filter(ImageFilter.BoxBlur(radius=1))

# Afficher l'image seuillée dans une fenêtre
plt.imshow(laplacian_filter, cmap='gray')
plt.title("Image Seuillée")
plt.axis('off')
plt.show()

# Appliquer filtre
filtered_image = ImageChops.add(image, laplacian_filter, scale=1.0, offset=0)

# Nom du fichier d'entrée sans l'extension
nom_fichier_base, extension = os.path.splitext(os.path.basename(image_path))

# Création du nouveau nom de fichier pour l'image de sortie
nom_image_sortie = "../imgoutdenoised/" + nom_fichier_base + "_laplacien2.jpg"

# Enregistrement de l'image modifiée
filtered_image.save(nom_image_sortie)
