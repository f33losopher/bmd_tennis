from moviepy.editor import *
from shutil import copy2
import moviepy.editor as mp
import moviepy.video.io.ffmpeg_tools as ffmpeg_tools
import os
from PIL import Image, ImageDraw, ImageFont
from project_consts import *
from TennisScore.tennis_score import TennisScore
import time

# Use markers trim unwanted video clips
START_PT = 'Blue'
END_PLAYER1_PT = 'Cyan'
END_PLAYER2_PT = 'Green'
CONTINUE_END = 'Yellow'

tennisScore = TennisScore()

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
        in_file = ROOT_MEDIA_FOLDER + '\\' + timelineItem.GetName()

        start = 0
        end = 0

        print ('sorted_frames: ', sorted_frames)
        print ('GetDuration(): ', timelineItem.GetDuration())
        print ('timelineItem.GetName(): ', timelineItem.GetName())
        
        for frame in sorted_frames:
            print ("    Working on frame: ", frame)
            print ("    markers[frame]: ", markers[frame])
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
    sb_font = ImageFont.truetype(ERBOS_DRACO, 25)
    img = Image.open(BASE_SCOREBOARD)
    clear = img.copy()
    draw = ImageDraw.Draw(clear)

    draw.text((10, 5), get_set_score(PLAYER1), anchor="lm", font=sb_font)
    draw.text((340, 5), get_game_score(PLAYER1), anchor="rm", font=sb_font)

    draw.text((10, 40), get_set_score(PLAYER2), anchor="lm", font=sb_font)
    draw.text((340, 40), get_game_score(PLAYER2), anchor="rm", font=sb_font)

    clear.save(ROOT_MEDIA_FOLDER + '\\score_pt_' + to_alpha_index(clipNo) + '.jpg')

def get_set_score(player):
    score = PLAYERS[player] + " "
    for s in tennisScore.get_match_score()['set'][player]:
        score = score + str(s) + " "

    return score

def get_game_score(player):
    score = str(tennisScore.get_match_score()['game'][player])
    return score

def update_score(markerValue):
    print (tennisScore.get_match_score())
    print ('  ', markerValue)

    if markerValue['color'] == END_PLAYER1_PT:
        print ('My point')
        tennisScore.update_game_score(PLAYER1, PLAYER2)
    elif markerValue['color'] == END_PLAYER2_PT:
        print ('His point')
        tennisScore.update_game_score(PLAYER2, PLAYER1)

def create_clip(in_file, start, end, clipNo, subClip=""):
    print ("create_clip start/FPS: " , start/FPS, " end/FPS: ", end/FPS)

    # videoFile = ROOT_MEDIA_FOLDER + "\\clip_" + to_alpha_index(clipNo) + subClip + '.mp4'
    tempVideo = ROOT_MEDIA_FOLDER + "\\temp.mp4"
    videoFile = ROOT_MEDIA_FOLDER + "\\temp_" + to_alpha_index(clipNo) + subClip + '.mp4'
    tempAudio = ROOT_MEDIA_FOLDER + "\\tempAudio.mp4"

    # clip = VideoFileClip(tempVideo, audio_fps=AUDIO_FPS)
    clip = VideoFileClip(in_file, audio_fps=AUDIO_FPS).subclip(start/FPS, end/FPS)
    scoreboard = mp.ImageClip(ROOT_MEDIA_FOLDER + "\\score_pt_" + to_alpha_index(clipNo) + '.jpg')\
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
    
