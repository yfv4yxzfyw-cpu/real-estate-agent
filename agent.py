import requests

BOT_TOKEN = 8651671485:AAE1uudOzDkBDvW2OaVrKQZoIomb5hxTSy4

# يجيب آخر محادثة (chat_id) تلقائي
res = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates").json()

if not res["result"]:
    print("❌ ما فيه محادثة - لازم تضغط Start للبوت")
else:
    chat_id = res["result"][-1]["message"]["chat"]["id"]

    msg = "🔥 البوت شغال 100%"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, data={"chat_id": chat_id, "text": msg})
