from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import db
from config import Config
from auth import auth_bp
from routes import routes  # ✅ Import the correct Blueprint

app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)

# ✅ Initialize JWT Authentication
jwt = JWTManager(app)

# ✅ Initialize Database
db.init_app(app)

# ✅ Enable CORS (Allow frontend to access API)
CORS(app)

# ✅ Register Blueprints Correctly
app.register_blueprint(auth_bp, url_prefix="/auth")  # User Authentication
app.register_blueprint(routes)  # ✅ Registers Home Page
# ✅ No need for another registration of "/api" because it's already in `routes.py`

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
