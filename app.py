from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Xin chào! Đây là ứng dụng Flask chạy trên Heroku! thank you to you "

if __name__ == '__main__':
    app.run()
