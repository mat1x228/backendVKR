from flask import Flask
from api.routes import messages_bp

app = Flask(__name__)

app.register_blueprint(messages_bp)

if __name__ == '__main__':
    app.run()
