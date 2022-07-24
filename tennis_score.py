class TennisScore:
    def __init__(self):
        self.match_score = {
            'match': {
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
        pass

    # player1 won game
    # player2 lost game
    def update_match_score(self, player1, player2):
        pass