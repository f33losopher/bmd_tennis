from python_get_resolve import GetResolve
from ctypes import alignment
import Tkinter
from Tkinter import *

from process_timeline_items import process_timeline
from post_process import create_timeline
from project_consts import *
import logging

win = Tkinter.Tk()
win.geometry('600x800')

logging.basicConfig(level=logging.DEBUG)

def processVideos():
    logging.info('Processing videos with settings...')
    logging.info('BASE_DAVINCI_PATH: ' + CONFIG[BASE_DAVINCI_PATH])
    logging.info('Video Files: ' + CONFIG[ROOT_MEDIA_FOLDER])
    logging.info('GAME_TYPE: ' + CONFIG[GAME_TYPE])
    logging.info('Player(s) 1: ' + PLAYERS[PLAYER1])
    logging.info('Player(s) 2: ' + PLAYERS[PLAYER2])

    resolve = app.GetResolve()
    resolve.OpenPage("edit")
    
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()

    # Trim unwanted parts of videos
    timeline = project.GetCurrentTimeline()
    process_timeline(timeline)

    # Time to import all the new clips
    mediaStorage = resolve.GetMediaStorage()
    file_list = mediaStorage.GetFileList(CONFIG[ROOT_MEDIA_FOLDER])
    file_list = filter(lambda k: k.find('temp_') != -1, file_list)
    mediaStorage.AddItemListToMediaPool(file_list)

    create_timeline(resolve)

def setPlayer(sv, player):
    PLAYERS[player] = sv.get()

def setBasePath(sv):
    CONFIG[BASE_DAVINCI_PATH] = sv.get()

def setVidPath(sv):
    CONFIG[ROOT_MEDIA_FOLDER] = sv.get()

def setGameType(event):
    selected_index = lbGameType.curselection()[0]
    CONFIG[GAME_TYPE] = GAME_TYPES[selected_index]


# Creating initial layout
curRow = 0

Label(win, text='BASE Davinci Path').grid(row=curRow, sticky='w')
svBasePath = StringVar()
svBasePath.trace("w", lambda name, index, mode, svBasePath=svBasePath: setBasePath(svBasePath))
entBaseDavinciPath = Entry(win, textvariable=svBasePath)
entBaseDavinciPath.grid(row=curRow, column=1)
curRow += 1

Label(win, text='Path to videos').grid(row=curRow, sticky='w')
svVidPath = StringVar()
svVidPath.trace("w", lambda name, index, mode, svVidPath=svVidPath: setVidPath(svVidPath))
entPathToVids = Entry(win, textvariable=svVidPath)
entPathToVids.grid(row=curRow, column=1)
curRow += 1

Label(win, text='Game Type').grid(row=curRow, sticky='w')
list_items = StringVar(value=GAME_TYPES)
lbGameType = Listbox(win, listvariable=list_items, height=2)
lbGameType.selection_set(0)
lbGameType.grid(row=curRow, column=1)
lbGameType.bind('<<ListboxSelect>>', setGameType)
curRow += 1

Label(win, text='Player(s) 1').grid(row=curRow, sticky='w')
svPlayer1 = StringVar()
svPlayer1.trace("w", lambda name, index, mode, svPlayer1=svPlayer1: setPlayer(svPlayer1, PLAYER1))
entPlayer1 = Entry(win, textvariable=svPlayer1)
entPlayer1.grid(row=curRow, column=1)
curRow += 1

Label(win, text='Player(s) 2').grid(row=curRow, sticky='w')
svPlayer2 = StringVar()
svPlayer2.trace("w", lambda name, index, mode, svPlayer2=svPlayer2: setPlayer(svPlayer2, PLAYER2))
entPlayer2 = Entry(win, textvariable=svPlayer2)
entPlayer2.grid(row=curRow, column=1)
curRow += 1

btnProcess = Button(win, text='Process', command=processVideos).grid(row=curRow, column=1)

# Initialize values for Entry(s)
entBaseDavinciPath.insert(0, CONFIG[BASE_DAVINCI_PATH])
entPathToVids.insert(0, CONFIG[ROOT_MEDIA_FOLDER])
entPlayer1.insert(0, PLAYERS[PLAYER1])
entPlayer2.insert(0, PLAYERS[PLAYER2])

win.mainloop()