# 2015.06.13 07:09:19 Jordan Daylight Time
#Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/TSTube/resources/tube_resolver/default.py
import YouTubePlayer
player = YouTubePlayer.YouTubePlayer()

def setparams(params):
    print 'default8pparams', params
    videoparams, error = player.playVideo(params)
    print 'default8videoparams', videoparams
    return (videoparams, error)
# okay decompyling D:\TSTube\TSTube\resources\tube_resolver\default.pyo 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.06.13 07:09:19 Jordan Daylight Time
