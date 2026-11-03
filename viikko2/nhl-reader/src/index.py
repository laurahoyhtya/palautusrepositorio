import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    finnish_players = filter(lambda player: player.nationality == "FIN", players)
    sorted_players = sorted(
        finnish_players,
        key=lambda player: player.goals + player.assists,
        reverse=True,
    )

    for player in sorted_players:
        print(f"{player.name} ({player.team}): {player.goals} goals, {player.assists} assists")

if __name__ == "__main__":
    main()
