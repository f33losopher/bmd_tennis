from project_consts import *

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

        if ('init_score' in globals() and init_score['match']):
            self.match_score['match'][PLAYER1] = init_score['match'][PLAYER1]
            self.match_score['match'][PLAYER2] = init_score['match'][PLAYER2]
        if ('init_score'  in globals() and init_score['game']):
            self.match_score['game'][PLAYER1] = init_score['game'][PLAYER1]
            self.match_score['game'][PLAYER2] = init_score['game'][PLAYER2]
    
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