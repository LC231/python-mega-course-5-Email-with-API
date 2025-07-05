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

# Make the API request
response = requests.get(url)
content = response.json()

# Start building the email content with one Subject header
body = "Subject: Today's News\n\n"

# Loop through the top 20 articles
for article in content.get("articles", [])[:20]:
    title = article.get("title") or "No Title"
    description = article.get("description") or "No Description"
    url = article.get("url") or "No URL Provided"

    body += f"{title}\n{description}\n{url}\n\n"

# Send the email (as a string)
body = body.encode("utf-8")
send_email(message=body)
