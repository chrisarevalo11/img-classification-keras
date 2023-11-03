from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# Initialize CORS with your Flask app
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

@app.route('/process-image', methods=['POST'])
def process_image():
    pass


if __name__ == '__main__':
    app.run()
