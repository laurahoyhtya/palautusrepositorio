# pylint: disable-next=too-few-public-methods  # This class intentionally provides one query operation.
class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader

    def top_scorers_by_nationality(self, nationality):
        players = filter(
            lambda player: player.nationality == nationality,
            self.player_reader.get_players(),
        )
        return sorted(
            players,
            key=lambda player: player.goals + player.assists,
            reverse=True,
        )

    def top_scorers_by_team(self, team):
        players = filter(
            lambda player: player.team == team,
            self.player_reader.get_players(),
        )
        return sorted(
            players,
            key=lambda player: player.goals + player.assists,
            reverse=True,
        )

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa
        laskevassa maalijärjestyksessä."""
        players = self.player_reader.get_players()
        return sorted(
            players,
            key=lambda player: player.goals,
            reverse=True,
        )[:how_many]
