from __future__ import unicode_literals
import youtube_dl
import os
from datetime import datetime
import os.path

download_folder = os.path.join('.','original_videos')
target_folder   = os.path.join('.','edited_videos')
rewriteAll=False # set this value to true if you want to recreate existing videos, or simply delet the existing videos in the file explorator

def download_and_cut(videoid,start,end,subfolder,move_name):
    FMT = '%H:%M:%S'
    videofile='%s.avi'%os.path.join(download_folder,videoid)
    tdelta = str(datetime.strptime(end, FMT) - datetime.strptime(start, FMT))
    ydl_opts = {'outtmpl':videofile}
    target_folder_full=os.path.join(target_folder,subfolder)
    if  not(os.path.isdir(target_folder_full)):
        os.makedirs(target_folder_full)
    targetvideofile=os.path.join(target_folder_full,'%s.avi'%move_name)
    if not(os.path.isfile(targetvideofile)) or rewriteAll:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            if not(os.path.isfile(videofile)):
                ydl.download(['http://www.youtube.com/watch?v=%s'%videoid])    
        command='avconv -i %s -c:v libx264 -ss %s -t %s "%s"'%(videofile,start,tdelta,targetvideofile)
        print command
        os.system(command)
    else:
        print 'video "%s.avi" already created'% move_name

download_and_cut('mLkkUDXE65Y','00:00:21','00:00:26','level 1/6 counts','barrel_roll')
download_and_cut('CF0KIsQR6A4','00:02:25','00:02:30','level 1/8 counts','lindy_circle' )
download_and_cut('pnWF9Lb7QaU','00:01:27','00:01:34','level 1/8 counts','lindy_circle_from_open' ) 
download_and_cut('YSnlHV_GCA0','00:01:00','00:01:04','level 1/8 counts','swing out from closed')
download_and_cut('YSnlHV_GCA0','00:01:07','00:01:11','level 1/8 counts','swing out from open')
download_and_cut('YSnlHV_GCA0','00:01:24','00:01:29','level 1/8 counts','texas tommy' )
download_and_cut('U9PJO-Keu-M','00:01:04','00:01:11','level 1/8 counts','texas tommy2')
download_and_cut('GzyQldsVDb0','00:00:15','00:00:21','level 1/8 counts','texas tommy from closed')
download_and_cut('9XkYi-s5YWw','00:01:41','00:01:47','level 1/8 counts','inside turn swingout from open' )
download_and_cut('TlUwWjbyeN0','00:00:29','00:00:33','level 1/8 counts','inside turn swingout fromclosed' )
download_and_cut('rfUdoXikhMc','00:00:17','00:00:21','level 1/8 counts','the nothing')
download_and_cut('rbxqTcKj2U8','00:00:21','00:00:27','level 1/8 counts','she goes')
download_and_cut('rbxqTcKj2U8','00:00:33','00:00:39','level 1/8 counts','treading water' )
download_and_cut('CF0KIsQR6A4','00:01:39','00:01:44','level 1/8 counts','he goes')
download_and_cut('uDARWpHsF-Y','00:02:30','00:02:34','level 1/6 counts','tuck turn' )
download_and_cut('KJGrzuTPj2o','00:01:32','00:01:37','level 1/6 counts','sugar push' )
download_and_cut('dPjS6QVqltk','00:01:47','00:02:00','level 1/8 counts','kick through')
download_and_cut('uDARWpHsF-Y','00:01:57','00:02:01','level 1/6 counts','under arm turn')
download_and_cut('EHubFEiS4tk','00:05:05','00:05:10','level 1/6 counts','send out')
download_and_cut('bv_Xsyy3uAY','00:00:58','00:01:04','level 1/6 counts','side pass')
download_and_cut('91FZSR9wQKk','00:00:55','00:01:01','level 1/6 counts','she goes he goes')
download_and_cut('CF0KIsQR6A4','00:01:49','00:01:54','level 1/8 counts','promenade')
download_and_cut('CF0KIsQR6A4','00:01:56','00:02:01','level 1/8 counts','reverse promenade')
download_and_cut('USXmK5QXwCc','00:02:19','00:02:26','level 1/6 counts','cudle')
download_and_cut('cjQIwvnfI3Q','00:02:21','00:02:29','level 1/6 counts','sweetheart')
download_and_cut('USXmK5QXwCc','00:00:56','00:01:00','level 1/6 counts','belt slide')
download_and_cut('yR-H2MKsOTM','00:02:28','00:02:36','level 1/8 counts','lindy hop basket')
download_and_cut('hlkp-XMeQOM','00:01:05','00:01:22','level 1/8 counts','tandem charleston')
download_and_cut('jU0NWSu2x0o','00:00:28','00:00:37','level 1/8 counts','tandem charleston2')
download_and_cut('jU0NWSu2x0o','00:00:35','00:00:46','level 1/8 counts','tandem - Windshield wiper')
download_and_cut('jU0NWSu2x0o','00:00:49','00:00:57','level 1/8 counts','tandem - follower turn')
download_and_cut('jU0NWSu2x0o','00:00:59','00:01:07','level 1/8 counts','tandem - Push away exit')
download_and_cut('-eQaOZXJdkA','00:00:19','00:00:30','level 1/8 counts','Airplane Charleston ')
download_and_cut('5MEfGPNf3nE','00:00:33','00:00:43','level 1/8 counts','s-turn into tandem charleston')
download_and_cut('0nbTtgY-aQ8','00:00:31','00:00:41','level 1/8 counts','scoots')





 


