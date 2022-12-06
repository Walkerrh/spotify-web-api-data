import requests
import os
from base.main import (
    obtain_auth_token, read_config
)


# Note: Chapter are only available for the
# US, UK, Ireland, New Zealand and Australia markets.
# The search can be extended with filters as stated in the doc
class Search:
    def __init__(self):
        self.base_url = read_config("CLIENT_CREDENTIALS", "BASE_URL")
        self.auth_token = obtain_auth_token()
        self.headers = {
            "Authorization": self.auth_token[
                "token_type"
                ] + " " + self.auth_token["access_token"],
            "Content-Type": "application/json"
        }

    def search(self, q: str, type: str = "track", limit: int = 20, country_code: str = "US"):
        response = requests.get(
            self.base_url + "/search",
            headers=self.headers,
            params={
                "q": q,
                "type": type,
                "limit": limit,
                "market": country_code
            }
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]


Search().search(
    q="names"
)
