# Lindy Hop Moves Videos Maker
This project contains a python script that downloads videos from *youtube* and edit them automatically to get a short video for each lindy move of about 5s.
You can transfert these videos to you smartphone and check you lindy hop moves from everywhere.

## Video Players
* Using the application *AVPlayer* on android you can loop the video until you fully understand the move.
* Using the *VLC player* on android you can visualize in slow motion

## Installation

### Windows installation


 * install python from https://www.python.org/ftp/python/2.7.10/python-2.7.10.amd64.msi
 * install youtube-dl: in command line type : pip install youtube-dl
 * install libav: http://builds.libav.org/windows/nightly-gpl/libav-i686-w64-mingw32-20141125.7z

### Linux (Ubuntu) installation
 
 * sudo pip install youtube-dl
 * sudo apt-get install libav-tools

## Execution

* By default the original youtube videos and the edited videos will be created repectively in the subfolders *edited_videos* and *original_videos*.
* You can change that by editing *download_lindy_moves.py* or you can create local symbolic links with this names that link to folder located somewhere else in the system
* In order to run the script you simply call python download_lindy_moves.py from the command line

##Existing moves

* barrel_roll
* lindy_circle
* lindy_circle_from_open
* swing out from closed
* swing out from open
* texas tommy
* texas tommy2
* texas tommy from closed
* inside turn swingout from open
* inside turn swingout fromclosed
* the nothing
* she goes
* treading water
* he goes
* tuck turn
* sugar push
* kick through
* under arm turn
* send out
* side pass
* she goes he goes
* promenade
* reverse promenade
* cudle
* sweetheart
* belt slide
* lindy hop basket
* tandem charleston
* tandem charleston2
* tandem - Windshield wiper
* tandem - follower turn
* tandem - Push away exit
* Airplane Charleston 
* s-turn into tandem charleston
* scoots

## TODO

Using OpenCV we could improve the quality of the vidoes by running some video stabilization method, background substraction and contrast enhancement.
we could also denoise the sound on some videos.













