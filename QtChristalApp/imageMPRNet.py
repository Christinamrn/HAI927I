import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms.functional as TF
from PIL import Image
import os
from runpy import run_path
from skimage import img_as_ubyte
from collections import OrderedDict
from natsort import natsorted
from glob import glob
import cv2
import tempfile

def save_img(filepath, img):
    cv2.imwrite(filepath,cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

def load_checkpoint(model, weights):
    checkpoint = torch.load(weights)
    try:
        model.load_state_dict(checkpoint["state_dict"])
    except:
        state_dict = checkpoint["state_dict"]
        new_state_dict = OrderedDict()
        for k, v in state_dict.items():
            name = k[7:] # remove `module.`
            new_state_dict[name] = v
        model.load_state_dict(new_state_dict)


# Load corresponding model architecture and weights
MPR_path = "MPRNet.py"
load_file = run_path(MPR_path)
model = load_file['MPRNet']()
model.cuda()

weights = "model_denoising.pth"
load_checkpoint(model, weights)
model.eval()

img_multiple_of = 8

def with_MPRNet(image_path, MainWindow):
    img = Image.open(image_path).convert('RGB')
    input_ = TF.to_tensor(img).unsqueeze(0).cuda()

    # Pad the input if not_multiple_of 8
    h,w = input_.shape[2], input_.shape[3]
    H,W = ((h+img_multiple_of)//img_multiple_of)*img_multiple_of, ((w+img_multiple_of)//img_multiple_of)*img_multiple_of
    padh = H-h if h%img_multiple_of!=0 else 0
    padw = W-w if w%img_multiple_of!=0 else 0
    input_ = F.pad(input_, (0,padw,0,padh), 'reflect')

    with torch.no_grad():
        restored = model(input_)
    restored = restored[0]
    restored = torch.clamp(restored, 0, 1)

    # Unpad the output
    restored = restored[:,:,:h,:w]

    restored = restored.permute(0, 2, 3, 1).cpu().detach().numpy()
    restored = img_as_ubyte(restored[0])

    #f = os.path.splitext(os.path.split(file_)[-1])[0]
    #save_img((os.path.join(out_dir, f+'.png')), restored)
    chemin_dossier_temp = tempfile.gettempdir() + "\ImgChristalTmp.jpg"
    save_img(chemin_dossier_temp, restored)
    MainWindow.affichageImageOut()

