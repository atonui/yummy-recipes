"""Start the server"""
from app import app

app.secret_key = "K!funguo51R1"

if __name__ == "__main__":
    app.run()