import requests

res = requests.get("https://api.github.com")

# if res.status_code == 200:
#     print("Success!")
# elif res.status_code == 404:
#     print("Not found.")

if res:
    print("Success")
else:
    print("An error occurred")
