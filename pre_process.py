# Get videos from directory
# Append clips to timeline
from python_get_resolve import GetResolve

from project_consts import *

# Takes clips in media pool and creates 'Timeline'
def create_timeline(resolve):
    pm = resolve.GetProjectManager()
    project = pm.GetCurrentProject()
    mediaPool = project.GetMediaPool()

    mediaPool.CreateEmptyTimeline('Timeline')
    project.SetCurrentTimeline('Timeline')
    mediaClips = mediaPool.GetRootFolder().GetClipList()

    # mediaClips aren't in any order, sort it by 
    # clip.GetName()
    # Remove Timeline
    mediaClips.sort(key=lambda x: x.GetName())
    mediaClips = filter(lambda k: k.GetName() != 'Timeline', mediaClips)
    for clip in mediaClips:
        mediaPool.AppendToTimeline(clip)

resolve = app.GetResolve()
resolve.OpenPage("edit")

mediaStorage = resolve.GetMediaStorage()
mediaStorage.AddItemListToMediaPool(ROOT_MEDIA_FOLDER)

create_timeline(resolve)