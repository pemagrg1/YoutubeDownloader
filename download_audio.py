#date:21-9-17
import pafy
url="https://www.youtube.com/watch?v=mkKXS0FI_L4"
video=pafy.new(url)
audiostreams = video.audiostreams
for a in audiostreams:
    print(a.bitrate, a.extension, a.get_filesize())
    
########to download audio directly 
#audiostreams[1].download()

bestaudio = video.getbestaudio()
bestaudio.bitrate
########To download best audio
#bestaudio.download()

##to see all the streams available
allstreams = video.allstreams
for s in allstreams:
    print(s.mediatype, s.extension, s.quality)
