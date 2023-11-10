import tensorflow as tf
import os

inception_net = tf.keras.models.load_model(os.path.join('models', 'final_model.h5'))

labels = ['bicycle', 'van', 'car', 'motorcycle']
def classify_image(inp):
    inp = inp.reshape((-1, 160, 160, 3))

    prediction = inception_net.predict(inp).flatten()
    index = prediction.argmax()

    return labels[index]