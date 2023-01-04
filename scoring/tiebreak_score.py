from tennis_score import TennisScore

class TiebreakScore(TennisScore):

    _goal = 7
    def __init__(self, goal): {
        self._goal = goal
        TennisScore.__init__(self)

    }

    def update_game_score(self, player1, player2):
        match_score = self.match_score['match']
        game_score = self.match_score['game']

        game_score[player1] += 1
        if (game_score[player1] >= 7) and ((game_score[player1] - game_score[player2]) > 1):
            self.update_match_score(player1, player2)
            game_score[player1] = 0
            game_score[player2] = 0

    def update_match_score(self, player1, player2):
        match_score = self.match_score['match']
        match_score[player1][-1] += 1
