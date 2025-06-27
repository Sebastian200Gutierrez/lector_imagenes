import easyocr

# Crear el lector
reader = easyocr.Reader(['es'], gpu=False)

# Ruta de la imagen que ya subiste
image_path = 'uploads/image.png'

# Leer el texto
results = reader.readtext(image_path, detail=0, paragraph=True)

# Mostrar resultados
print("Texto extraído:")
print("\n".join(results))
