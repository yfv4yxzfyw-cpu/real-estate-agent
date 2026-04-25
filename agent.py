import requests

BOT_TOKEN = "8651671485:AAE1uudOzDkBDvW2OaVrKQZoIomb5hxTSy4"
CHAT_ID = 1160495820

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

# 🔥 روابط بحث مباشرة من حراج
links = [
    "https://haraj.com.sa/search/اراضي-للبيع-الرياض-السويدي",
    "https://haraj.com.sa/search/اراضي-للبيع-الرياض-الشفا",
    "https://haraj.com.sa/search/فلل-للبيع-الرياض-جنوب",
]

msg = "🔎 تحديث جديد من حراج:\n\n"

for link in links:
    msg += link + "\n\n"

msg += "📊 شروطك:\nسعر متر ≤ 2500\nمساحة ≤ 500\nشارع ≥ 15"

send(msg)
