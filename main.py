from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/health")
def health():
   
    return "<p>Server is up and running.</p>"

@app.route("/monitor")
def monitor():

    # calculate some metrics here

    data = [
        {"datetime": "2023-10-01T12:00:00Z", "temperature": "22.5"},
        {"datetime": "2023-10-01T12:01:00Z", "temperature": "22.7"},
        {"datetime": "2023-10-01T12:02:00Z", "temperature": "22.6"},
        {"datetime": "2023-10-01T12:03:00Z", "temperature": "22.8"},
        {"datetime": "2023-10-01T12:04:00Z", "temperature": "22.9"},
    ]

    person = "Pepe"
   
    return render_template('monitor.html', data=data, person=person)

@app.route("/data/append")
def data_append():

    datetime = request.args.get('datetime')
    temp = request.args.get('temp')
    if not datetime or not temp:
        return "<p>Error: Missing parameters</p>", 400
    
    # Here you would typically append the data to a database or a file
    print(f"Appending data: datetime={datetime}, temp={temp}")

    with open('data.txt', 'a') as f:
        f.write(f"{datetime},{temp}\n")

    return "<p>Data appended successfully.</p>"
