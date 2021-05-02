class TennisScore:
    def __init__(self):
        self.match_score = {
            'set': {
                'felix': [0],
                'opponent': [0]
            },
            'game': {
                'felix': 0,
                'opponent': 0
            }
        }
    
    def get_match_score(self):
        return self.match_score

    # player1 won point
    # player2 lost point
    def update_game_score(self, player1, player2):
        if self.match_score['game'][player1] == 0:
            self.match_score['game'][player1] = 15;
        elif self.match_score['game'][player1] == 15:
            self.match_score['game'][player1] = 30;
        elif self.match_score['game'][player1] == 30:
            self.match_score['game'][player1] = 40;
        elif self.match_score['game'][player1] == 40:
            # TODO Finish Scoring
            print "Need to check if it's deuce"