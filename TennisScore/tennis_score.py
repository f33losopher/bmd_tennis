class TennisScore:
    def __init__(self):
        self.match_score = {
            'set': {
                'Player1': [0],
                'Player2': [0]
            },
            'game': {
                'Player1': 0,
                'Player2': 0
            }
        }
    
    def get_match_score(self):
        return self.match_score

    # player1 won point
    # player2 lost point
    def update_game_score(self, player1, player2):
        # TODO need to account for a tie break

        set_score = self.match_score['set']
        game_score = self.match_score['game']

        if set_score[player1][-1] == 6 and set_score[player2][-1] == 6:
            game_score[player1] += 1
            if (game_score[player1] >= 7) and ((game_score[player1] - game_score[player2]) > 1):
                self.update_set_score(player1, player2)
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
                    self.update_set_score(player1, player2)
                    game_score[player1] = 0
                    game_score[player2] = 0
            elif game_score[player1] == 'Ad':
                self.update_set_score(player1, player2)
                game_score[player1] = 0
                game_score[player2] = 0
            elif game_score[player1] == '-':
                game_score[player1] = 40
                game_score[player2] = 40
    
    # player1 won game
    # player2 lost game
    def update_set_score(self, player1, player2):
        set_score = self.match_score['set']
        set_score[player1][-1] += 1

        if ((set_score[player1][-1] == 6) and (set_score[player2][-1] < 5)) or set_score[player1][-1] == 7:
            # Player1 wins set
            set_score[player1].append(0)
            set_score[player2].append(0)