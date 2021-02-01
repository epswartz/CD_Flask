from flask import Flask
from datetime import datetime

application = Flask(__name__)

start_time = str(datetime.now())

@application.route("/", methods=["GET"])
def main():
    """
    Handler for index.
    """

    resp = [
        "Hello world!!!!!!!",
        f"Start Time: {start_time}"
    ]
    return "\n".join(resp)

if __name__ == "__main__":
    application.run(debug=False)
