from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bundesliga-Tipp-API läuft!"

@app.route("/tipps")
def tipps():
    return jsonify({
        "text": "🚀 31. Spieltag – 1. Bundesliga (25.–27. April 2025)\n\n🏟 Fr: Stuttgart vs. Heidenheim ➡️ 3:1\n📖 Sa: Bayern vs. Mainz ➡️ 3:0\n📅 So: Bremen vs. St. Pauli ➡️ 2:0"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
