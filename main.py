from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    x = 1+1

    return "<p>Hello, World!</p>"


@app.route("/health")
def health():
    x = 1+1
    
    return "<p>Server is up and running.</p>"
