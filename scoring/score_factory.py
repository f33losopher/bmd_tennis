from project_consts import GAME_TYPE
from tennis_score import TennisScore
from standard_score import StandardScore

def createTennisScore():
    if (GAME_TYPE == 'Standard'):
        return StandardScore()
