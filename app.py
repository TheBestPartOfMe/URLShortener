from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to URL Shortener!'

if __name__ == '__main__':
    app.run(debug=True)
