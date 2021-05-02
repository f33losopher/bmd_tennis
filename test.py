from python_get_resolve import GetResolve

from init_project import create_timeline
from tennis_score import TennisScore

def update_score(markerValue):
    print tennisScore.get_match_score()
    print '  ', markerValue

    if markerValue['color'] == MY_PT:
        print 'My point'
        tennisScore.update_game_score(FELIX, OPP)
    elif markerValue['color'] == OPP_PT:
        print 'His point'
        tennisScore.update_game_score(OPP, FELIX)


MY_PT = 'Blue'
OPP_PT = 'Cyan'
FELIX = 'felix'
OPP = 'opponent'

tennisScore = TennisScore()



resolve = app.GetResolve()
resolve.OpenPage("edit")

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()

create_timeline(resolve)


# TODO How to load a LUT in fusion
# resolve.OpenPage("fusion")
# timeline = project.GetCurrentTimeline()
# timeLineVideos = timeline.GetItemListInTrack('video', 1)
# for timelineItem in timeLineVideos:
#     print timelineItem.GetName()

# Tally Score via markers
# Dark Blue I win point
# Light blue opponent wins point
# timeline = project.GetCurrentTimeline()
# timeLineVideos = timeline.GetItemListInTrack('video', 1)
# for timelineItem in timeLineVideos:
#     markers = timelineItem.GetMarkers()
#     sorted_keys = sorted(markers.keys())
#     for key in sorted_keys:
#         update_score(markers[key])

# Update Scoreboard Macro
# timeline = project.GetCurrentTimeline()
# timeLineVideos = timeline.GetItemListInTrack('video', 1)
# for timelineItem in timeLineVideos:
#     timelineItem.AddFusionComp()
#     fusionComponents = timelineItem.GetFusionCompNameList()
#     print 'fusionComponents:', fusionComponents
#     if len(fusionComponents) > 0:
#         for compName in fusionComponents:
#             comp = timelineItem.GetFusionCompByName(compName)
#             print comp