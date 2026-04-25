import requests

BOT_TOKEN = "8651671485:AAE1uudOzDkBDvW2OaVrKQZoIomb5hxTSy4"

# يجيب آخر رسالة (وفيها chat_id)
res = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates").json()

print(res)
