# This Python file uses the following encoding: utf-8

from PIL import Image, ImageFilter, ImageChops
from imageSettings import enregistrerImageTmp, enregistrerImageTmpCV
import sys
sys.path.append("./filters")
from Papier1 import estimate_photon_density_and_gain,anscombe_transform,bilateral_filter,inverse_anscombe_transform
import random
import sys
import os
import numpy as np
import cv2

#Filtre bilatéral
def filtre_bilateral(image_path, diameter, var_color, var_space, MainWindow):
    image = cv2.imread(image_path)
    filtered_image = cv2.bilateralFilter(image, d=diameter, sigmaColor=var_color, sigmaSpace=var_space)
    enregistrerImageTmpCV(filtered_image)
    MainWindow.ImageModified = True
    print(MainWindow.ImageModified)
    MainWindow.affichageImageOut()

#Filtre gaussien
def filtre_gaussien(image, radius, MainWindow):
    filtered_image = image.filter(ImageFilter.GaussianBlur(radius=radius))
    enregistrerImageTmp(filtered_image)
    MainWindow.ImageModified = True
    print(MainWindow.ImageModified)
    MainWindow.affichageImageOut()

#Filtre moyenneur
def filtre_moyenneur(image, radius, MainWindow):
    filtered_image = image.filter(ImageFilter.BoxBlur(radius=radius))
    enregistrerImageTmp(filtered_image)
    MainWindow.ImageModified = True
    print(MainWindow.ImageModified)
    MainWindow.affichageImageOut()

#Filtre médian
def filtre_median(image, taille, MainWindow):
    filtered_image = image.filter(ImageFilter.MedianFilter(size=taille))
    enregistrerImageTmp(filtered_image)
    MainWindow.ImageModified = True
    print(MainWindow.ImageModified)
    MainWindow.affichageImageOut()


#Filtre laplacien
def filtre_laplacien(image, MainWindow):
    laplacian_filter = image.filter(ImageFilter.FIND_EDGES)
    threshold = 50
    laplacian_filter = laplacian_filter.point(lambda p: p if p > threshold else 0)
    largeur, hauteur = laplacian_filter.size
    for x in range(largeur):
        for y in range(hauteur):
            if x < 1 or x >= largeur - 1 or y < 1 or y >= hauteur - 1:
                laplacian_filter.putpixel((x, y), 0)
    laplacian_filter = laplacian_filter.filter(ImageFilter.BoxBlur(radius=1))
    filtered_image = ImageChops.add(image, laplacian_filter, scale=1.0, offset=0)
    enregistrerImageTmp(filtered_image)
    MainWindow.ImageModified = True
    print(MainWindow.ImageModified)
    MainWindow.affichageImageOut()

#
def filtre_poissonDN(image_path, MainWindow):
    image = cv2.imread(image_path)
    #blablabla
    img_array = np.array(image)
    gamma = estimate_photon_density_and_gain(img_array)
    img_array = img_array / gamma
    img_array = anscombe_transform(img_array)
    img_array = bilateral_filter(img_array,7, 0.5)
    img_array = inverse_anscombe_transform(img_array)
    img_array = img_array * gamma 
    filtered_image = np.clip(img_array, 0, 255).astype(np.uint8)
    enregistrerImageTmp(filtered_image)
    MainWindow.ImageModified = True
    print(MainWindow.ImageModified)
    MainWindow.affichageImageOut()