
import urllib
import os
import subprocess
import platform
system=platform.system()
dowloadProjectZip=False

if system=='Windows':
    
    if dowloadProjectZip:
        targetFolder=os.path.join(os.getcwd(),'lindy_hop_moves')
        os.mkdir(targetFolder)
        print 'downloading lindy_hop_moves',
        urllib.urlretrieve ("https://github.com/martinGithub/lindy_hop_moves/archive/master.zip",os.path.join(tempDownloadsFolder,"lindy_hop_moves.zip"))
        print 'done'
        subprocess.call(' "C:\\Program Files\\7-Zip\\7z.exe" e "%s" lindy_hop_moves-master\\* -o"%s" '% \
                        (os.path.join(tempDownloadsFolder,"lindy_hop_moves.zip"),\
                         targetFolder),shell=True)
        os.remove(os.path.join(tempDownloadsFolder,"lindy_hop_moves.zip"))
    else:
        targetFolder=os.getcwd()

    tempDownloadsFolder=os.path.join(targetFolder,'temporary_downloads')
    os.mkdir(tempDownloadsFolder)
    import pip
    
    pip.main(['install', 'youtube-dl'])
    
    print 'downloading 7z',
    urllib.urlretrieve ("http://www.7-zip.org/a/7z920-x64.msi", os.path.join(tempDownloadsFolder,"7z920-x64.msi"))
    print 'done'
    
    print 'downloading libav',
    urllib.urlretrieve ("http://builds.libav.org/windows/release-gpl/libav-11.3-win64.7z", os.path.join(tempDownloadsFolder,"libav-11.3-win64.7z"))
    print 'done'

    print 'installing 7z'
   
    subprocess.call(os.path.join(tempDownloadsFolder,"7z920-x64.msi"),shell=True)
    
    print 'decompressing libav in a local subfolder'
    subprocess.call(' "C:\\Program Files\\7-Zip\\7z.exe" e "%s" win64\\usr\\bin\\* -o"%s" '% \
    (os.path.join(tempDownloadsFolder,"libav-11.3-win64.7z"),\
     os.path.join(targetFolder,'libav')),shell=True)
    
    print 'deleteing temporary download files',   
    
    os.remove(os.path.join(tempDownloadsFolder,"libav-11.3-win64.7z")) 
    os.remove(os.path.join(tempDownloadsFolder,"7z920-x64.msi")) 
    print 'done'    
    os.rmdir(tempDownloadsFolder)
    print 'INSTALLATION FINISHED :)'
    
elif system=='Darwin':
    print 'installing pip'
    # problem : installing brew requires xcode to be installed :(
    #subprocess.call('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"',shell=True)
    #subprocess.call('brew install python',shell=True)
    #subprocess.call('sudo easy_install pip',shell=True)# seems like this does not work on some machines
    urllib.urlretrieve ("https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py","get-pip.py")
    subprocess.call('sudo python get-pip.py',shell=True)
    os.remove('get-pip.py') 
    print 'done'  
    print 'installing youtube-dl'
    subprocess.call('sudo pip install youtube-dl',shell=True)
    print 'done'

    # installing libav seem complex on mac :( as it requires brew that itelf requiers xcode so we use ffmpeg instead
    #subprocess.call('brew install libav',shell=True)
    
    print 'installing ffmpeg'
    #urllib.urlretrieve ("http://evermeet.cx/ffmpeg/ffmpeg-2.8.7z","ffmpeg-2.8.7z")
    urllib.urlretrieve ("http://ffmpegmac.net/resources/SnowLeopard_Lion_Mountain_Lion_Mavericks_Yosemite_09.08.2015.zip","ffmpeg.zip")
    import zipfile
    fh = open('ffmpeg.zip', 'rb')
    z = zipfile.ZipFile(fh)
    z.extract('ffmpeg', '.')
    fh.close()   
    os.remove('ffmpeg.zip') 
    subprocess.call('chmod +x ffmpeg',shell=True)
    print 'done'
    print 'INSTALLATION FINISHED :)'
    
    
    
    
    
elif system=='Linux':
    subprocess.call('sudo pip install youtube-dl',shell=True)
    subprocess.call('sudo apt-get install libav-tools',shell=True)
    print 'INSTALLATION FINISHED :)'
    #if one wants to use ffmpeg instead
    #sudo add-apt-repository ppa:mc3man/trusty-media
    #sudo apt-get update
    #sudo apt-get dist-upgrade
    #sudo apt-get ffmpeg    
    
else:
    print 'unreckognize sytem'
    raise
