import logging
from flask import Flask, jsonify

app = Flask(__name__)

# Configure logging to display in the terminal
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

@app.route('/', methods=['GET'])
def home():
    """GET / -> should return Hello World"""
    return "Hello World", 200

@app.route('/health', methods=['GET'])
def health():
    """GET /health -> should return healthy"""
    return "healthy", 200

@app.route('/feedback', methods=['POST'])
def feedback():
    """POST /feedback -> should return 201 success"""
    return jsonify({"status": "success"}), 201

@app.route('/log-test', methods=['GET'])
def log_test():
    """GET /log-test -> check logs appear in terminal"""
    logger.info("LOG TEST: The log-test endpoint was hit successfully!")
    return "Logs generated in terminal", 200

if __name__ == '__main__':
    # Runs on port 5000 as required by the Docker configuration
    app.run(host='0.0.0.0', port=5000, debug=True)
