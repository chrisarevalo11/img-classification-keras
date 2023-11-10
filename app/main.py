import io
import base64
import numpy as np
from flask import Flask, request, jsonify
from PIL import Image
from flask_cors import CORS
from model import classify_image

app = Flask(__name__)
CORS(app) 
app.secret_key = 'secret key' 

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

@app.route('/predict', methods=['POST'])
def upload_image():
        
    try:
        req = request.get_json(force=True)

        image = decode_request(req)
        batch = preprocess(image)

        prediction = classify_image(batch)

        return jsonify({'prediction': prediction}), 200
    except:
        return jsonify({'prediction': 'error'}), 400

def decode_request(req):
    encoded = req["image"]
    decoded = base64.b64decode(encoded)
    return decoded

def preprocess(decoded):
    pil_image = Image.open(io.BytesIO(decoded)).resize((160,160)).convert("RGB") 

    image = np.asarray(pil_image)
    batch = np.expand_dims(image, axis=0)
    
    return batch

if __name__ == '__main__':
    app.run()
