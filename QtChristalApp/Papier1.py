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

def estimate_photon_density_and_gain(image, window_size=11, sigma=2, theta=2):
    # Appliquer une convolution gaussienne avec une variance σ sur l'image originale
    smoothed_image = cv2.GaussianBlur(image, (0, 0), sigma)
    # Échantillonnage des régions T−(J) à partir de l'image complète
    image_height = smoothed_image.shape[0]
    image_width= smoothed_image.shape[1]
    sampled_indices = np.random.choice(image_height * image_width, size=10000, replace=True)

    sampled_coordinates = np.unravel_index(sampled_indices, (image_height, image_width))

    regions = list(zip(sampled_coordinates[0], sampled_coordinates[1]))
    if len(image.shape) == 3:
        variance_values_smoothed = [np.var(smoothed_image[region_x:region_x + window_size, region_y:region_y + window_size], axis=(0, 1)) for (region_x, region_y) in regions]

        mean_values_original = [np.mean(image[region_x:region_x + window_size, region_y:region_y + window_size], axis=(0, 1)) for (region_x, region_y) in regions]
        seuil=1
        currentVar=0
        gamma=0
        i=0
        while (currentVar<0.98 or currentVar>1.1) and i<100:
            i+=1
            image2=image
            index = 0
            nbTotal=0
            totalVariance=0
            totalMean=0
            for r,g,b in variance_values_smoothed:
                if((r+g+b)/3<=seuil):
                    totalVariance+=(r+g+b)/3
                    totalMean+=(mean_values_original[index][0] +mean_values_original[index][1]+mean_values_original[index][2])/3
                    nbTotal+=1
                index+=1
            if nbTotal !=0:
                totalMean/=nbTotal
                totalVariance/=nbTotal
                gamma = totalMean/totalVariance
                image2 = image2 / gamma 
                image2 = anscombe_transform(image2)
                currentVar=np.var(image2)
            else:
                currentVar=0
            seuil += 1
    else:
        # Estimation de la moyenne et de la variance pour chaque région
        variance_values_smoothed = [np.var(smoothed_image[region_x:region_x + window_size, region_y:region_y + window_size]) for (region_x, region_y) in regions]

        mean_values_original = [np.mean(image[region_x:region_x + window_size, region_y:region_y + window_size]) for (region_x, region_y) in regions]
        seuil=1
        currentVar=0
        gamma=0
        i=0
        while (currentVar<0.98 or currentVar>1.1) and i<100:
            i+=1
            image2=image
            index = 0
            nbTotal=0
            totalVariance=0
            totalMean=0
            for a in variance_values_smoothed:
                if(a<=seuil):
                    totalVariance+=a
                    totalMean+=mean_values_original[index]
                    nbTotal+=1
                index+=1
            if nbTotal != 0:
                totalMean/=nbTotal
                totalVariance/=nbTotal
                gamma = totalMean/totalVariance
                image2 = image2 / gamma 
                image2 = anscombe_transform(image2)
                currentVar=np.var(image2)
            else:
                currentVar=0
            seuil += 1
    return gamma

def bilateral_filter(image, sigma_spatial=2.5, sigma_intensity=0.1):
    img_array = np.array(image)

    img_array = img_array.astype(np.float32)
    if len(img_array.shape) == 3:
        img_array[...,0] = cv2.bilateralFilter(img_array[...,0], d=-1, sigmaColor=sigma_intensity, sigmaSpace=sigma_spatial)
        img_array[...,1] = cv2.bilateralFilter(img_array[...,1], d=-1, sigmaColor=sigma_intensity, sigmaSpace=sigma_spatial)
        img_array[...,2] = cv2.bilateralFilter(img_array[...,2], d=-1, sigmaColor=sigma_intensity, sigmaSpace=sigma_spatial)
    else:
        img_array = cv2.bilateralFilter(img_array, d=-1, sigmaColor=sigma_intensity, sigmaSpace=sigma_spatial)
    return img_array

def stabilize_variance_and_denoise(input_image, window_size=7, h_parameter=2.5):
    img_array = np.array(input_image)
    gamma = estimate_photon_density_and_gain(img_array)
    img_array = img_array / gamma
    img_array = anscombe_transform(img_array)
    img_array = bilateral_filter(img_array,window_size, 0.5)
    img_array = inverse_anscombe_transform(img_array)
    img_array = img_array * gamma 
    img_array = np.clip(img_array, 0, 255).astype(np.uint8)
    return img_array

