from project_consts import GAME_TYPE
from project_consts import CONFIG
from tennis_score import TennisScore
from standard_score import StandardScore
# from tiebreak_score import TiebreakScore

def createTennisScore():
    if (CONFIG[GAME_TYPE] == 'Standard'):
        return StandardScore()
    # elif (CONFIG[GAME_TYPE] == 'Tiebreak'):
    #     return TiebreakScore(7)
