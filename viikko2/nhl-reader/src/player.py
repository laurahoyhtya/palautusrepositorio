# pylint: disable-next=too-few-public-methods  # A data model exposes attributes rather than methods.
class Player:
    def __init__(self, player_data):
        self.name = player_data['name']
        self.nationality = player_data['nationality']
        self.team = player_data['team']
        self.goals = player_data['goals']
        self.assists = player_data['assists']

    def __str__(self):
        return self.name
