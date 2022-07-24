BASE_DAVINCI_PATH = "C:\\Users\\fluuc\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\"
BASE_SCOREBOARD = BASE_DAVINCI_PATH + "ScoreBoard.jpg"
ERBOS_DRACO     = BASE_DAVINCI_PATH + "fonts\\erbos-draco-monospaced-nbp-font\\ErbosDraco1StOpenNbpRegular-l5wX.ttf"
SELF_DESTRUCT   = BASE_DAVINCI_PATH + "fonts\\self-destruct-button-bb-font\\SelfdestructbuttonbbBold-0gKR.otf" 

PLAYER1 = 'Player1'
PLAYER2 = 'Player2'

# Update per match
GAME_TYPE = 'Standard'
FPS = 59.940
AUDIO_FPS = 48000
ROOT_MEDIA_FOLDER = "E:\\Felix\\Pictures\\GoPro\\2022-07-22-JamesChan"
PLAYERS = {
    PLAYER1: 'Felix ',
    PLAYER2: 'James '
}

# To initialize a score before the video starts
# Comment out if want to start from 0-0
init_score = {
    'match': {
        'Player1': [6,0],
        'Player2': [1,0]
    },
    'game': {
        'Player1': 0,
        'Player2': 0
    }
}