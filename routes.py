import google.generativeai as genai
from flask import Blueprint, jsonify, request, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, ChatHistory
from config import Config

# Define Blueprint
routes = Blueprint("routes", __name__)

# Configure Gemini API with correct key
genai.configure(api_key=Config.GEMINI_API_KEY)

# Serve Home Page
@routes.route("/", methods=["GET"])
def home():
    return render_template("index.html")  

@routes.route("/api/chat", methods=["POST"])
@jwt_required()
def chat():
    user_id = get_jwt_identity()
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400

    try:
        # Retrieve the last 5 messages to provide context
        recent_chats = ChatHistory.query.filter_by(user_id=user_id).order_by(ChatHistory.timestamp.desc()).limit(5).all()
        context = "\n".join([f"User: {chat.message}\nAI: {chat.response}" for chat in reversed(recent_chats)])
        # ✅ Call Gemini API with context
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(f"{context}\nUser: {user_message}\nAI:")
        bot_response = response.text if response.text else "I'm not sure how to respond."

        # Save chat history
        chat_entry = ChatHistory(user_id=user_id, message=user_message, response=bot_response)
        db.session.add(chat_entry)
        db.session.commit()

        return jsonify({"response": bot_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Fix 404 Error for Chat History API
@routes.route("/api/chat-history", methods=["GET"])
@jwt_required()
def chat_history():
    user_id = get_jwt_identity()
    chats = ChatHistory.query.filter_by(user_id=user_id).order_by(ChatHistory.timestamp.desc()).all()

    chat_list = [
        {"message": chat.message, "response": chat.response, "timestamp": chat.timestamp}
        for chat in chats
    ]
    
    return jsonify({"chat_history": chat_list})
