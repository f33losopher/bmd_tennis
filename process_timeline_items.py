from moviepy.editor import *
import moviepy.editor as mp
from PIL import Image, ImageDraw
from project_consts import *
from tennis_score import TennisScore

# Use markers trim unwanted video clips
START_PT = 'Blue'
END_MY_PT = 'Cyan'
END_OPP_PT = 'Green'
FELIX = 'felix'
OPP = 'opponent'
FPS = 60

tennisScore = TennisScore()

def process_timeline(timeline):
    update_scoreboard(1)

    timelineItems = timeline.GetItemListInTrack('video', 1)
    for timelineItem in timelineItems:
        markers = timelineItem.GetMarkers()
        sorted_frames = sorted(markers.keys())
        in_file = ROOT_MEDIA_FOLDER + '\\' + timelineItem.GetName()

        clipNo = 1
        start = 0
        end = 0
        for frame in sorted_frames:
            print markers[frame]
            if markers[frame]['color'] == START_PT:
                start = frame
            else:
                end = frame
                clip = VideoFileClip(in_file).subclip(start/FPS, end/FPS)
                scoreboard = mp.ImageClip(ROOT_MEDIA_FOLDER + "\\score_pt_" + str(clipNo) + '.jpg')\
                        .set_duration(clip.duration)\
                        .set_pos((10,20))
                video = CompositeVideoClip([clip, scoreboard])
                video.write_videofile(ROOT_MEDIA_FOLDER + "\\clip_" + str(clipNo) + '.mp4')

                clipNo += 1
                update_score(markers[frame])
                update_scoreboard(clipNo)


        print 'sorted_frames: ', sorted_frames
        print 'GetDuration(): ', timelineItem.GetDuration()
        

def update_scoreboard(clipNo):
    img = Image.open(BASE_SCOREBOARD)
    clear = img.copy()
    draw = ImageDraw.Draw(clear)
    draw.text((10, 10), FELIX + " " + str(tennisScore.get_match_score()['game'][FELIX]))
    draw.text((10, 20), OPP + " " + str(tennisScore.get_match_score()['game'][OPP]))
    clear.save(ROOT_MEDIA_FOLDER + '\\score_pt_' + str(clipNo) + '.jpg')


def update_score(markerValue):
    print tennisScore.get_match_score()
    print '  ', markerValue

    if markerValue['color'] == END_MY_PT:
        print 'My point'
        tennisScore.update_game_score(FELIX, OPP)
    elif markerValue['color'] == END_OPP_PT:
        print 'His point'
        tennisScore.update_game_score(OPP, FELIX)
