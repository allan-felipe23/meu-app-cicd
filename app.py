from flask import Flask, jsonify
import logging
import os
from datetime import datetime

app = Flask(__name__)

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables
PORT = int(os.getenv("PORT", 5000))
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    logger.info("🏠 Home endpoint acessado")
    return jsonify({
        "message": "Bem-vindo ao CI/CD Pipeline!",
        "status": "online",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "timestamp": datetime.now().isoformat()
    }), 200


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    logger.info("🏥 Health check")
    return jsonify({
        "status": "healthy",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "uptime": "running"
    }), 200


@app.route('/api/users', methods=['GET'])
def get_users():
    """Get users list"""
    logger.info("👥 Buscando usuários")
    return jsonify({
        "success": True,
        "count": 3,
        "users": [
            {
                "id": 1,
                "name": "João Silva",
                "email": "joao@example.com",
                "role": "Developer"
            },
            {
                "id": 2,
                "name": "Maria Santos",
                "email": "maria@example.com",
                "role": "DevOps"
            },
            {
                "id": 3,
                "name": "Pedro Costa",
                "email": "pedro@example.com",
                "role": "Cloud Architect"
            }
        ]
    }), 200


@app.route('/api/health/detailed', methods=['GET'])
def detailed_health():
    """Detailed health check with all services"""
    logger.info("📊 Health check detalhado")
    return jsonify({
        "status": "ok",
        "services": {
            "api": "running",
            "database": "connected",
            "cache": "active",
            "storage": "available"
        },
        "version": APP_VERSION,
        "timestamp": datetime.now().isoformat()
    }), 200


@app.route('/version', methods=['GET'])
def version():
    """Get app version"""
    logger.info("📦 Versão check")
    return jsonify({
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "build_time": "2025-12-21"
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    logger.warning(f"❌ 404 - Path not found")
    return jsonify({
        "error": "Not Found",
        "message": "Endpoint não existe",
        "status": 404
    }), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    logger.error(f"❌ 500 - Server error: {str(error)}")
    return jsonify({
        "error": "Internal Server Error",
        "message": "Erro no servidor",
        "status": 500
    }), 500


if __name__ == '__main__':
    logger.info(f"🚀 Iniciando aplicação na porta {PORT}")
    logger.info(f"🌍 Ambiente: {ENVIRONMENT}")
    logger.info(f"📦 Versão: {APP_VERSION}")
    app.run(host='0.0.0.0', port=PORT, debug=False)
