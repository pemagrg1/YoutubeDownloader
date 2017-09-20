'''
Author: Pema Gurung
Date: 21-9-17
'''

import pafy
#enter the url of the video you want to download
url="https://www.youtube.com/watch?v=mkKXS0FI_L4"
video=pafy.new(url)
#print(video.title)
#print(video.rating)
#print(video.viewcount, video.author, video.length)
#print(video.duration, video.likes, video.dislikes)
#print(video.description)

##to see the list of available streams for a video
streams=video.streams
for s in streams:
    print(s)
##To see all the formats
for s in streams:
    print(s.resolution,s.extension, s.get_filesize(), s.url)

##get best resolution of the video
best=video.getbest()
print(best.resolution,best.extension)

###best resolution in required format[give your req format in "preftype"]
best = video.getbest(preftype="webm")
print(best.resolution, best.extension)
#get url for download
print(best.url)
#download video
#best.download(quiet=False) #this will download directly 
#if you want to specify a particular path for the video
filename = best.download(filepath="/home/pema/Desktop/")
filename = best.download(filepath="/home/pema/Desktop/vid." + best.extension)
