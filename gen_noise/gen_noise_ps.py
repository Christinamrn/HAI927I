from PIL import Image
import random
import sys
import os

# Vérification des arguments
if len(sys.argv) != 3:
    print("Utilisation : python gen_noise_ps.py le_chemin.jpg densité(ex: 0.05)")
    sys.exit(1)

image_path = sys.argv[1]
densite = float(sys.argv[2])

# Ouverture de l'image
image = Image.open(image_path).convert("L")  # Convertion de l'image en niveaux de gris si elle est en RGB

# Dimensions de l'image
largeur, hauteur = image.size

# Valeur maximale du bruit
valeur_max_bruit = 255

# Parcours de chaque pixel de l'image
for x in range(largeur):
    for y in range(hauteur):
        if random.random() < densite:
            # Génération d'une valeur aléatoire pour le bruit
            bruit = random.randint(0, valeur_max_bruit)

            # Application du bruit
            pixel = image.getpixel((x, y))
            new_pixel = min(bruit, 255)
            image.putpixel((x, y), new_pixel)

# Nom du fichier d'entrée sans l'extension
nom_fichier_base, extension = os.path.splitext(os.path.basename(image_path))

# Densite sans virgule
str_densite = str(densite).replace(".", "")

# Création du nouveau nom de fichier pour l'image de sortie
nom_image_sortie = "../imgoutnoised/" + nom_fichier_base + f"_poivre_et_sel_{str_densite}.jpg"

# Enregistrement de l'image modifiée
image.save(nom_image_sortie)
