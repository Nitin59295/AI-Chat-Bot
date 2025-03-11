import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16) # For Flask security
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:qwerty@localhost:5432/Aibot"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GEMINI_API_KEY = "Your Gemini Api key "  # Replace with your actual API key
    JWT_SECRET_KEY = "Your JWT Key"
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # ✅ Tokens expire in 1 hour