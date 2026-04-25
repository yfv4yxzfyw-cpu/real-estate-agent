import requests
from bs4 import BeautifulSoup

BOT_TOKEN = "8651671485:AAE1uudOzDkBDvW2OaVrKQZoIomb5hxTSy4"
CHAT_ID = 1160495820

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

url = "https://haraj.com.sa/search/اراضي-للبيع-الرياض"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

ads = soup.find_all("a")

count = 0

for ad in ads:
    text = ad.get_text()

    if "الرياض" in text and ("ارض" in text or "فيلا" in text):
        send(f"🔎 إعلان:\n{text}")
        count += 1

    if count >= 5:
        break
