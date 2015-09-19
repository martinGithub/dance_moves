from __future__ import unicode_literals
import youtube_dl
import os
from datetime import datetime
import os.path
import platform
system=platform.system()

import subprocess
import csv
download_folder = os.path.join('.','original_videos')
target_folder   = os.path.join('.','edited_videos')
rewriteAll=False # set this value to true if you want to recreate existing videos, or simply delet the existing videos in the file explorator



if system=='Windows':
    aviconv_executable='"./libav/avconv"'
elif system=='Linux':
    aviconv_executable='avconv'
elif system=='Darwin':
    aviconv_executable='ffmpeg'
    
else:
    print 'unreckognized OS'
    raise
    
    
generate_gifs=False
movesUrlsDict=dict()

def download_and_cut(videoid,start,end,subfolder,move_name):
    FMT = '%H:%M:%S'
    videofile='%s.avi'%os.path.join(download_folder,videoid)
    tdelta = str(datetime.strptime(end, FMT) - datetime.strptime(start, FMT))
    ydl_opts = {'outtmpl':videofile}
    target_folder_full=os.path.join(target_folder,subfolder)
    if  not(os.path.isdir(target_folder_full)):
        os.makedirs(target_folder_full)
    targetvideofile=os.path.join(target_folder_full,'%s.avi'%move_name)
    targetgiffile=os.path.join(target_folder_full,'%s.gif'%move_name)
    if not(os.path.isfile(targetvideofile)) or rewriteAll:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            if not(os.path.isfile(videofile)):
                ydl.download(['http://www.youtube.com/watch?v=%s'%videoid]) 
          
        command=aviconv_executable+' -i %s -y -c:v libx264 -ss %s -t %s "%s"'%(videofile,start,tdelta,targetvideofile)
        print command
        subprocess.call(command,shell=True)
        if generate_gifs:           
            
            command=aviconv_executable+' -i %s  -y -vsync 1 -pix_fmt rgb24 -r 5 -s 320x240 -ss %s -t %s "%s"'%(videofile,start,tdelta,targetgiffile)
            subprocess.call(command,shell=True)
        
    else:
        print 'video "%s.avi" already created'% move_name
    s=int((datetime.strptime(start, FMT)-datetime(1900,1,1)).total_seconds() ) 
    e=int((datetime.strptime(end, FMT)-datetime(1900,1,1)).total_seconds() ) 
    url='http://www.youtube.com/v/%s?start=%d&end=%d&autoplay=1&loop=1'%(videoid ,s,e)
    url='http://www.infinitelooper.com/?v=%s#/%d;%d'%(videoid ,s,e)
    url='https://www.yourepeat.com/watch/?v=%s&start_at=%d&end_at=%d'%(videoid ,s,e)
    #coul use http://loopthetube.com/#FB1cCoib7xQ&start=41.948&end=46.915
    movesUrlsDict[move_name]=url
    
    

#download_and_cut('HYcuxW5_ilg','00:00:25','00:00:31','level 1/8 counts','arm catch 8 step')
with open('moves.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=str(','), quotechar=str('|'))
    for row in reader:
        download_and_cut(*row)
        
f = open('listmoves.md', 'w')
f.write('##Existing moves\n\n')
for move_name in sorted(movesUrlsDict.keys()):
    f.write('* [%s](%s)\n'%(move_name,movesUrlsDict[move_name]))
f.close()





 


