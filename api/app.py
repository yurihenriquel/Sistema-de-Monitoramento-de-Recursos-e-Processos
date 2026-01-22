from flask import Flask
from api.database import init_db
from api.routes import metrics_bp

app = Flask(__name__)

init_db()
app.register_blueprint(metrics_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
