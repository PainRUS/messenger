from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! 1223"

@app.route("/status")
def status():
    return {"abc": 123}


app.run()