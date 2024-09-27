from flask import Flask
import pytz
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz)
    return f"{current_time.strftime('%Y:%m:%d %H:%M:%S')}"


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
