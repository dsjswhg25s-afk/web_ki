from flask import Flask, request, jsonify
import random
from flask_cors import CORS

# Flask-App erstellen
app = Flask(__name__)

# CORS aktivieren (wichtig für Browser-Zugriff!)
CORS(app)

# ----------------------------------------------------
# KI-Logik
# ----------------------------------------------------
def antwort_generieren(nachricht: str) -> str:
    nachricht = nachricht.lower().strip()

    if not nachricht:
        return "Sag mir bitte eine Frage oder Nachricht."

    # Begrüßungen
    if any(wort in nachricht for wort in ["hallo", "hi", "hey", "moin", "servus"]):
        return random.choice([
            "Hallo! Wie kann ich dir helfen?",
            "Hey, schön dass du da bist!",
            "Moin! Was gibt's?",
        ])

    # Wie geht's
    if "wie geht" in nachricht:
        return "Mir geht es gut – ich bin bereit für deine Fragen. Und dir?"

    # Name der KI
    if "wie heißt du" in nachricht or "wie heisst du" in nachricht:
        return "Ich bin die Web-KI auf dieser Seite. Du kannst mir einen Namen geben."

    # Beispiel: Öffnungszeiten
    if "öffnungszeiten" in nachricht or "oeffnungszeiten" in nachricht:
        return "Die Öffnungszeiten findest du oberhalb. Normalerweise Mo–Fr 9–18 Uhr."

    # Beispiel: Email
    if "email" in nachricht or "e-mail" in nachricht:
        return "Du kannst uns per E-Mail kontaktieren. Die Adresse steht im Impressum."

    # Beenden
    if nachricht in ["ende", "tschüss", "tschuss", "quit", "exit"]:
        return "Danke für die Unterhaltung. Bis zum nächsten Mal!"

    # Standardantworten
    standard_antworten = [
        "Interessant – erzähl mir mehr.",
        "Okay, was möchtest du genau wissen?",
        "Verstehe. Kannst du das genauer erklären?",
        "Gute Frage. Lass uns darüber sprechen.",
    ]
    return random.choice(standard_antworten)


# ----------------------------------------------------
# API-Endpunkt für die Kommunikation
# ----------------------------------------------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_message = data.get("message", "")
    reply = antwort_generieren(user_message)
    return jsonify({"reply": reply})


# ----------------------------------------------------
# Test-Endpunkt (Homepage)
# ----------------------------------------------------
@app.route("/", methods=["GET"])
def index():
    return "Web-KI läuft! Sende POST-Anfragen an /chat."


# ----------------------------------------------------
# App starten
# ----------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
