from rembg import remove
from PIL import Image
import io
import base64

def remove_background(base64_image):
    # Decodificar la imagen de Base64
    image_data = base64.b64decode(base64_image)
    
    # Convertir los datos de la imagen a un objeto de imagen
    input_image = Image.open(io.BytesIO(image_data))
    
    # Eliminar el fondo
    output_image = remove(input_image)
    
    # Guardar la imagen resultante en un objeto BytesIO
    output_bytes = io.BytesIO()
    output_image.save(output_bytes, format='PNG')
    
    # Obtener la imagen en formato Base64
    output_bytes.seek(0)
    output_base64 = base64.b64encode(output_bytes.read()).decode('utf-8')
    
    return output_base64