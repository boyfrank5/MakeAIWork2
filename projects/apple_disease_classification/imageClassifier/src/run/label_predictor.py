#!/usr/bin/env python

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator




batches = "../../data/batches"
mobileNetV2 = load_model('/Users/boyfrankclaesen/workspace/makeAIWork2/projects/apple_disease_classification/imageClassifier/models/mobileNetV2_256px.h5')



# activation=mobileNetV2.predict(batch01)

# predictions=(np.argmax(activation, axis = -1)) 
                        
# predictions = mobileNetV2.predict(batch01)

# labelsBatch01 = list(predictions) # casting np.array naar 'list'

# print(labelsBatch01)
