from flask import Flask
from datetime import datetime

app = Flask(__name__)

number = 1
start_time = str(datetime.now())

@app.route("/", methods=["GET"])
def main():
    """
    Handler for index.
    """
    global number
    global start_time

    resp = [
        "Hello world!",
        f"You are visitor number: {number}",
        f"Start Time: {start_time}"
    ]
    number += 1
    return "\n".join(resp)

if __name__ == "__main__":
    app.run(debug=False)
