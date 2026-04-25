import requests

BOT_TOKEN="
BOT_TOKEN="8737038270:AAEprrM2beRSvTYOVshmM3oaOLpw2YdxPb4"
CHAT_ID="1160495820"

listings=[
{
"district":"السويدي",
"area":400,
"street":20,
"price":800000,
"type":"أرض"
}
]

for item in listings:

    ppm=item["price"]/item["area"]

    if ppm<=2500 and item["area"]<=500 and item["street"]>=15:

        msg=f"""
🔥 فرصة عقارية

{item["type"]}
{item["district"]}
{item["area"]}م
شارع {item["street"]}

سعر المتر {ppm}
"""

        url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        requests.post(
            url,
            data={
                "chat_id":CHAT_ID,
                "text":msg
            }
        )
