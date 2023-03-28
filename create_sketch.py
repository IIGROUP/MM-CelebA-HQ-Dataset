#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   create_sketch.py
@Time    :   2023/03/28 10:10:16
@Author  :   Weihao Xia (xiawh3@outlook.com)
@Version :   1.0
@Desc    :   This script is used to generate sketches.
             please ensure torch==0.4.1 and torchvision==0.2.1
'''

import os
import cv2
import numpy as np
import argparse

import hashlib
import platform
import subprocess
# import urllib.request

from torchvision import transforms
from torchvision.utils import save_image
from torch.utils.serialization import load_lua

def sobel(img):
    opImgx = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)
    opImgy = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
    return cv2.bitwise_or(opImgx, opImgy)

def sketch(frame):
    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    invImg = 255 - frame
    edgImg0 = sobel(frame)
    edgImg1 = sobel(invImg)
    edgImg = cv2.addWeighted(edgImg0, 0.75, edgImg1, 0.75, 0)
    opImg = 255 - edgImg
    return opImg

def get_sketch_image(image_path):
    original = cv2.imread(image_path)
    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    sketch_image = sketch(original)
    return sketch_image[:, :, np.newaxis]

def download_model(modelname, filename, fileurl, filemd5):
    '''
    download the sketch simplification model (sketch_gan.t7) from official implementation: 
    https://github.com/bobbens/sketch_simplification
    '''
    # check if the model already exists
    if os.path.isfile(filename):
        print (filename)
        print(f"Model '{modelname}' already exists. Skipping download.")
    else:
        #  call wget command to download the file 
        print(f"Downloading the sketch simplification {modelname} model...")
        # urllib.request.urlretrieve(fileurl, filename)
        subprocess.call(["wget", "-q", "--show-progress", "--continue", "-O", filename, "--", fileurl])

        # verify the MD5 checksum
        print("checking integrity (md5sum)...")
        with open(filename, "rb") as f:
            md5 = hashlib.md5(f.read()).hexdigest()
        if md5 != filemd5:
            print("Integrity check failed. File is corrupt!")
            print(f"Try running this script again and if it fails remove '{filename}' before trying again.")
            os.remove(filename)
            raise ValueError("MD5 checksum does not match")
           
        print(f"Model '{modelname}' downloaded successfully")

if __name__ == "__main__":

    # define a dictionary to store the model information
    models = {
        "GAN": {
            "filename": "model_gan.t7",
            "fileurl": "https://esslab.jp/~ess/data/sketch_gan.t7",
            "filemd5": "3a5b4088f2490ca4b8140a374e80c878"
        },
        "MSE": {
            "filename": "model_mse.t7",
            "fileurl": "https://esslab.jp/~ess/data/sketch_mse.t7",
            "filemd5": "12317df9a0a2a7220629f5f361b45b82"
        },
        "PENCIL(1)": {
            "filename": "model_pencil1.t7",
            "fileurl": "https://esslab.jp/~ess/data/pencil_artist1.t7",
            "filemd5": "33d553ff3a50d6522e79a73002b0025c"
        },
        "PENCIL(2)": {
            "filename": "model_pencil2.t7",
            "fileurl": "https://esslab.jp/~ess/data/pencil_artist2.t7",
            "filemd5": "537b3ad9d46b2a82b65883be747a7ba9"
        }
    }

    # parse command-line arguments
    parser = argparse.ArgumentParser(description="sketch data generation")
    parser.add_argument("modelname", type=str, choices=models.keys(), help="name of the model to download")
    parser.add_argument("use_cuda", type=bool, default=True, help="use cuda or not")
    parser.add_argument("data_path", type=str, default="celeba_image", help="path to read images")
    parser.add_argument("save_path", type=str, default="celeba_sketch", help="path to save sketches")
    args = parser.parse_args()

    # download the specified model
    print("downloading pretrained models...")
    model = models[args.modelname]
    download_model(args.modelname, model["filename"], model["fileurl"], model["filemd5"])
    print("download finished!")

    # load the model
    cache = load_lua(args.modelname) # sketch_gan.t7
    model = cache.model
    immean = cache.mean
    imstd = cache.std
    model.evaluate()

    if not os.path.exists(args.save_path):
        os.makedirs(args.save_path)

    images = [os.path.join(args.data_path, f) for f in os.listdir(args.data_path)]

    for idx, image_path in enumerate(images):
        if idx % 50 == 0:
            print("{} out of {}".format(idx, len(images)))
        data = get_sketch_image(image_path)
        data = ((transforms.ToTensor()(data) - immean) / imstd).unsqueeze(0)
        if args.use_cuda:
            pred = model.cuda().forward(data.cuda()).float()
        else:
            pred = model.forward(data)
        save_image(pred[0], os.path.join(args.save_path, "{}_edges.jpg".format(image_path.split("/")[-1].split('.')[0])))