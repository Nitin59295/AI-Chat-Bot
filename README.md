# AI-Chat-Bot

# AI Chat Bot

## Introduction
The **AI Chat Bot** is a Flask-based chatbot designed to interact with users, providing responses based on predefined logic or AI models. It is built using Python and can be extended to integrate NLP models for intelligent conversations.

## Features
- Interactive chatbot interface
- Flask-based web framework
- Modular architecture with authentication
- Database support for storing user interactions
- Scalable and customizable

## Technologies Used
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (Bootstrap)
- **Database:** PostgreSQL (or SQLite for development)
- **Authentication:** JWT-based authentication
- **AI/NLP Models:** Can be integrated with OpenAI GPT, NLTK, or custom ML models

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- PostgreSQL (optional)
- Git

### Steps to Set Up the Project
1. **Clone the Repository**
   ```sh
   git clone https://github.com/Nitin59295/AI-Chat-Bot.git
   cd AI-Chat-Bot
   ```

2. **Create a Virtual Environment & Install Dependencies**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   pip install -r requirements.txt
   ```

3. **Set Up the Database**
   - Configure `config.py` with your database credentials.
   - Run migrations (if applicable):
     ```sh
     flask db init
     flask db migrate -m "Initial migration"
     flask db upgrade
     ```

4. **Run the Application**
   ```sh
   flask run
   ```
   The chatbot will be accessible at `http://127.0.0.1:5000/`

## Usage
- Open the web interface and start a conversation.
- Customize responses and AI logic in `routes.py`.
- Extend with NLP models for AI-driven responses.

## Folder Structure
```
AI-Chat-Bot/
│-- app.py          # Main Flask application file
│-- auth.py         # Authentication logic
│-- config.py       # Configuration settings
│-- models.py       # Database models
│-- routes.py       # API routes and chatbot logic
│-- static/         # CSS and static files
│-- templates/      # HTML templates
│-- README.md       # Project documentation
```

## Contributing
Feel free to fork the repository and contribute! Submit a pull request with improvements or new features.

## License
This project is open-source and available under the MIT License.

## Contact
For any issues or feature requests, please open an issue on [GitHub](https://github.com/Nitin59295/AI-Chat-Bot).

