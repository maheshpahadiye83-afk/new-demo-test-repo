"""
Simple Flask web application for Docker demonstration
"""

from flask import Flask, jsonify
import os

app = Flask(__name__)

# Environment configuration
PORT = int(os.getenv('PORT', 8000))
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'


@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Welcome to Docker Python CI/CD Demo',
        'status': 'running',
        'version': '1.0.0'
    })


@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'docker-python-app'
    }), 200


@app.route('/api/info')
def api_info():
    """API information endpoint"""
    return jsonify({
        'api_version': '1.0',
        'endpoints': [
            '/',
            '/health',
            '/api/info'
        ],
        'python_version': '3.11',
        'docker_enabled': True
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'message': str(error)
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'message': str(error)
    }), 500


if __name__ == '__main__':
    print(f"Starting Flask application on port {PORT}")
    print(f"Debug mode: {DEBUG}")
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
