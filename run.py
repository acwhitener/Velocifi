from flask import Flask
from backend.database import db
from app.layout import init_dashboard  # This creates and mounts the Dash app
import dash
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask server (used by Dash)
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(server)

# Create database tables if they don't exist
with server.app_context():
    db.create_all()

# Initialize Dash app (uses Flask server)
dash_app = init_dashboard(server)

# Debug log of loaded Dash pages
print("📄 Dash Pages Loaded:")
for page in dash.page_registry.values():
    print(f" - {page['module']} -> {page['path']}")

# Run the Dash app server (not Flask directly!)
if __name__ == "__main__":
    print("✅ Velocifi server is starting on http://127.0.0.1:5000 ...")
    dash_app.run(debug=True, port=5000)
