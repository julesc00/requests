import requests

URL = "https://api.github.com/search/repositories"

# Search Github's repos for requests.
res = requests.get(
    URL,
    params={"q": "requests+language:python"}
)

# Inspect some attributes of the `requests` repo.
json_res = res.json()
repo = json_res.get("items", '')[0]
print(f"Repository name: {repo.get('name', '')}")
print(f"Repository description: {repo.get('description', '')}")
