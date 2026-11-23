class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    WINNING_SCORE = 4
    ADVANTAGE_DIFFERENCE = 1
    WIN_DIFFERENCE = 2

    POINT_NAMES = {
        LOVE: "Love",
        FIFTEEN: "Fifteen",
        THIRTY: "Thirty",
        FORTY: "Forty",
    }

    TIED_SCORE_NAMES = {
        LOVE: "Love-All",
        FIFTEEN: "Fifteen-All",
        THIRTY: "Thirty-All",
    }

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def get_score(self):
        if self.scores_are_tied():
            return self.get_tied_score()
        if self.is_endgame():
            return self.get_endgame_score()
        return self.get_normal_score()

    def scores_are_tied(self):
        return self.player1_points == self.player2_points

    def get_tied_score(self):
        if self.player1_points in self.TIED_SCORE_NAMES:
            return self.TIED_SCORE_NAMES[self.player1_points]
        return "Deuce"

    def is_endgame(self):
        return (
            self.player1_points >= self.WINNING_SCORE
            or self.player2_points >= self.WINNING_SCORE
        )

    def get_endgame_score(self):
        point_difference = self.player1_points - self.player2_points

        if point_difference == self.ADVANTAGE_DIFFERENCE:
            return f"Advantage {self.player1_name}"
        if point_difference == -self.ADVANTAGE_DIFFERENCE:
            return f"Advantage {self.player2_name}"
        if point_difference >= self.WIN_DIFFERENCE:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def get_normal_score(self):
        player1_score = self.POINT_NAMES[self.player1_points]
        player2_score = self.POINT_NAMES[self.player2_points]
        return f"{player1_score}-{player2_score}"
