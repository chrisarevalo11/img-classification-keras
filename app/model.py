import tensorflow as tf
import cv2
import os

inception_net = tf.keras.models.load_model(os.path.join('app\models', 'final_model.h5'))

labels = ['bicicleta', 'camioneta', 'carro', 'moto']
def classify_image(inp):
    inp = cv2.resize(inp, (160, 160))
    inp = inp.reshape((-1, 160, 160, 3))

    prediction = inception_net.predict(inp).flatten()
    index = prediction.argmax()

    return labels[index]