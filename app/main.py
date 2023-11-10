import cv2
import os
from flask import Flask, request, jsonify, flash
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = os.path.join('app', 'static')

# Ensure the target directory exists, or create it if it doesn't
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'secret key' 

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

@app.route('/', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        flash('No file part')
        return jsonify({'error': "media not provided"}), 400
    
    img = request.files['image']
    if img.filename == '':
        return jsonify({'error': "image not selected"}), 400
    
    if img and allowed_file(img.filename):
        filename = secure_filename(img.filename)
        
        # Use os.path.join to create the path and then replace backslashes with forward slashes
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
        return process_image(os.path.join(app.config['UPLOAD_FOLDER'], filename))

def process_image(img_path):
    print("img_path:", img_path)
    test(img_path)
    return jsonify({'message': "Image uploaded and processed"}), 200

def test(img_path):
    image = cv2.imread(img_path)
    print("image:", image)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run()



# try:
    #     image = cv2.imread(img_path)
    #     print("image:", image)

    #     prediction = classify_image(image)

    #     return jsonify({'prediction': prediction}), 200
    # except Exception as e:
    #     error_message = str(e)  
    #     app.logger.error(f"An error occurred: {error_message}")
    #     return jsonify({'error': "invalid image"}), 400