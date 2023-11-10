# Image Classification API

This Flask-based API uses a pre-trained (created by our team) deep learning model to classify images into categories such as 'bicycle', 'van', 'car', or 'motorcycle'. 
The model is based on Convolutional Neural Network and is loaded from the 'final_model.h5' file.

## Getting Started

These instructions will guide you through setting up and running the application. You can clone it and run it locally or you can do requests to 
https://image-classifier-kdd0.onrender.com.

## API Endpoints

* GET '/' -> this endpoint is a hello world for testing
* POST '/predict' -> this endpoint receives a vehicle image encoded in base64 and classifies it into 'bicycle', 'van', 'car', or 'motorcycle'.

## To run the app locally

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

### Running the app

1. Clone the repository:

   ```bash
   git clone https://github.com/chrisarevalo11/img-classification-keras.git
   cd your-repository
   ```
2. Create a .env file with the following content: 

   ```bash
   FLASK_APP=main.py
   FLASK_RUN_HOST=0.0.0.0
   FLASK_RUN_PORT=5000
   ```
3. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```
4. Test the API:

  Now you should be able to use the app and test the previous mentioned endpoints with image data.

## Built with ❤️ and
* Flask - Web framework for Python
* TensorFlow - Open-source machine learning framework
