import requests
import pprint


URL = "https://api.github.com/search/repositories"
res = requests.get(
    URL,
    params={"q": "requests+language:python"},
    headers={"Accept": "application/vnd.github.v3.text-match+json"}
)


json_res = res.json()
repo = json_res.get("items", "")[0]
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(f"Text matches: {repo.get('text_matches', '')}")
