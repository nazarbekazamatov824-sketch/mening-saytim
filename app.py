import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
  return "Salom, mening saytim ishlayapti!"


if __name__ == "__main__":
  # Render avtomatik beradigan portni o'qiydi, agar bo'lmasa 5000-portni ishlatadi
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)