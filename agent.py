import requests

BOT_TOKEN = "8651671485:AAE1uudOzDkBDvW2OaVrKQZoIomb5hxTSy4"
CHAT_ID = 1160495820

MAX_PPM = 2500

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

# 🔥 بيانات مثال (تمثيل إعلانات)
ads = [
    {"title":"ارض السويدي","area":400,"price":800000},
    {"title":"فيلا الشفا","area":450,"price":1200000},
    {"title":"ارض رخيصة","area":420,"price":700000},
]

for ad in ads:

    ppm = ad["price"] / ad["area"]

    if ppm <= MAX_PPM:

        msg = f"""
🔥 فرصة محتملة!

📍 {ad['title']}
📐 {ad['area']} م
💰 {ad['price']}
📊 {ppm:.0f} / متر
"""
        send(msg)
