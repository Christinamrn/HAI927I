from PIL import Image
import sys
import numpy as np

def calculPSNR(img1_path, img2_path):
    # Chargement des images
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # Conversion des images en tableaux NumPy
    image_arr = np.array(img1).astype(np.float64)
    imageout_arr = np.array(img2).astype(np.float64)

    if img1.mode == "L" :

        mse = np.mean((image_arr - imageout_arr) ** 2)

        max_pixel = 255.0
        PSNR = 10 * np.log10((max_pixel ** 2) / mse)
        return PSNR

    else :
        mse_r = np.mean((image_arr[:, :, 0] - imageout_arr[:, :, 0]) ** 2)
        mse_g = np.mean((image_arr[:, :, 1] - imageout_arr[:, :, 1]) ** 2)
        mse_b = np.mean((image_arr[:, :, 2] - imageout_arr[:, :, 2]) ** 2)

        mse = (mse_r + mse_g + mse_b) / 3.0

        max_pixel = 255.0
        psnr_val = 10 * np.log10((max_pixel ** 2) / mse)

        return psnr_val

if len(sys.argv) != 3:
    print("Utilisation : python PSNR.py chemin_img_originale.jpg chemin_img_modifiee.jpg")
    sys.exit(1)

image1_path = sys.argv[1]
image2_path = sys.argv[2]

# Calcul du PSNR
psnr_value = calculPSNR(image1_path, image2_path)
print(f"PSNR entre les images : {psnr_value} dB")