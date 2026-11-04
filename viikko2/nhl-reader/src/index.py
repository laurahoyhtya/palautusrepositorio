from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def _create_table(title):
    table = Table(title=title)
    table.add_column("Rank", justify="right")
    table.add_column("Player")
    table.add_column("Team")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right", style="bold")
    return table


def _add_players_to_table(table, players):
    for rank, player in enumerate(players, start=1):
        points = player.goals + player.assists
        table.add_row(
            str(rank),
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(points),
        )


def main():
    season = input("Season (e.g. 2024-25): ").strip()
    nationality = input("Country code (e.g. FIN): ").strip().upper()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    table = _create_table(f"Players in {season} ({nationality})")
    _add_players_to_table(table, players)
    Console().print(table)


if __name__ == "__main__":
    main()
