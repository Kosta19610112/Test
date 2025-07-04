from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "✅ Сервер работает!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render задаёт PORT
    print(f"🚀 Flask запускается на порту: {port}")
    app.run(host="0.0.0.0", port=port)
