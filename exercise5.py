import requests
from requests.exceptions import Timeout


URL = 'https://api.github.com'

try:
    res = requests.get(URL, timeout=1)

except Timeout:
    print("The request timed out.")
else:
    print("Did not timed out.")
