import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.players = [
            Player(
                {
                    "name": "Alex",
                    "nationality": "FIN",
                    "team": "BOS",
                    "goals": 10,
                    "assists": 5,
                }
            ),
            Player(
                {
                    "name": "Blake",
                    "nationality": "CAN",
                    "team": "BOS",
                    "goals": 8,
                    "assists": 12,
                }
            ),
            Player(
                {
                    "name": "Casey",
                    "nationality": "FIN",
                    "team": "NYR",
                    "goals": 15,
                    "assists": 2,
                }
            ),
        ]
        self.stats = PlayerStats(PlayerReaderStub(self.players))

    def test_top_scorers_by_nationality_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual([player.name for player in result], ["Casey", "Alex"])

    def test_top_scorers_by_team_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_team("BOS")

        self.assertEqual([player.name for player in result], ["Blake", "Alex"])

    def test_top_goal_scorers_sorts_by_goals_and_limits_results(self):
        result = self.stats.top_goal_scorers(2)

        self.assertEqual([player.name for player in result], ["Casey", "Alex"])

    def test_top_goal_scorers_returns_empty_list_for_zero_limit(self):
        self.assertEqual(self.stats.top_goal_scorers(0), [])

    def test_filters_return_empty_list_when_there_are_no_matches(self):
        self.assertEqual(self.stats.top_scorers_by_nationality("SWE"), [])
        self.assertEqual(self.stats.top_scorers_by_team("MTL"), [])


if __name__ == "__main__":
    unittest.main()
