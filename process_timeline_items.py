from moviepy.editor import *
from shutil import copy2
import moviepy.editor as mp
import moviepy.video.io.ffmpeg_tools as ffmpeg_tools
import os
from PIL import Image, ImageDraw, ImageFont
from project_consts import *
from tennis_score import TennisScore
import time

# Use markers trim unwanted video clips
START_PT = 'Blue'
END_MY_PT = 'Cyan'
END_OPP_PT = 'Green'
CONTINUE_END = 'Yellow'
FELIX = 'felix'
OPP = 'opponent'

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

        print 'sorted_frames: ', sorted_frames
        print 'GetDuration(): ', timelineItem.GetDuration()
        print 'timelineItem.GetName(): ', timelineItem.GetName()
        
        for frame in sorted_frames:
            print "    Working on frame: ", frame
            print "    markers[frame]: ", markers[frame]
            if markers[frame]['color'] == START_PT:
                start = frame
            elif markers[frame]['color'] == END_MY_PT or markers[frame]['color'] == END_OPP_PT:
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
    # TODO Make spacing better for scoreboard
    sb_font = ImageFont.truetype(ERBOS_DRACO, 25)
    img = Image.open(BASE_SCOREBOARD)
    clear = img.copy()
    draw = ImageDraw.Draw(clear)
    draw.text((10, 5), FELIX + " " + str(tennisScore.get_match_score()['game'][FELIX]), anchor="lm", font=sb_font)
    draw.text((10, 40), OPP + "   " + str(tennisScore.get_match_score()['game'][OPP]), anchor="lm", font=sb_font)
    clear.save(ROOT_MEDIA_FOLDER + '\\score_pt_' + to_alpha_index(clipNo) + '.jpg')


def update_score(markerValue):
    print tennisScore.get_match_score()
    print '  ', markerValue

    if markerValue['color'] == END_MY_PT:
        print 'My point'
        tennisScore.update_game_score(FELIX, OPP)
    elif markerValue['color'] == END_OPP_PT:
        print 'His point'
        tennisScore.update_game_score(OPP, FELIX)

def create_clip(in_file, start, end, clipNo, subClip=""):
    print "create_clip start/FPS: " , start/FPS, " end/FPS: ", end/FPS

    videoFile = ROOT_MEDIA_FOLDER + "\\clip_" + to_alpha_index(clipNo) + subClip+ '.mp4'
    cmd = "ffmpeg -i \"{0}\" -ss {1} -to {2} -async 1 \"{3}\"".format(
        in_file, 
        time.strftime('%H:%M:%S', time.gmtime(start/FPS)), 
        time.strftime('%H:%M:%S', time.gmtime(end/FPS)), 
        videoFile)

    print "System command: ", cmd
    os.system(cmd)

    # clip = VideoFileClip(in_file).subclip(start/FPS, end/FPS)

    # scoreboard = mp.ImageClip(ROOT_MEDIA_FOLDER + "\\score_pt_" + to_alpha_index(clipNo) + '.jpg')\
    #         .set_duration(clip.duration)\
    #         .set_pos((10,20))

    # video = CompositeVideoClip([clip, scoreboard])

    # videoFile = ROOT_MEDIA_FOLDER + "\\clip_" + to_alpha_index(clipNo) + subClip+ '.mp4'
    # tempAudio = ROOT_MEDIA_FOLDER + "\\temp_audio_" + to_alpha_index(clipNo) + subClip + ".mp3"
    # tempVideo = ROOT_MEDIA_FOLDER + "\\temp_video_" + to_alpha_index(clipNo) + subClip + ".mp4"
    # video.write_videofile(videoFile, 
    #     threads=4,
    #     fps=FPS,
    #     remove_temp=False,
    #     temp_audiofile=tempAudio)
    
    # Bug with MoviePy using ffmpeg. Need to
    # Save off the sound file
    # Manually use ffmpeg to merge the video clip with the sound
    # command = 'ffmpeg -y -i ' + videoFile + ' -i ' + tempAudio + ' -c:v copy -c:a aac -shortest ' + tempVideo
    # ffmpeg_tools.ffmpeg_merge_video_audio(videoFile, tempAudio, tempVideo,
    #     vcodec='copy',
    #     acodec='aac')

    # os.remove(videoFile)
    # os.remove(tempAudio)
