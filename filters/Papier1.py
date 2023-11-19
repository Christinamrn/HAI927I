import numpy as np
from PIL import Image, ImageFilter
import cv2

def anscombe_transform(image):
    return 2 * np.sqrt(image + 3/8)

def inverse_anscombe_transform(image):
    return (1.0/4.0 * np.power(image, 2) +
            1.0/4.0 * np.sqrt(3.0/2.0) * np.power(image, -1.0) -
            11.0/8.0 * np.power(image, -2.0) + 
            5.0/8.0 * np.sqrt(3.0/2.0) * np.power(image, -3.0) - 1.0 / 8.0)

def texture_free_areas(image, sigma=2, theta=2, window_size=11):

    # Appliquer une convolution gaussienne avec une variance σ
    smoothed_image = cv2.GaussianBlur(image, (0, 0), sigma)

    # Calculer le gradient de l'image lissée
    gradient_image = np.abs(cv2.Sobel(smoothed_image, cv2.CV_64F, 1, 0) + cv2.Sobel(smoothed_image, cv2.CV_64F, 0, 1))

    # Seuiller le gradient pour obtenir un masque binaire
    binary_mask = (gradient_image > theta).astype(np.uint8)

    # Appliquer une érosion morphologique avec une fenêtre carrée de taille ω x ω
    kernel = np.ones((window_size, window_size), np.uint8)
    texture_free_mask = cv2.erode(binary_mask, kernel)

    return texture_free_mask^1

def estimate_photon_density_and_gain(image, texture_free_mask, window_size=11, sigma=2, theta=2):
    # Appliquer une convolution gaussienne avec une variance σ sur l'image originale
    smoothed_image = cv2.GaussianBlur(image, (0, 0), sigma)

    # Échantillonnage des régions T−(J) uniquement là où le masque est actif
    non_zero_indices = np.where(texture_free_mask > 0)
    sampled_indices = np.random.choice(len(non_zero_indices[0]), size=1000, replace=True)
    
    regions = [(non_zero_indices[0][index], non_zero_indices[1][index]) for index in sampled_indices]

    # Estimation de la moyenne et de la variance pour chaque région
    variance_values_smoothed = [np.var(smoothed_image[region_x:region_x + window_size, region_y:region_y + window_size]) for (region_x, region_y) in regions]

    mean_values_original = [np.mean(image[region_x:region_x + window_size, region_y:region_y + window_size]) for (region_x, region_y) in regions]

    # Calcul du paramètre de gain gamma
    gamma = np.mean(mean_values_original) / np.mean(variance_values_smoothed)

    # Calcul de la densité de photons
    photon_density = np.sum(smoothed_image) / gamma

    return photon_density, gamma

def bilateral_filter(image, sigma_spatial=2.5, sigma_intensity=0.1):
    img_array = np.array(image)
    if len(img_array.shape) == 3:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    img_array = img_array.astype(np.uint8)

    filtered_image = cv2.bilateralFilter(img_array, d=-1, sigmaColor=sigma_intensity, sigmaSpace=sigma_spatial)

    return filtered_image

def stabilize_variance_and_denoise(input_image, texture_free_mask, window_size=7, h_parameter=2.5):
    img_array = np.array(input_image)
    if len(img_array.shape) == 3:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    photon_density, gamma = estimate_photon_density_and_gain(img_array, texture_free_mask)
    img_array = img_array / gamma 
    img_array = anscombe_transform(img_array)
    img_array = bilateral_filter(img_array,20,0.5)
    img_array = inverse_anscombe_transform(img_array)
    img_array = img_array * gamma 

    img_array = np.clip(img_array, 0, 255).astype(np.uint8)

    return Image.fromarray(img_array)

input_image_path = "imgtest/image_test.PNG"
output_image_path = "imgoutdenoised/papier1.jpg"

input_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

texture_free_mask = texture_free_areas(input_image)

output_image = stabilize_variance_and_denoise(input_image, texture_free_mask)

output_image.save(output_image_path)