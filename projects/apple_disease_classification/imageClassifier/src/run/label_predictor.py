#!/usr/bin/env python

import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array 
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

mobileNetV2 = load_model('../models/mobileNetV2_256px.h5')
 #OSError: No file or directory found at ../models/mobileNetV2_256px.h5 Bij het uitvoeren in terminal.. 

dirBatch01 = '../data/batches/batch01/'
dirBatch02 = '../data/batches/batch02/'
dirBatch03 = '../data/batches/batch03/'

batches = [dirBatch01, dirBatch02, dirBatch03]

txtFiles = list()
foto_path = list()

predBatches=[[],[],[]]

tel=0

for i in batches:
  txtFile = os.path.join(i)
  txtFiles.append(txtFile) 
  foto_path.append(os.listdir(i))

  for filename in os.listdir(i):
    txtFile = os.path.join(i, filename)
    x = img_to_array(Image.open(txtFile)).astype('uint8')
    y = np.stack([x], axis=0)
    print(x)
    
    predictions=mobileNetV2.predict([y])
    appletypenr = np.argmax(predictions)
    predBatches[tel].append(appletypenr)
  tel+=1
  
print(predBatches)


predBatch01 = (predBatches[0])
predBatch02 = (predBatches[1])
predBatch03 = (predBatches[2])