import requests
import json

# fetch data from reddit URL
url = "https://www.reddit.com/r/python/top.json"

# Adding headers
headers = {
    "User-Agent": "TrendPulse/1.0"
}

try:
    # Send request to reddit url to collect data
    response = requests.get(url, headers=headers)

    # Convert fetched data to JSON
    data = response.json()

    posts = []

    # Loop through the reddit posts
    for item in data['data']['children']:
        post = item['data']

        posts.append({
            "title": post.get("title"),
            "score": post.get("score"),
            "author": post.get("author"),
            "comments": post.get("num_comments"),
            "created": post.get("created_utc")
        })

    # Save data as JSON file
    with open("reddit_data.json", "w") as f:
        json.dump(posts, f, indent=4)

    print("Data saved successfully")

except Exception as e:
    print("Error:", e)