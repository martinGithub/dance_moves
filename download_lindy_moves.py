from __future__ import unicode_literals
import youtube_dl
import os
from datetime import datetime,timedelta
import os.path
import platform
system=platform.system()
import urllib2
import subprocess
import csv
import sys
download_folder = os.path.join('.','original_videos')
target_folder   = os.path.join('.','edited_videos')
rewriteAll=False # set this value to true if you want to recreate existing videos, or simply delet the existing videos in the file explorator



if system=='Windows':
    aviconv_executable='"./libav/avconv"'
elif system=='Linux':
    aviconv_executable='avconv'
elif system=='Darwin':
    aviconv_executable='./ffmpeg'
    
else:
    print 'unreckognized OS'
    raise
    
    
generate_gifs=False
movesUrlsDict=dict()

def download_and_cut(videoid,start,end,level,beatcount,move_name):
    FMT = '%H:%M:%S'
    subfolder=level+'/'+beatcount
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
        print ' Video "%s.avi" already created'% move_name
    s=int((datetime.strptime(start, FMT)-datetime(1900,1,1)).total_seconds() ) 
    e=int((datetime.strptime(end, FMT)-datetime(1900,1,1)).total_seconds() ) 
    url='http://www.youtube.com/v/%s?start=%d&end=%d&autoplay=1&loop=1'%(videoid ,s,e)
    url='http://www.infinitelooper.com/?v=%s#/%d;%d'%(videoid ,s,e)
    url='https://www.yourepeat.com/watch/?v=%s&start_at=%d&end_at=%d'%(videoid ,s,e)
    #coul use http://loopthetube.com/#FB1cCoib7xQ&start=41.948&end=46.915
    movesUrlsDict[move_name]={'url':url,'level':level,'beatcount':beatcount}

valid=False

while not valid:
    v=raw_input (' Do you want to download videos from:\n\n'+\
           '  [1] the default list from '+\
           'https://raw.githubusercontent.com/martinGithub/lindy_hop_moves/listmoves/lindy_moves.csv\n'+\
           '  [2] another spreadsheet in the csv format available online\n'+\
           '  [3] a list from a google doc spreadsheet \n'+\
           '  [4] a spreasheet in the cvs format available locally on the harddisk \n\n'+\
           ' Make your choice and press enter: ')
    
    valid=v in ['1','2','3','4']


if v=='1' or v=='2':
    if v=='1':
        url = 'https://raw.githubusercontent.com/martinGithub/lindy_hop_moves/listmoves/lindy_moves.csv'
    else:
        url =raw_input('enter the url of the raw csv file')
    csvfile = urllib2.urlopen(url)
    reader = csv.reader(csvfile, delimiter=str(','), quotechar=str('|'))
    first=True
    for row in reader:
        if first:#skip the first line that correspond to the columns names
            first=False
            continue
        
        if not row==[]:
            download_and_cut(*row)
        else:
            print 'empty row'         
elif v=='3':
    spid =raw_input(' Enter the speadsheet id (part of the url following https://docs.google.com/spreadsheets/d/): ')
    url = 'https://spreadsheets.google.com/feeds/list/'+spid+'/default/public/values?alt=json'
    print ' Getting data from '  +url 
        
    
    jsonfile = urllib2.urlopen(url)
    import json       
    jsondata=json.loads(jsonfile.read())
    for move in jsondata['feed']['entry']:    
        download_and_cut(videoid=move['gsx$youtubeid']['$t'],
                         start=move['gsx$start']['$t'], 
                         end=move['gsx$end']['$t'], 
                         level=move['gsx$level']['$t'],
                         beatcount=move['gsx$beatcount']['$t'],
                         move_name=move['gsx$name']['$t'])
   
elif v=='4':    
    filepath =raw_input(' Enter the path and name of of the csv file (for example: ./exampleMoves.csv )')
    with open(filepath, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=str(','), quotechar=str('|'))
        column_names=reader.next()
        column_names[column_names.index('name')]='move_name'
        column_names[column_names.index('youtubeid')]='videoid'
        for row in reader:
            if not row==[]:
                d=dict(zip(column_names, row))
                d2=dict()
                for k in 'videoid','start','end','level','beatcount','move_name':
                    d2[k]=d[k]                
                download_and_cut(**d2)
            else:
                print 'empty row'
            
#with  open('listmoves.md', 'r') as f:

    #f.readline()#skipping the first to line that are the header of the table
    #f.readline()
    #lines = f.readlines()
    #for line in lines:
        #columns=line.split('|')
        #s=columns[1]
        #url=s[s.find("(")+1:s.find(")")]
        #move_name=s[s.find("[")+1:s.find("]")]
        #t=url.split('&')
        #beatcount=columns[2]
        #level=columns[3]
        #videoid=t[0][t[0].find('?v=')+3:]
        #start=str(timedelta(seconds=int(t[1][9:])))
        #end=str(timedelta(seconds=int(t[2][7:])))
        #download_and_cut(videoid, start, end, level, beatcount, move_name)
        
        


#f = open('listmoves.md', 'w')
#f.write('| Name  | beatcount | level|\n')
#f.write('| --- |:-------:| -----:|\n')
#for move_name in sorted(movesUrlsDict.keys()):
    #d=movesUrlsDict[move_name]
    #f.write('| [%s](%s)|%s|%s|\n'%(move_name,d['url'],d['beatcount'],d['level']))
#f.close()





 


