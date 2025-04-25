import os
import psycopg2
import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing) if frontend and backend are hosted on different domains
CORS(app)

# Get database connection details from environment variables
db_host = os.getenv('DB_HOST', 'localhost')
db_name = os.getenv('DB_NAME', 'mydb')
db_user = os.getenv('DB_USER', 'user')
db_pass = os.getenv('DB_PASS', 'password')

def get_db_connection():
    """Helper function to establish a connection to the database."""
    return psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_pass
    )

@app.route('/')
def home():
    return jsonify(message="Hello from the backend API!")

@app.route('/contact', methods=['POST'])
def contact():
    try:
        # Get JSON data from frontend
        data = request.get_json()
        
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')

        # Basic validation
        if not name or not email or not phone or not message:
            return jsonify(message="All fields are required!"), 400

        # Connect to PostgreSQL
        conn = get_db_connection()
        cur = conn.cursor()

        # Insert data into the 'contacts' table (you should create this table in your DB)
        insert_query = """
        INSERT INTO contacts (name, email, phone, message)
        VALUES (%s, %s, %s, %s);
        """
        cur.execute(insert_query, (name, email, phone, message))
        
        # Commit transaction and close connection
        conn.commit()
        cur.close()
        conn.close()

        return jsonify(message="Your message has been sent successfully!"), 200
    
    except Exception as e:
        # Log error for debugging
        logger.error(f"Error occurred: {e}")
        return jsonify(message=f"Error: {e}"), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
