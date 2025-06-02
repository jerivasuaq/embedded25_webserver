# Simple web server

# Pre-requisites


```
sudo apt install python3 python3-pip python3-venv
```

# Create venv

```
python3 -m venv .venv
source .venv/bin/activate
```

# Install requirements

Create a requierements file.

``` requirements.txt
flask
```

install requirements:

```
pip3 install -r requirements.txt
```

# Run the website

```
flask --app main run
```

- visit (http://127.0.0.1:5000/)[http://127.0.0.1:5000/]

