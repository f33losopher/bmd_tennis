from python_get_resolve import GetResolve

from init_project import create_timeline
from process_timeline_items import process_timeline

ROOT_MEDIA_FOLDER = "C:\\Users\\Felix\\Pictures\\GoPro\\2021-04-10_OneHandBH\\HERO5 Black 1"

resolve = app.GetResolve()
resolve.OpenPage("edit")

mediaStorage = resolve.GetMediaStorage()
print mediaStorage.GetMountedVolumeList()

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()

# create_timeline(resolve)


# TODO How to load a LUT in fusion
# resolve.OpenPage("fusion")
# timeline = project.GetCurrentTimeline()
# timeLineVideos = timeline.GetItemListInTrack('video', 1)
# for timelineItem in timeLineVideos:
#     print timelineItem.GetName()


# Trim unwanted parts of videos
timeline = project.GetCurrentTimeline()
process_timeline(ROOT_MEDIA_FOLDER, timeline)


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