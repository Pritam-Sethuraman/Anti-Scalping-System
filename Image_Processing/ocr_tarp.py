# -*- coding: utf-8 -*-
"""OCR_TARP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XRbzpi2vUENhSVMGpv9oVfm3vZ00-v7o
"""

!sudo apt install tesseract-ocr
!pip install pytesseract

import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import Image
import numpy as np
import cv2
from google.colab.patches import cv2_imshow

filename = 'TARP1.jfif'
img1 = np.array(Image.open(filename))
cv2_imshow(img1)
text = pytesseract.image_to_string(img1)
print(text)

filename = 'TARP2.jfif'
img1 = np.array(Image.open(filename))
cv2_imshow(img1)
text = pytesseract.image_to_string(img1)
print(text)

filename = 'TARP3.jfif'
img1 = np.array(Image.open(filename))
cv2_imshow(img1)
text = pytesseract.image_to_string(img1)
print(text)

