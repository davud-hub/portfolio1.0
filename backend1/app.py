from flask import Flask

app = Flask(__name__)

@app.route("/")
def defaultEndPoint():
    return "ang is dom"

app.run()
