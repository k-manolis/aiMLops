from flask import Flask
from routes import upload_model, get_models, get_model
from models import init_db

app = Flask(__name__)

# Initialize the database (create tables if they don't exist)
init_db()

# Define routes
app.add_url_rule('/models', 'upload_model', upload_model, methods=['POST'])
app.add_url_rule('/models', 'get_models', get_models, methods=['GET'])
app.add_url_rule('/models/<name>', 'get_model', get_model, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
