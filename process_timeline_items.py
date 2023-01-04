from moviepy.editor import *
from shutil import copy2
import moviepy.editor as mp
import moviepy.video.io.ffmpeg_tools as ffmpeg_tools
from PIL import Image, ImageDraw, ImageFont
from project_consts import *
from scoring.score_factory import createTennisScore
from scoring.tennis_score import TennisScore
import time
import logging
import json

# Use markers trim unwanted video clips
START_PT = 'Blue'
END_PLAYER1_PT = 'Cyan'
END_PLAYER2_PT = 'Green'
CONTINUE_END = 'Yellow'

tennisScore = createTennisScore()

def process_timeline(timeline):
    update_scoreboard(1)

    # In the event a point crosses a clip, need to store the first half
    # of the clip to concatenate with the second half
    continue_clip = None

    timelineItems = timeline.GetItemListInTrack('video', 1)
    clipNo = 1
    for timelineItem in timelineItems:
        markers = timelineItem.GetMarkers()
        sorted_frames = sorted(markers.keys())
        in_file = CONFIG[ROOT_MEDIA_FOLDER] + '\\' + timelineItem.GetName()

        start = 0
        end = 0

        logging.debug('sorted_frames: ' + " ".join([str(x) for x in sorted_frames]))
        logging.debug('GetDuration(): ' + str(timelineItem.GetDuration()))
        logging.debug('timelineItem.GetName(): ' + timelineItem.GetName())
        
        for frame in sorted_frames:
            logging.debug("    Working on frame: " + str(frame))
            logging.debug("    markers[frame]: " + json.dumps(markers[frame]))
            if markers[frame]['color'] == START_PT:
                start = frame
            elif markers[frame]['color'] == END_PLAYER1_PT or markers[frame]['color'] == END_PLAYER2_PT:
                # Used to keep ordering of a shot that spans two timelineItems
                # Allows for sorting to be correct, and use same scoreboard for both
                subClip = ""
                if continue_clip:
                    start = 0
                    continue_clip = None
                    subClip = 'a'

                end = frame

                create_clip(in_file, start, end, clipNo, subClip)

                clipNo += 1
                update_score(markers[frame])
                update_scoreboard(clipNo)
            elif markers[frame]['color'] == CONTINUE_END:
                logging.debug("    Continue Clip, using timelineItem.GetDuration(): " + str(timelineItem.GetDuration()))
                create_clip(in_file, start, timelineItem.GetDuration(), clipNo)
                continue_clip = True

# Since sorting is alphabetical, convert the clip number to 3 character letters
# Will handle 1000 clips
def to_alpha_index(num):
    conv =['a','b','c','d','e','f','g','h','i','j','k']
    rtn = []
    while (num > 0):
        idx = num % 10;
        rtn.insert(0, conv[idx])
        num /= 10

    while len(rtn) < 3:
        rtn.insert(0, 'a')

    return "".join(rtn)

def update_scoreboard(clipNo):
    sb_font = ImageFont.truetype(DRAFT, 25)
    img = Image.open(BASE_SCOREBOARD)
    clear = img.copy()
    draw = ImageDraw.Draw(clear)

    draw.text((10, 5), get_set_score(PLAYER1), anchor="lm", font=sb_font)
    draw.text((340, 5), get_game_score(PLAYER1), anchor="rm", font=sb_font)

    draw.text((10, 40), get_set_score(PLAYER2), anchor="lm", font=sb_font)
    draw.text((340, 40), get_game_score(PLAYER2), anchor="rm", font=sb_font)

    clear.save(CONFIG[ROOT_MEDIA_FOLDER] + '\\score_pt_' + to_alpha_index(clipNo) + '.jpg')

def get_set_score(player):
    score = PLAYERS[player] + " "
    for s in tennisScore.get_match_score()['match'][player]:
        score = score + str(s) + " "

    return score

def get_game_score(player):
    score = str(tennisScore.get_match_score()['game'][player])
    return score

def update_score(markerValue):
    logging.debug(tennisScore.get_match_score())
    logging.debug("  " + str(markerValue))

    if markerValue['color'] == END_PLAYER1_PT:
        logging.debug('My point')
        tennisScore.update_game_score(PLAYER1, PLAYER2)
    elif markerValue['color'] == END_PLAYER2_PT:
        logging.debug('His point')
        tennisScore.update_game_score(PLAYER2, PLAYER1)

def create_clip(in_file, start, end, clipNo, subClip=""):
    logging.debug("create_clip start/FPS: "  + str(start/FPS) + " end/FPS: " + str(end/FPS))

    # videoFile = CONFIG[ROOT_MEDIA_FOLDER] + "\\clip_" + to_alpha_index(clipNo) + subClip + '.mp4'
    tempVideo = CONFIG[ROOT_MEDIA_FOLDER] + "\\temp.mp4"
    videoFile = CONFIG[ROOT_MEDIA_FOLDER] + "\\temp_" + to_alpha_index(clipNo) + subClip + '.mp4'
    tempAudio = CONFIG[ROOT_MEDIA_FOLDER] + "\\tempAudio.mp4"

    # clip = VideoFileClip(tempVideo, audio_fps=AUDIO_FPS)
    clip = VideoFileClip(in_file, audio_fps=AUDIO_FPS).subclip(start/FPS, end/FPS)
    scoreboard = mp.ImageClip(CONFIG[ROOT_MEDIA_FOLDER] + "\\score_pt_" + to_alpha_index(clipNo) + '.jpg')\
            .set_duration(clip.duration)\
            .set_pos((10,20))\
            .set_opacity(0.80)

    video = CompositeVideoClip([clip, scoreboard])

    video.write_videofile(videoFile, 
        threads=4,
        fps=FPS,
        audio=True,
        audio_fps=AUDIO_FPS,
        audio_codec='aac',
        temp_audiofile=tempAudio,
        rewrite_audio=False,
        remove_temp=False)
    
    # os.remove(tempVideo)
    os.remove(tempAudio)
    
