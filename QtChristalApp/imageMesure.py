# This Python file uses the following encoding: utf-8

from PIL import Image
import numpy as np
import tempfile
import cv2
import math
from skimage.metrics import structural_similarity as ssim
from skimage import img_as_float
from skimage.transform import resize
from imageSettings import IsNdg
from brisque import BRISQUE


def calculPSNR(image):
    chemin_dossier_temp = tempfile.gettempdir() + "\ImgChristalTmp.jpg"
    imageout = Image.open(chemin_dossier_temp)

    image_arr = np.array(image).astype(np.float64)
    imageout_arr = np.array(imageout).astype(np.float64)

    if IsNdg(image) == True:

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

def calculSSIM(image):
    chemin_dossier_temp = tempfile.gettempdir() + "\ImgChristalTmp.jpg"
    imageout = Image.open(chemin_dossier_temp)

    image = np.array(image).astype(np.float64)
    imageout = np.array(imageout).astype(np.float64)

#    # Convertir les images en valeurs de type float32
#    image = image.astype(np.float32)
#    imageout = imageout.astype(np.float32)

    c1 = (0.01 * 255) ** 2
    c2 = (0.03 * 255) ** 2

    mean1 = cv2.GaussianBlur(image, (11, 11), 1.5)
    mean2 = cv2.GaussianBlur(imageout, (11, 11), 1.5)

    mean1_sq = mean1 ** 2
    mean2_sq = mean2 ** 2

    mean12 = mean1 * mean2

    var1 = cv2.GaussianBlur(image ** 2, (11, 11), 1.5) - mean1_sq
    var2 = cv2.GaussianBlur(imageout ** 2, (11, 11), 1.5) - mean2_sq

    covar12 = cv2.GaussianBlur(image * imageout, (11, 11), 1.5) - mean12

    ssim_index = ((2 * mean12 + c1) * (2 * covar12 + c2)) / ((mean1_sq + mean2_sq + c1) * (var1 + var2 + c2))

    return np.mean(ssim_index)

def calculBRISQUE():
    chemin_dossier_temp = tempfile.gettempdir() + "\ImgChristalTmp.jpg"
    image = Image.open(chemin_dossier_temp)
    image = np.array(image).astype(np.float64)
    obj = BRISQUE(url=False)
    return obj.score(image)

def calculRMSE(image):
    chemin_dossier_temp = tempfile.gettempdir() + "\ImgChristalTmp.jpg"
    imageout = Image.open(chemin_dossier_temp)
    image_arr = np.array(image).astype(np.float64)
    imageout_arr = np.array(imageout).astype(np.float64)

    if IsNdg(image) == True:

        mse = np.mean((image_arr - imageout_arr) ** 2)
        RMSE = math.sqrt(mse)
        return RMSE

    else :
        mse_r = np.mean((image_arr[:, :, 0] - imageout_arr[:, :, 0]) ** 2)
        mse_g = np.mean((image_arr[:, :, 1] - imageout_arr[:, :, 1]) ** 2)
        mse_b = np.mean((image_arr[:, :, 2] - imageout_arr[:, :, 2]) ** 2)

        mse = (mse_r + mse_g + mse_b) / 3.0

        RMSE = math.sqrt(mse)
        return RMSE

def calculSNR(image):
    chemin_dossier_temp = tempfile.gettempdir() + "\ImgChristalTmp.jpg"
    imageout = Image.open(chemin_dossier_temp)
    image_arr = np.asarray(image)
    imageout_arr = np.asarray(imageout)

    image = image_arr.astype(np.float64)
    imageout = imageout_arr.astype(np.float64)

    signal_power_per_channel = np.sum(image**2, axis=(0, 1))

    noise = image - imageout
    noise_power_per_channel = np.sum(noise**2, axis=(0, 1))

    noise_power_per_channel[noise_power_per_channel < 1e-10] = 1e-10

    snr_per_channel = 10 * np.log10(signal_power_per_channel / noise_power_per_channel)

    average_snr = np.mean(snr_per_channel)

    return average_snr
