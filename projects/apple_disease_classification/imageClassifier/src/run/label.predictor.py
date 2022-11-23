#!/usr/bin/env python


import '/Users/boyfrankclaesen/workspace/makeAIWork2/projects/apple_disease_classification/imageClassifier/data/batches/batch01'
import tensorflow as tf
from tensorflow import keras



modelNetV2 = keras.models.load_model('/Users/boyfrankclaesen/workspace/makeAIWork2/projects/apple_disease_classification/imageClassifier/models/mobileNetV2_256px.h5')


print(modelNetV2.predict(batch01))

