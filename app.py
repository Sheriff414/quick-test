from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "I am DevOps engineer!"

app.run(host="0.0.0.0", port=5000)
