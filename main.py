import requests
import smtplib

api_key = "8f1ee43151d34f569522c7940c191e47"
url = (
    "https://newsapi.org/v2/everything?"
    "q=tesla&"
    "from=2025-06-05&"
    "sortBy=publishedAt&"
    "apiKey=8f1ee43151d34f569522c7940c191e47"
)
request = requests.get(url)
content = request.json()
for article in content["article"]:
    print(article["title"])

