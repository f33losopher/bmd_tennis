from python_get_resolve import GetResolve

from process_timeline_items import process_timeline
from project_consts import *

resolve = app.GetResolve()
resolve.OpenPage("edit")


projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()

# Trim unwanted parts of videos
timeline = project.GetCurrentTimeline()
process_timeline(timeline)
