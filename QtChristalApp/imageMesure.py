# This Python file uses the following encoding: utf-8

from PIL import Image
import numpy as np
import tempfile
from skimage.metrics import structural_similarity as ssim

def calculPSNR(image):
    chemin_dossier_temp = tempfile.gettempdir() + "\ImgChristalTmp.jpg"
    imageout = Image.open(chemin_dossier_temp)

    #Conversion des images en tableaux NumPy
    image_arr = np.array(image).astype(np.float64)
    imageout_arr = np.array(imageout).astype(np.float64)

    #Calcul de la différence quadratique
    mse = np.mean((image_arr - imageout_arr) ** 2)

    #Calcul PSNR
    max_pixel = 255.0
    PSNR = 20 * np.log10(max_pixel / np.sqrt(mse))
    return PSNR

def calculSSIM(image):
    chemin_dossier_temp = tempfile.gettempdir() + "\ImgChristalTmp.jpg"
    imageout = Image.open(chemin_dossier_temp)

    # Conversion des images en tableaux NumPy
    image_arr = np.array(image)
    imageout_arr = np.array(imageout)

    # Calcul SSIM
    ssim_value, _ = ssim(image_arr, imageout_arr, full=True)
    return ssim_value

