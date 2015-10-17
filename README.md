
# Dance Moves Videos Maker
This project contains a python script that downloads videos from *youtube* and edit them automatically to create on your computer a short video file of about 5s for each Dance move listed [here](http://martingithub.github.io/dance_moves/) or in your own playlist written in google doc spreadsheet (see here [here](http://martingithub.github.io/dance_moves/newplaylist.html)). You can transfer these video files to your smartphone and watch them whenever you forgot the details of a move.



## Mobile Video Players 

* Using the application [AVPlayer](https://play.google.com/store/apps/details?id=com.vnd.mplayer.neon.noad&hl=en) on android you can loop the video until you fully understand the move.
* Using the *VLC player* on android you can visualize a video in slow motion.

##Existing moves

You can consult the list of moves [here](http://martingithub.github.io/dance_moves/). 

If you want to download other moves you can create you own list of moves 
* using a google doc spreadsheet (as explained [here](http://martingithub.github.io/dance_moves/newplaylist.html)). The advantage is that you can then see the videos directly in the player.
* locally in a spreadsheet in the  cvs format (comma separated values) that needs to be structured like exampleMoves.cvs in the project folder once your decompressed the zip file of the project.

## Installation

### Windows installation

* install python from https://www.python.org/ftp/python/2.7.10/python-2.7.10.amd64.msi.
* download the zip file of the project [here] (https://github.com/martinGithub/dance_moves/archive/master.zip) an decompress it 
* double click on *setup.py*, this will install automatically the dependencies (*youtube-dl* and *libav*). 

### Mac OS installation

* install python from https://www.python.org/ftp/python/2.7.10/python-2.7.10-macosx10.6.pkg (note that recent version of Mac OS X should comes with Python 2.7 out of the box)
* download the zip file of the project [here] (https://github.com/martinGithub/dance_moves/archive/master.zip) an decompress it 
* in the terminal, move in the decompressed folder using the *cd* command (for example *cd ~/Downloads/dance_moves-master* if that where it has been decompressed) and type *sudo python setup.py*, this will install automatically the dependencies (*youtube-dl* and *ffmpeg*)
* you can now select *PythonLauncher* as the default application to open python scripts  through the *finder Info window*

### Linux (Ubuntu) installation 

* download the zip file of the project [here] (https://github.com/martinGithub/dance_moves/archive/master.zip) an decompress it 
* in the terminal, move in the decompressed folder and type *sudo python setup.py*, this will install automatically the dependencies (*youtube-dl* and *libav*)

## Execution


In order to run the script you can either 

*  double-click on *download_dance_moves.py* in Windows and Mac OS (assuming you have setup PythonLauncher as the default application for python scripts in Mac OS) 

* open a terminal on Mac OS or Linux, or the [command prompt](http://www.7tutorials.com/7-ways-launch-command-prompt-windows-7-windows) in Windows, then move to the decompressed folder using the *cd* command and then call *python download_dance_moves.py*. 


By default the original youtube videos and the edited videos will be created respectively in the subfolders *edited_videos* and *original_videos*. You can change that by editing *download_dance_moves.py* or you can create local symbolic links with this names that link to folder located somewhere else in the system.

## TODO
Using OpenCV we could improve the quality of the videos by running some video stabilisation method, background substraction and contrast enhancement.
We could also denoise the sound on some videos.
We could use avconvert when executed on Mac OS (from OS X Lion) to avoid the installation of libav or ffmpeg.








