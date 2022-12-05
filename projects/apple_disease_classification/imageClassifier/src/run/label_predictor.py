import os
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array 
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt


def predict_label(filePath):
    img = tf.keras.utils.load_img(filePath, target_size=(100, 100))

    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence.".format(
            class_names[np.argmax(score)], 100 * np.max(score)
        )
    )

    img = image.load_img(img_path, target_size=(100,100))
    imgArray = image.img_to_array(i)/255.0
    imgArray = imgArray.reshape(1, 100,100,3)
    p = model.predict_classes()
    return "label"