from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Xin chào! Đây là ứng dụng Flask chạy trên Heroku!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
