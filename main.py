from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Bundesliga-Tipp-API läuft!"

@app.route("/tipps")
def tipps():
    res = requests.get("https://bundesligabot-content.vercel.app/spieltag.json")
    return res.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
