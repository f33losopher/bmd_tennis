from tennis_score import TennisScore

class StandardScore(TennisScore):
    def __init__(self): {
        TennisScore.__init__(self)
    }

    def update_game_score(self, player1, player2):
        match_score = self.match_score['match']
        game_score = self.match_score['game']

        if match_score[player1][-1] == 6 and match_score[player2][-1] == 6:
            game_score[player1] += 1
            if (game_score[player1] >= 7) and ((game_score[player1] - game_score[player2]) > 1):
                self.update_match_score(player1, player2)
                game_score[player1] = 0
                game_score[player2] = 0
        else:
            if game_score[player1] == 0:
                game_score[player1] = 15
            elif game_score[player1] == 15:
                game_score[player1] = 30
            elif game_score[player1] == 30:
                game_score[player1] = 40
            elif game_score[player1] == 40:
                if game_score[player2] == 40:
                    game_score[player1] = 'Ad'
                    game_score[player2] = '-'
                else:
                    self.update_match_score(player1, player2)
                    game_score[player1] = 0
                    game_score[player2] = 0
            elif game_score[player1] == 'Ad':
                self.update_match_score(player1, player2)
                game_score[player1] = 0
                game_score[player2] = 0
            elif game_score[player1] == '-':
                game_score[player1] = 40
                game_score[player2] = 40
    
    def update_match_score(self, player1, player2):
        match_score = self.match_score['match']
        match_score[player1][-1] += 1

        if ((match_score[player1][-1] == 6) and (match_score[player2][-1] < 5)) or match_score[player1][-1] == 7:
            # Player1 wins set
            match_score[player1].append(0)
            match_score[player2].append(0)