import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16) # For Flask security
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:passowrd@localhost:5432/your_db_name"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GEMINI_API_KEY = "your Gemini key"  # Replace with your actual API key
    JWT_SECRET_KEY = "your Jwt token key"
    JWT_ACCESS_TOKEN_EXPIRES = 3600  #  Tokens expire in 1 hour
