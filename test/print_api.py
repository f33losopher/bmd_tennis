from python_get_resolve import GetResolve

def print_obj(text, obj):
    print '******************************************************************************************'
    print text, ':', dir(obj)
    print '******************************************************************************************'


resolve = app.GetResolve()
print_obj('Resolve', resolve)

pm = resolve.GetProjectManager()
print_obj('Project Manager', pm)

project = pm.GetCurrentProject()
print_obj('Project', project)

mp = project.GetMediaPool()
print_obj('Media Pool', mp)

timeline = project.GetCurrentTimeline()
print_obj('Timeline', timeline)

currentVideoIteam = timeline.GetCurrentVideoItem()
print_obj('Current Video Item', currentVideoIteam)