# bmd_tennis
Black Magic Design API Scripting for Tennis Videos

In Davinci resolve set the color shortcuts
- Davinci Resolve -> Keyboard Preferences -> Mark
- START_PT = 'Blue'
- END_PLAYER1_PT = 'Cyan'
- END_PLAYER2_PT = 'Green'
- CONTINUE_END = 'Yellow'

Clone to: C:\Users\<USER>\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Comp

Install Python 2.7
https://www.python.org/downloads/release/python-2718/

Install MoviePy
pip install moviepy

In Python command prompt download ffmpeg
>>> import imageio
>>> imageio.plugins.ffmpeg.download()

Update project_consts.py for paths to scoreboard, fonts, media root, etc...

