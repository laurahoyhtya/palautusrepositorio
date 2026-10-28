import unittest

from player import Player
from statistics_service import StatisticsService


class PlayerReaderStub:
    def __init__(self, players):
        self._players = players

    def get_players(self):
        return self._players


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.players = [
            Player("Mikko Rantanen", "COL", 20, 30),
            Player("Sebastian Aho", "CAR", 25, 20),
            Player("Aleksander Barkov", "FLA", 15, 25),
        ]
        self.statistics_service = StatisticsService(
            PlayerReaderStub(self.players)
        )

    def test_search_returns_matching_player(self):
        result = self.statistics_service.search("Aho")

        self.assertIs(result, self.players[1])

    def test_search_returns_none_when_no_player_matches(self):
        result = self.statistics_service.search("Unknown")

        self.assertIsNone(result)

    def test_team_returns_players_from_the_requested_team(self):
        result = self.statistics_service.team("COL")

        self.assertEqual(result, [self.players[0]])

    def test_top_returns_requested_number_plus_one_players_in_points_order(self):
        result = self.statistics_service.top(1)

        self.assertEqual(result, [self.players[0], self.players[1]])


if __name__ == "__main__":
    unittest.main()
