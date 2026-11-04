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


def _get_players_to_display(stats, season):
    selection = input("Show players by (N)ationality or (T)eam? ").strip().upper()
    while selection not in ("N", "T"):
        print("Please enter N for nationality or T for team.")
        selection = input("Show players by (N)ationality or (T)eam? ").strip().upper()

    if selection == "T":
        team = input("Team abbreviation (e.g. BOS): ").strip().upper()
        return stats.top_scorers_by_team(team), f"Players in {season} (Team {team})"

    nationality = input("Country code (e.g. FIN): ").strip().upper()
    return (
        stats.top_scorers_by_nationality(nationality),
        f"Players in {season} ({nationality})",
    )


def main():
    season = input("Season (e.g. 2024-25): ").strip()
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players, title = _get_players_to_display(stats, season)

    table = _create_table(title)
    _add_players_to_table(table, players)
    Console().print(table)


if __name__ == "__main__":
    main()
