from python_get_resolve import GetResolve

from process_timeline_items import process_timeline
from project_consts import *


# Takes clips in media pool and creates 'Timeline'
def create_timeline(resolve):
    pm = resolve.GetProjectManager()
    project = pm.GetCurrentProject()
    mediaPool = project.GetMediaPool()

    mediaPool.CreateEmptyTimeline('Timeline1')
    project.SetCurrentTimeline('Timeline1')
    mediaClips = mediaPool.GetRootFolder().GetClipList()

    # mediaClips aren't in any order, sort it by 
    # clip.GetName()
    # Remove Timeline from list
    mediaClips = filter(lambda k: k.GetName().startswith('temp_'), mediaClips)
    mediaClips.sort(key=lambda k: k.GetName())
    mediaClips = filter(lambda k: k.GetName() != 'Timeline', mediaClips)
    for clip in mediaClips:
        mediaPool.AppendToTimeline(clip)

# resolve = app.GetResolve()
# resolve.OpenPage("edit")


# projectManager = resolve.GetProjectManager()
# project = projectManager.GetCurrentProject()

# # Trim unwanted parts of videos
# timeline = project.GetCurrentTimeline()
# process_timeline(timeline)

# # Time to import all the new clips
# mediaStorage = resolve.GetMediaStorage()
# file_list = mediaStorage.GetFileList(ROOT_MEDIA_FOLDER)
# file_list = filter(lambda k: k.find('temp_') != -1, file_list)
# mediaStorage.AddItemListToMediaPool(file_list)

# create_timeline(resolve)