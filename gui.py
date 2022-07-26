from python_get_resolve import GetResolve
from ctypes import alignment
import Tkinter
from Tkinter import *

from process_timeline_items import process_timeline
from post_process import create_timeline
from project_consts import *

win = Tkinter.Tk()
win.geometry('600x800')

def processVideos():
    print('Processing videos')
    resolve = app.GetResolve()
    resolve.OpenPage("edit")
    
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()

    # Trim unwanted parts of videos
    timeline = project.GetCurrentTimeline()
    process_timeline(timeline)

    # Time to import all the new clips
    mediaStorage = resolve.GetMediaStorage()
    file_list = mediaStorage.GetFileList(ROOT_MEDIA_FOLDER)
    file_list = filter(lambda k: k.find('temp_') != -1, file_list)
    mediaStorage.AddItemListToMediaPool(file_list)

    create_timeline(resolve)


# Creating initial layout
curRow = 0
Label(win, text='BASE Davinci Path').grid(row=curRow, sticky='w')
entBaseDavinciPath = Entry(win)
entBaseDavinciPath.grid(row=curRow, column=1)
curRow += 1
Label(win, text='Path to videos').grid(row=curRow, sticky='w')
entPathToVids = Entry(win)
entPathToVids.grid(row=curRow, column=1)
curRow += 1
Label(win, text='Game Type').grid(row=curRow, sticky='w')
list_items = StringVar(value=GAME_TYPES)
lbGameType = Listbox(win, listvariable=list_items, height=2)
lbGameType.selection_set(0)
lbGameType.grid(row=curRow, column=1)
curRow += 1
Label(win, text='Player(s) 1').grid(row=curRow, sticky='w')
entPlayer1 = Entry(win)
entPlayer1.grid(row=curRow, column=1)
curRow += 1
Label(win, text='Player(s) 2').grid(row=curRow, sticky='w')
entPlayer2 = Entry(win)
entPlayer2.grid(row=curRow, column=1)
curRow += 1

btnProcess = Button(win, text='Process', command=processVideos).grid(row=curRow, column=1)


# Initialize values for Entry(s)
entBaseDavinciPath.insert(0, BASE_DAVINCI_PATH)
entPathToVids.insert(0, ROOT_MEDIA_FOLDER)
entPlayer1.insert(0, PLAYERS[PLAYER1])
entPlayer2.insert(0, PLAYERS[PLAYER2])


win.mainloop()