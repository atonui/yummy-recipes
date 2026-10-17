"""Start the server"""
import os
from app import app

app.secret_key = "K!funguo51R1"

if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    app.run('', port=port)