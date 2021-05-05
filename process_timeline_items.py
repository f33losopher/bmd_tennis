from moviepy.editor import *

# Use markers trim unwanted video clips
START_PT = 'Blue'
END_MY_PT = 'Cyan'
END_OPP_PT = 'Green'
FELIX = 'felix'
OPP = 'opponent'

def process_timeline(ROOT_MEDIA_FOLDER, timeline):
    timelineItems = timeline.GetItemListInTrack('video', 1)
    for timelineItem in timelineItems:
        print 'timelineItem: ', timelineItem.GetName()
        markers = timelineItem.GetMarkers()
        sorted_frames = sorted(markers.keys())
        in_file = ROOT_MEDIA_FOLDER + '\\' + timelineItem.GetName()

        FPS = 60
        clipNo = 1
        start = 0
        for frame in sorted_frames:
            print 'start: ', start, ' end: ', frame/FPS, ' clipNo: ', clipNo
            clip = VideoFileClip(in_file).subclip(start, frame/FPS)
            video = CompositeVideoClip([clip])
            video.write_videofile(ROOT_MEDIA_FOLDER + "\\clip_" + str(clipNo) + '.mp4')

            start = frame/FPS
            clipNo += 1
        