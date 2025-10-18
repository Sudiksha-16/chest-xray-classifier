from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import io
from src.model import CNNModel
from src.utils import softmax

app = Flask(__name__)

# Load trained model (you can load saved weights later)
model = CNNModel()

@app.route('/')
def home():
    return jsonify({"message": "Chest X-Ray CNN API Running"})

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    image = Image.open(io.BytesIO(file.read())).convert('L')
    image = image.resize((64, 64))
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, 1, 64, 64)

    probs, _, _ = model.forward(img_array[0], label=0)
    prediction = int(np.argmax(probs))
    labels = ['NORMAL', 'PNEUMONIA']

    response = {
        "prediction": labels[prediction],
        "probabilities": probs[0].tolist()
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
