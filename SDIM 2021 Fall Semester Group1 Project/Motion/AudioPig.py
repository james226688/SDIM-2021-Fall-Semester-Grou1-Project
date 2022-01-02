import vlc

def AudioPig12():
    p = vlc.MediaPlayer("file:///home/pi/Desktop/Main/Slogan/rubbish12.aac")
    p.play()