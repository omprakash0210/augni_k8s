import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>HELLO SCRIBETECH.</h1> <br>This is version V2 of application."

app.run(host="0.0.0.0", port=80)