from time import sleep
from flask import Flask


app = Flask(__name__)


@app.route("/delay")
def delay():
    sleep(0.3)
    return "ok"


@app.route("/simple")
def simple():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7575, debug=False)
