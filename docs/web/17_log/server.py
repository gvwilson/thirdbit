"""Server that handles file uploads with HTMX, enhanced with structured logging."""

from flask import Flask, render_template, request, g
from flask_cors import CORS
import os
from pathlib import Path
from werkzeug.utils import secure_filename
import structlog
from datetime import datetime
from functools import wraps

# Simple in-memory log storage (no thread safety needed for single-threaded mode)
LOGS = []

# Custom processor to store logs in memory
def store_log_processor(logger, method_name, event_dict):
    """Store log entries in the LOGS list."""
    log_entry = event_dict.copy()
    log_entry['level'] = method_name
    LOGS.append(log_entry)
    return event_dict

# Configure structlog with our custom processor
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        store_log_processor,
        structlog.processors.JSONRenderer()
    ],
    logger_factory=structlog.PrintLoggerFactory(),
    cache_logger_on_first_use=True,
)

# Create logger
logger = structlog.get_logger()

# Configure upload folder
UPLOAD_FOLDER = 'uploads'

def get_request_logger():
    """Create a logger with request context."""
    return logger.bind(
        user_agent=request.headers.get('User-Agent'),
        ip_address=request.remote_addr
    )

def get_uploaded_files():
    """Get list of uploaded files."""
    return os.listdir(UPLOAD_FOLDER) if os.path.exists(UPLOAD_FOLDER) else []

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
    
    @app.before_request
    def log_request():
        """Log all incoming requests."""
        if not request.path.startswith('/static'):
            logger.info("request", 
                      method=request.method,
                      path=request.path,
                      ip=request.remote_addr,
                      user_agent=request.headers.get('User-Agent'))
    
    @app.route('/')
    def index():
        """Render the upload form."""
        # Log page visit with context
        get_request_logger().info("page_view", page="index")
        
        files = get_uploaded_files()
        return render_template('index.html', files=files)
    
    @app.route('/upload', methods=['POST'])
    def upload_file():
        """Handle file upload."""
        req_logger = get_request_logger()
        
        if 'file' not in request.files:
            req_logger.warning("upload_failed", reason="no_file_in_request")
            return "No file selected", 400
            
        file = request.files['file']
        
        if file.filename == '':
            req_logger.warning("upload_failed", reason="empty_filename")
            return "No file selected", 400
            
        filename = secure_filename(file.filename)
        
        try:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_size = os.path.getsize(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            # Log successful upload with metadata
            req_logger.info("file_uploaded", 
                           filename=filename, 
                           file_size_bytes=file_size,
                           content_type=file.content_type)
                
            # Return a success message that HTMX will use to update the UI
            return render_template('file_item.html', filename=filename)
            
        except Exception as e:
            # Log error with exception details
            req_logger.exception("upload_error", 
                                filename=filename,
                                error_type=type(e).__name__,
                                error_msg=str(e))
            return "Upload failed", 500
    
    @app.route('/files')
    def list_files():
        """List uploaded files."""
        # Log files listing request
        get_request_logger().info("files_listed")
        
        files = get_uploaded_files()
        return render_template('file_list.html', files=files)
    
    @app.route('/delete/<filename>', methods=['DELETE'])
    def delete_file(filename):
        """Delete an uploaded file."""
        secure_name = secure_filename(filename)
        filepath = os.path.join(UPLOAD_FOLDER, secure_name)
        log_ctx = {'filename': secure_name}
        req_logger = get_request_logger()
        
        if not os.path.exists(filepath):
            req_logger.warning("delete_failed", reason="file_not_found", **log_ctx)
            return "File not found", 404
            
        try:
            file_size = os.path.getsize(filepath)
            os.remove(filepath)
            req_logger.info("file_deleted", file_size_bytes=file_size, **log_ctx)
            return "", 200
        except Exception as e:
            req_logger.exception("delete_error", 
                                error_type=type(e).__name__, 
                                error_msg=str(e),
                                **log_ctx)
            return "Delete failed", 500
    
    @app.route('/logs')
    def view_logs():
        """View recent logs."""
        try:
            # Log the view logs request
            get_request_logger().info("logs_viewed")
            
            # Get logs from our in-memory storage and sort by timestamp (newest first)
            recent_logs = sorted(LOGS.copy(), key=lambda x: x.get('timestamp', ''), reverse=True)
                       
            return render_template('logs.html', logs=recent_logs)
            
        except Exception as e:
            get_request_logger().exception("logs_view_error", 
                                        error_type=type(e).__name__,
                                        error_msg=str(e))
            return "Error fetching logs", 500

    return app

if __name__ == "__main__":
    # Log application startup
    logger.info("application_startup", 
               upload_folder=UPLOAD_FOLDER,
               max_content_length=16*1024*1024)
    
    app = create_app()
    # Run in single-threaded mode
    app.run(debug=True, threaded=False)
