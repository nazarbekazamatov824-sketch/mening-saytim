import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  # Bu buyruq sizning templates papkangizdagi index.html ni ochib beradi
  return render_template("index.html")


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 10000))
  app.run(host="0.0.0.0", port=port)