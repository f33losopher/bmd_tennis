from project_consts import GAME_TYPE
from project_consts import CONFIG
from tennis_score import TennisScore
from standard_score import StandardScore

def createTennisScore():
    if (CONFIG[GAME_TYPE] == 'Standard'):
        return StandardScore()
