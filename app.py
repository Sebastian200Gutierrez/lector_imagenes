from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return "API OCR funcionando correctamente."

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No se encontró el archivo con clave "image"'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'Nombre de archivo vacío'}), 400

    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    # Procesar imagen con OCR
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang='spa')  # usa español
        return jsonify({'texto_extraido': text.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
