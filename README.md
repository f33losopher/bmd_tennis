# bmd_tennis
Black Magic Design API Scripting for Tennis Videos

Best BMD API: https://diop.github.io/davinci-resolve-api/#/

# Environment Setup

In Davinci Resolve the marker colors represent
- Start of Point= 'Blue'
- Player 1 wins point = 'Cyan'
- Player 2 wins point = 'Green'
- Continue Clip = 'Yellow'

Continue clip is used when a point crosses a video clip boundary. Use the Blue marker as usual, end the clip with Yellow, and then in the next clip mark the winning point as normal

I set the following shortcuts in Davinci Resolve
- Davinci Resolve -> Keyboard Preferences -> Mark
- m => 'Blue'
- 1 => 'Cyan'
- 2 => 'Green'
- 3 => 'Yellow'

Clone to: C:\Users\<USER>\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Comp

Install Python 2.7
https://www.python.org/downloads/release/python-2718/

Install MoviePy
pip install moviepy

In Python command prompt download ffmpeg
>>> import imageio
>>> imageio.plugins.ffmpeg.download()

# Run Program

