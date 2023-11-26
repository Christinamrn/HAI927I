# This Python file uses the following encoding: utf-8

from PIL import Image
from imageSettings import enregistrerImageTmp, enregistrerImageTmpNoisy
import random
import sys
import os
import numpy as np
import copy

#A la fin de chaque bruitage, on modifie la valeur de ImageIsNoisy pour dire qu'elle a été bruitée

# Bruit chromatique
def bruit_chromatique(image, ecart_type, MainWindow):
    image = copy.deepcopy(image)
    largeur, hauteur = image.size

    for x in range(largeur):
        for y in range(hauteur):
            bruit_r = int(np.random.normal(0, ecart_type))
            bruit_g = int(np.random.normal(0, ecart_type))
            bruit_b = int(np.random.normal(0, ecart_type))
            pixel = image.getpixel((x,y))
            r, g, b = pixel
            new_r = max(0, min(r + bruit_r, 255))
            new_g = max(0, min(g + bruit_g, 255))
            new_b = max(0, min(b + bruit_b, 255))
            new_pixel = (new_r, new_g, new_b)

            image.putpixel((x, y), new_pixel)
    enregistrerImageTmpNoisy(image)
    MainWindow.affichageImageNoisy()


#Bruit gaussien
def bruit_gaussien(image, ecart_type, MainWindow):
    image = copy.deepcopy(image)
    largeur, hauteur = image.size

    if(image.mode == "L"):
        for x in range(largeur):
            for y in range(hauteur):
                bruit = int(np.random.normal(0, ecart_type))
                pixel = image.getpixel((x, y))
                new_pixel = max(0, min(pixel + bruit, 255))
                image.putpixel((x, y), new_pixel)
    else:
        for x in range(largeur):
            for y in range(hauteur):
                bruit = int(np.random.normal(0, ecart_type))
                pixel = image.getpixel((x, y))
                r, g, b = pixel
                new_r = max(0, min(r + bruit, 255))
                new_g = max(0, min(g + bruit, 255))
                new_b = max(0, min(b + bruit, 255))
                new_pixel = (new_r, new_g, new_b)
                image.putpixel((x, y), new_pixel)
    enregistrerImageTmpNoisy(image)
    MainWindow.affichageImageNoisy()


#Bruit poivre et sel
def bruit_poivre_et_sel(image, densite, MainWindow):
    image = copy.deepcopy(image)
    largeur, hauteur = image.size
    pixels = image.load()

    if(image.mode == "L"):
        for x in range(largeur):
            for y in range(hauteur):
                if random.random() < densite:
                    bruit = random.randint(0, 255)
                    new_pixel = min(bruit, 255)
                    image.putpixel((x, y), new_pixel)
    else:
        for x in range(largeur):
            for y in range(hauteur):
                if random.random() < densite:
                    bruit = random.randint(0, 255)
                    new_pixel = (min(bruit, 255), min(bruit, 255), min(bruit, 255))
                    pixels[x,y] = new_pixel
                    #image.putpixel((x, y), new_pixel)
    enregistrerImageTmpNoisy(image)
    MainWindow.affichageImageNoisy()

#Déjà bruitée
def deja_bruitee(image, MainWindow):
    enregistrerImageTmpNoisy(image)
    MainWindow.ImageIsAlreadyNoisy = True
    MainWindow.affichageImageNoisy()
