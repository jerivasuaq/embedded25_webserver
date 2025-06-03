from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def main():
    name = "Pepe"

    return render_template('fb.html', person=name)

@app.route("/health")
def health():
    x = 1+1
    
    return "<p>Server is up and running.</p>"
