class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0
        self.scores = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}

    def won_point(self, player_name):
        if player_name == self.player1:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        score = ""
        if self.player1_score == self.player2_score:
            score = self.even_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.win_or_advantage(score)
        else:
            score = self.points_to_scores()
        return score

    def points_to_scores(self):
        return f"{self.scores[self.player1_score]}-{self.scores[self.player2_score]}"

    def even_score(self):
        if self.player1_score in self.scores:
            return f"{self.scores[self.player1_score]}-All"
        else:
            return "Deuce"
    
    def win_or_advantage(self, score):
        point_difference = self.player1_score - self.player2_score
        if point_difference == 1:
            score = "Advantage player1"
        elif point_difference == -1:
            score = "Advantage player2"
        elif point_difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

