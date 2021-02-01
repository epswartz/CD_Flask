from flask import Flask
from datetime import datetime

app = Flask(__name__)

start_time = str(datetime.now())

@app.route("/", methods=["GET"])
def main():
    """
    Handler for index.
    """

    resp = [
        "Hello world!!!",
        f"Start Time: {start_time}"
    ]
    return "\n".join(resp)

if __name__ == "__main__":
    app.run(debug=False)
