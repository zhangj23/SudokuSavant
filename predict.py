import numpy as np
import tensorflow as tf
from keras.preprocessing import image
from PIL import Image,ImageChops 
import cv2

def predict_image(model, x):
  x = np.expand_dims(x, axis=0)

  image_predict = model.predict(x, verbose=0)

  return np.argmax(image_predict)

def trim(im, im2=None):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        if im2 is not None:
          return im2.crop(bbox), bbox
        return im.crop(bbox)
        
def predict(filename):
    model_1 = tf.keras.models.load_model('nums.h5')
    path = filename
    img = np.array(cv2.resize(cv2.imread(path), (28, 28), interpolation=cv2.INTER_AREA))
    number_of_white_pix = np.sum(img > 150)
    number_of_black_pix = np.sum(img < 10)
    ratio = number_of_black_pix/number_of_white_pix
    if  ratio < 0.000005 and ratio < 1:
      return 0
    elif 1/ratio < 0.000005 and ratio > 1:
      return 0
    # trim(Image.open(filename)).save(filename)
    img = np.array(cv2.resize(cv2.imread(path), (28, 28), interpolation=cv2.INTER_AREA))
    return predict_image(model_1, img)

# while Truew {filename}.jpg")