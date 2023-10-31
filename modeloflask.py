import os
from flask import Flask

app = Flask(__name__)
os.environ["FLASK_DEBUG"] = True
app.debug = os.environ.get("FLASK_DEBUG") == True

@app.route('/')

def home():
    return "/modelo.html"


if __name__ == "__main__":

    app.run(debug=True)
