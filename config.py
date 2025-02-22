import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16) # For Flask security
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:qwerty@localhost:5432/Aibot"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GEMINI_API_KEY = "AIzaSyBR_CHlj0EEs3i7khkosrvICZyEq-RLglU"  # Replace with your actual API key
    JWT_SECRET_KEY = "2d19bf1cd8c2f7a4eb7eba1411a1f2b79039074df3df3fcd1eb3087d0658eb4c"
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # ✅ Tokens expire in 1 hour