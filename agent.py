import requests

BOT_TOKEN = "8651671485:AAE1uudOzDkBDvW2OaVrKQZoIomb5hxTSy4"
CHAT_ID = 1160495820

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": "🔥 مبروك! البوت شغال 100%"
    }
)
