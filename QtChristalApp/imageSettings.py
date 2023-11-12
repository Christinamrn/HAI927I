# This Python file uses the following encoding: utf-8

from PIL import Image
import random
import sys
import os
import numpy as np
import tempfile

def ouvrirImageIn(imagein_path):
    return Image.open(imagein_path)

def enregistrerImageOut(image, imageout_path):
    image.save(imageout_path)

def enregistrerImageTmp (image):
    chemin_dossier_temp = tempfile.gettempdir() + "\ImgChristalTmp.jpg"
    print(chemin_dossier_temp)
    image.save(chemin_dossier_temp)

def conversion_ndg(image):
    image.convert("L")

def IsNdg(image):
    if image.mode == "L":
        return True
    else:
        return False
