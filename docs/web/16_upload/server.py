"""Server that handles file uploads with HTMX."""

from flask import Flask, render_template, request
from flask_cors import CORS
import os
from pathlib import Path
from werkzeug.utils import secure_filename

# Configure upload folder
UPLOAD_FOLDER = 'uploads'

def create_app():
    """Build application and configure routes."""
    app = Flask(
        "upload_server", 
        static_folder=Path("../static").absolute(), 
        static_url_path="/static"
    )
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload
    CORS(app)
    
    # Create upload folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    @app.route('/')
    def index():
        """Render the upload form."""
        files = os.listdir(UPLOAD_FOLDER) if os.path.exists(UPLOAD_FOLDER) else []
        return render_template('index.html', files=files)
    
    @app.route('/upload', methods=['POST'])
    def upload_file():
        """Handle file upload."""
        if 'file' not in request.files:
            return "No file selected", 400
            
        file = request.files['file']
        
        if file.filename == '':
            return "No file selected", 400
            
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Return a success message that HTMX will use to update the UI
        return render_template('file_item.html', filename=filename)
    
    @app.route('/files')
    def list_files():
        """List uploaded files."""
        files = os.listdir(UPLOAD_FOLDER) if os.path.exists(UPLOAD_FOLDER) else []
        return render_template('file_list.html', files=files)
    
    @app.route('/delete/<filename>', methods=['DELETE'])
    def delete_file(filename):
        """Delete an uploaded file."""
        filepath = os.path.join(UPLOAD_FOLDER, secure_filename(filename))
        if os.path.exists(filepath):
            os.remove(filepath)
            return "", 200
        return "File not found", 404

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)