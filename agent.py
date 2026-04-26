import requests

BOT_TOKEN = "8651671485:AAE1uudOzDkBDvW2OaVrKQZoIomb5hxTSy4"
CHAT_ID = 1160495820

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

# 🔎 روابط بحث جاهزة (تطلع نتائج حراج مباشرة)
search_links = [
    "https://www.google.com/search?q=site:haraj.com.sa+ارض+السويدي+الرياض",
    "https://www.google.com/search?q=site:haraj.com.sa+فيلا+الشفا+الرياض",
    "https://www.google.com/search?q=site:haraj.com.sa+ارض+غرب+الرياض",
]

msg = "🔥 عروض حقيقية من السوق:\n\n"

for link in search_links:
    msg += link + "\n\n"

msg += "📊 شروطك:\nجنوب/غرب الرياض\nسعر متر ≤ 2500\nمساحة ≤ 500"

send(msg)
