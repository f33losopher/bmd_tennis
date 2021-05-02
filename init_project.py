# Takes clips in media pool and creates 'Timeline'
def create_timeline(resolve):
    pm = resolve.GetProjectManager()
    project = pm.GetCurrentProject()
    mediaPool = project.GetMediaPool()

    mediaPool.CreateEmptyTimeline('Timeline')
    project.SetCurrentTimeline('Timeline')
    mediaClips = mediaPool.GetRootFolder().GetClipList()
    for clip in mediaClips:
        mediaPool.AppendToTimeline(clip)
