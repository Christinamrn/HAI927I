from PIL import Image
import numpy as np

def calculPSNR(img1_path, img2_path):
    # Chargement des images
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # Conversion des images en tableaux NumPy
    img1_arr = np.array(img1).astype(np.float64)
    img2_arr = np.array(img2).astype(np.float64)

    # Calcul de la différence quadratique
    mse = np.mean((img1_arr - img2_arr) ** 2)

    # Calcul du PSNR
    max_pixel = 255.0
    PSNR = 20 * np.log10(max_pixel / np.sqrt(mse))
    return PSNR

if len(sys.argv) != 3:
    print("Utilisation : python gen_noise_chroma.py chemin_img_originale.jpg chemin_img_modifiee.jpg")
    sys.exit(1)

image1_path = sys.argv[1]
image2_path = sys.argv[2]

# Calcul du PSNR
psnr_value = calculate_psnr(image1_path, image2_path)
print(f"PSNR entre les images : {psnr_value} dB")