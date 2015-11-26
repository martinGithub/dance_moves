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

def addSubfolderColumn(listColumnNames,rows):
    valid=False
    while not valid:
        print('\nlist of columns names:')
        for i,name in enumerate(listColumnNames):
            print ('[%d] %s'%(i+1,name))
            
        print ('\n Using the columns number above, specify the rule use to specify \n the subfolder in which each video will be created')
        print (' by writing numbers sperated by "/"')
        listnb=[1,2]        
        str= '/'.join([listColumnNames[i-1] for i in listnb])      
        print (' for example if you type 1/2\n  - the rule will be %s'%str)
        print ('  - and the first video will be stored as follow')    
        row=rows[0]
        s= '/'.join([row[listColumnNames[i-1]] for i in listnb])
        print '      %s/%s.avi'%(s,row['name']  )     

            
        v=raw_input ('your format: ')
        listnb=[int(s) for s in v.split('/')]
        
        print ('Using this format the first few videos will be stored as follows:')
        for k in range(min(5,len(rows))):
            row=rows[k]
            s= '/'.join([row[listColumnNames[i-1]] for i in listnb])
            print '      %s/%s.avi'%(s,row['name']  ) 
        v=raw_input ('is it the right format [y/n]?')
        if (v=='y'):
            valid=True
            
    keys=[listColumnNames[i-1] for i in listnb]
    for row in rows:        
        str= '/'.join([row[k] for k in keys])  
        row['subfolder']=str
    
    
       
    

def download_and_cut(youtubeid,start,end,name,subfolder):
    FMT = '%H:%M:%S'    
    videofile='%s.avi'%os.path.join(download_folder,youtubeid)
    tdelta = str(datetime.strptime(end, FMT) - datetime.strptime(start, FMT))
    ydl_opts = {'outtmpl':videofile}
    target_folder_full=os.path.join(target_folder,subfolder)
    if  not(os.path.isdir(target_folder_full)):
        os.makedirs(target_folder_full)
    targetvideofile=os.path.join(target_folder_full,'%s.avi'%name)
    targetgiffile=os.path.join(target_folder_full,'%s.gif'%name)
    if not(os.path.isfile(targetvideofile)) or rewriteAll:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            if not(os.path.isfile(videofile)):
                ydl.download(['http://www.youtube.com/watch?v=%s'%youtubeid]) 
          
        command=aviconv_executable+' -i %s -y -c:v libx264 -ss %s -t %s "%s"'%(videofile,start,tdelta,targetvideofile)
        print command
        subprocess.call(command,shell=True)
        if generate_gifs:           
            
            command=aviconv_executable+' -i %s  -y -vsync 1 -pix_fmt rgb24 -r 5 -s 320x240 -ss %s -t %s "%s"'%(videofile,start,tdelta,targetgiffile)
            subprocess.call(command,shell=True)
        
    else:
        print ' Video "%s.avi" already created'% name
    s=int((datetime.strptime(start, FMT)-datetime(1900,1,1)).total_seconds() ) 
    e=int((datetime.strptime(end, FMT)-datetime(1900,1,1)).total_seconds() ) 
    url='http://www.youtube.com/v/%s?start=%d&end=%d&autoplay=1&loop=1'%(youtubeid ,s,e)
    url='http://www.infinitelooper.com/?v=%s#/%d;%d'%(youtubeid ,s,e)
    url='https://www.yourepeat.com/watch/?v=%s&start_at=%d&end_at=%d'%(youtubeid ,s,e)
    #coul use http://loopthetube.com/#FB1cCoib7xQ&start=41.948&end=46.915
    #movesUrlsDict[name]={'url':url,'level':level,'beatcount':beatcount}

valid=False

while not valid:
    v=raw_input (' Do you want to download videos from:\n\n'+\
           '  [1] one of the default dance moves list from '+\
           'https://github.com/martinGithub/dance_moves/tree/listmoves\n'+\
           '  [2] another spreadsheet in the csv format available online\n'+\
           '  [3] a list from a google doc spreadsheet \n'+\
           '  [4] a spreasheet in the cvs format available locally on the hard disk \n\n'+\
           ' Make your choice and press enter: ')
    
    valid=v in ['1','2','3','4']


if v=='1' or v=='2':
    print '\n'
    if v=='1':
        valid=False
        
        while not valid:
            v=raw_input ('  [1] lindy hop\n'+\
                         '  [2] salsa\n'+\
                         '  [3] tango\n'+\
                         ' Make your choice and press enter: ')       
        
            valid=v in ['1','2','3']  
        urls=dict()
        urls['1']='https://raw.githubusercontent.com/martinGithub/dance_moves/listmoves/lindy_moves.csv'
        urls['2']='https://raw.githubusercontent.com/martinGithub/dance_moves/listmoves/salsa_moves.csv'
        urls['3']='https://raw.githubusercontent.com/martinGithub/dance_moves/listmoves/tango_moves.csv'
        url= urls[v]
        
    else:
        url =raw_input(' Enter the url of the raw csv file:')
    csvfile = urllib2.urlopen(url)
    reader = csv.reader(csvfile, delimiter=str(','), quotechar=str('|'))
    first=True
    rows=[]
    for row in reader:
        if first:#skip the first line that correspond to the columns names
            column_names=row
            first=False
            continue
        if not row==[]:        
            rows.append(dict(zip(column_names, row)))
        else:
            print 'empty row'  
            
   
elif v=='3':
    spid =raw_input(' Enter the speadsheet id (part of the url following https://docs.google.com/spreadsheets/d/): ')
    url = 'https://spreadsheets.google.com/feeds/list/'+spid+'/default/public/values?alt=json'
    #'https://spreadsheets.google.com/feeds/worksheets/'+spid+'/public/full?alt=json'# to get the list of sheet in the spreadsheet
    print ' Getting data from '  +url      
    
    jsonfile = urllib2.urlopen(url)
    import json       
    jsondata=json.loads(jsonfile.read())
    rows=[]

    for move in jsondata['feed']['entry']: 
        row=dict()
        for k,v in move.iteritems():
            if k.startswith("gsx$"):
                row[k[4:]]=v['$t']   

        rows.append(row)
    column_names=rows[0].keys()
   
elif v=='4':    
    filepath =raw_input(' Enter the path and name of of the csv file (for example: ./exampleMoves.csv )')
    with open(filepath, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=str(','), quotechar=str('|'))
        column_names=reader.next()
        rows=[]
        for row in reader:
            if not row==[]:
                d=dict(zip(column_names, row))
                rows.append(d)
            else:
                print 'empty row'
                
                

            
column_names2=[]
for k in column_names:
    if not k in ['youtubeid','start','end','name']:
        column_names2.append(k)
    
addSubfolderColumn(column_names2,rows)
                
for row in rows:
        download_and_cut(youtubeid=row['youtubeid'],start=row['start'],\
                     end=row['end'],name=row['name'],subfolder=row['subfolder']) 
print '\n Downloaded all moves'
#with  open('listmoves.md', 'r') as f:

    #f.readline()#skipping the first to line that are the header of the table
    #f.readline()
    #lines = f.readlines()
    #for line in lines:
        #columns=line.split('|')
        #s=columns[1]
        #url=s[s.find("(")+1:s.find(")")]
        #name=s[s.find("[")+1:s.find("]")]
        #t=url.split('&')
        #beatcount=columns[2]
        #level=columns[3]
        #videoid=t[0][t[0].find('?v=')+3:]
        #start=str(timedelta(seconds=int(t[1][9:])))
        #end=str(timedelta(seconds=int(t[2][7:])))
        #download_and_cut(videoid, start, end, level, beatcount, name)
        
        


#f = open('listmoves.md', 'w')
#f.write('| Name  | beatcount | level|\n')
#f.write('| --- |:-------:| -----:|\n')
#for name in sorted(movesUrlsDict.keys()):
    #d=movesUrlsDict[name]
    #f.write('| [%s](%s)|%s|%s|\n'%(name,d['url'],d['beatcount'],d['level']))
#f.close()





 


