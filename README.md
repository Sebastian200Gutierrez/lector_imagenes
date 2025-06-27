# Lector de Imágenes OCR

API REST para extraer texto de imágenes usando OCR (Reconocimiento Óptico de Caracteres) con Tesseract.

## Características

- ✅ Extracción de texto de imágenes (PNG, JPG, JPEG, GIF, BMP, TIFF)
- ✅ Soporte para idioma español
- ✅ API REST simple y fácil de usar
- ✅ Despliegue en Railway
- ✅ Manejo de errores robusto

## Endpoints

### GET /
Información sobre la API y endpoints disponibles.

### GET /health
Verificar el estado de salud de la API.

### POST /upload
Subir una imagen para extraer texto.

**Parámetros:**
- `image`: Archivo de imagen (formato: PNG, JPG, JPEG, GIF, BMP, TIFF)

**Respuesta exitosa:**
```json
{
  "texto_extraido": "Texto extraído de la imagen",
  "longitud_texto": 25,
  "archivo_procesado": "imagen.png"
}
```

## Instalación Local

1. Clonar el repositorio:
```bash
git clone https://github.com/Sebastian200Gutierrez/lector_imagenes.git
cd lector_imagenes
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Instalar Tesseract OCR:
   - **Windows**: Descargar desde https://github.com/UB-Mannheim/tesseract/wiki
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

4. Ejecutar la aplicación:
```bash
python app.py
```

La API estará disponible en `http://localhost:5000`

## Despliegue en Railway

1. Conectar tu repositorio de GitHub a Railway
2. Railway detectará automáticamente que es una aplicación Python
3. La aplicación se desplegará automáticamente

## Tecnologías Utilizadas

- **Flask**: Framework web para Python
- **Tesseract OCR**: Motor de reconocimiento óptico de caracteres
- **Pillow**: Procesamiento de imágenes
- **Gunicorn**: Servidor WSGI para producción

## Autor

Sebastian Gutierrez 