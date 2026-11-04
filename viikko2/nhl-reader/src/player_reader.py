import requests

from player import Player


# pylint: disable-next=too-few-public-methods  # Reading players is this class's single responsibility.
class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url, timeout=10).json()
        return [Player(player_dict) for player_dict in response]
