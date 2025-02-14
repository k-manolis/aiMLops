from flask import request, jsonify
import os
from models import insert_model, get_all_models, get_model_by_name
from config import MODEL_STORAGE_DIR, ALLOWED_EXTENSIONS

# Ensure the model storage directory exists
os.makedirs(MODEL_STORAGE_DIR, exist_ok=True)

def allowed_file(filename):
    """Check if the file has a valid extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_model():
    """Handle uploading a model with metadata."""
    file = request.files.get('file')
    if not file or file.filename == '':
        return jsonify({'message': 'No file provided'}), 400

    if not allowed_file(file.filename):
        return jsonify({'message': 'Invalid file type'}), 400

    model_path = os.path.join(MODEL_STORAGE_DIR, filename)
    file.save(model_path)

    # Extract and validate metadata
    name, version, accuracy = request.form.get('name'), request.form.get('version'), request.form.get('accuracy')
    if not all([name, version, accuracy]):
        return jsonify({'message': 'Missing model metadata'}), 400

    # Save model metadata
    insert_model(name, version, accuracy, model_path)

    return jsonify({'message': f'Model {name} uploaded successfully!'}), 201

def get_models():
    """Retrieve metadata for all models."""
    models = get_all_models()
    return jsonify({'models': [{'id': model[0], 'name': model[1], 'version': model[2], 'accuracy': model[3], 'file_path': model[4]} for model in models]})

def get_model(name):
    """Retrieve metadata for a specific model by name."""
    model = get_model_by_name(name)
    if model:
        return jsonify({'id': model[0], 'name': model[1], 'version': model[2], 'accuracy': model[3], 'file_path': model[4]})
    return jsonify({'message': 'Model not found'}), 404
