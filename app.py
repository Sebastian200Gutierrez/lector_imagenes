from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import os
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configurar Tesseract para Railway (si es necesario)
try:
    # En Railway, Tesseract puede estar en una ubicación diferente
    if os.environ.get('RAILWAY_ENVIRONMENT'):
        # Configuración específica para Railway
        pass
except Exception as e:
    logger.warning(f"No se pudo configurar Tesseract específicamente: {e}")

@app.route('/')
def home():
    return jsonify({
        "mensaje": "API OCR funcionando correctamente",
        "endpoints": {
            "upload": "/upload (POST) - Subir imagen para extraer texto"
        }
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No se encontró el archivo con clave "image"'}), 400

        image = request.files['image']
        if image.filename == '':
            return jsonify({'error': 'Nombre de archivo vacío'}), 400

        # Validar tipo de archivo
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'}
        if not image.filename.lower().endswith(tuple('.' + ext for ext in allowed_extensions)):
            return jsonify({'error': 'Tipo de archivo no permitido. Use: PNG, JPG, JPEG, GIF, BMP, TIFF'}), 400

        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(image_path)

        # Procesar imagen con OCR
        try:
            img = Image.open(image_path)
            text = pytesseract.image_to_string(img, lang='spa')  # usa español
            
            # Limpiar archivo después de procesar
            if os.path.exists(image_path):
                os.remove(image_path)
            
            return jsonify({
                'texto_extraido': text.strip(),
                'longitud_texto': len(text.strip()),
                'archivo_procesado': image.filename
            })
            
        except Exception as e:
            logger.error(f"Error en OCR: {e}")
            # Limpiar archivo en caso de error
            if os.path.exists(image_path):
                os.remove(image_path)
            return jsonify({'error': f'Error al procesar la imagen: {str(e)}'}), 500
            
    except Exception as e:
        logger.error(f"Error general: {e}")
        return jsonify({'error': f'Error interno del servidor: {str(e)}'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
