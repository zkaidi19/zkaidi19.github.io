#!/usr/bin/env python3
"""
Personal Website - Kaidi Zhang
Development Server Runner

This script provides a convenient way to run the Flask application
with different configurations for development and production.
"""

import os
import sys
from app import app

def run_development():
    """Run the Flask app in development mode"""
    print("🚀 Starting Kaidi Zhang's Personal Website in Development Mode")
    print("📍 URL: http://localhost:5000")
    print("🔧 Debug Mode: Enabled")
    print("⚡ Auto-reload: Enabled")
    print("-" * 50)
    
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
        use_reloader=True,
        use_debugger=True
    )

def run_production():
    """Run the Flask app in production mode"""
    print("🌐 Starting Kaidi Zhang's Personal Website in Production Mode")
    print("📍 URL: http://0.0.0.0:5000")
    print("🔒 Debug Mode: Disabled")
    print("⚡ Auto-reload: Disabled")
    print("-" * 50)
    
    app.run(
        debug=False,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        use_reloader=False
    )

def show_help():
    """Show help information"""
    print("""
    🌟 Kaidi Zhang's Personal Website Runner
    
    Usage:
        uv run python run.py [mode]
    
    Modes:
        dev, development    - Run in development mode (default)
        prod, production    - Run in production mode
        help, -h, --help    - Show this help message
    
    Examples:
        uv run python run.py                # Development mode
        uv run python run.py dev            # Development mode
        uv run python run.py production     # Production mode
    
    Alternative (using gunicorn for production):
        uv run gunicorn --bind 0.0.0.0:5000 app:app
    
    Environment Variables:
        PORT                 - Port to run on (default: 5000)
        FLASK_ENV           - Flask environment (development/production)
    """)

if __name__ == '__main__':
    # Get command line argument
    mode = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    
    if mode in ['help', '-h', '--help']:
        show_help()
    elif mode in ['prod', 'production']:
        run_production()
    elif mode in ['dev', 'development'] or not mode:
        run_development()
    else:
        print(f"❌ Unknown mode: {mode}")
        print("💡 Use 'python run.py help' for usage information")
        sys.exit(1)
