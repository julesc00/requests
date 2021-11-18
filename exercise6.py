"""
Using sessions to persist parameters across requests.
"""
import pprint

import requests
from getpass import getpass


USER_URL = "https://api.github.com/user"

with requests.Session() as session:
    session.auth = ("username", getpass())

    res = session.get(USER_URL)

pp = pprint.PrettyPrinter(indent=1)
pp.pprint(res.headers)
pp.pprint(res.json())
