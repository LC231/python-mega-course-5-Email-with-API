import requests
from send_email import send_email

topic = "tesla"
api_key = "8f1ee43151d34f569522c7940c191e47"
url = (
    "https://newsapi.org/v2/everything?"
    f"q={topic}&"
    "from=2025-06-05&"
    "sortBy=publishedAt&"
    "apiKey=8f1ee43151d34f569522c7940c191e47&language=en"
)


# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" 
        + "\n" + body + article["title"] + "\n" \
        + str(article["description"]) + 2*"\n" \
        + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)