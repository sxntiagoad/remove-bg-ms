from flask import Blueprint, request, jsonify
from app.services.bg_remove import remove_background

bgRemove_bp = Blueprint('bgRemove', __name__)

@bgRemove_bp.route('/remove-bg', methods=['POST'])
def remove_bg():
    data = request.json
    image_base64 = data.get('image')
    if not image_base64:
        return jsonify({'error': 'No se ha proporcionado una imagen'}), 400
    
    result = remove_background(image_base64)
    return jsonify({'result': result}), 200 