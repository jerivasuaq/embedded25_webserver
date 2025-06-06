# Simple web server

# Pre-requisites


```
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

# Create venv

```
python3 -m venv .venv
source .venv/bin/activate
```

# Install requirements


```
pip3 install -r requirements.txt
```

# Run the website

```
flask --app main run
```

- visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

# Test

test the monitor using

``` python
# use requrest to test the endpoints
import requests
print("Testing /health endpoint...")
response = requests.get("http://localhost:5000/data/append?temp=25")
```
