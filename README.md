# Lindy Hop Moves Videos Maker
This project contains a python script that downloads videos from *youtube* and edit them automatically to create on your computer a short video file of about 5s for each lindy move listed below. You can transfert these video files to your smartphone and watch them whenever you forgot the details of a move.

## Mobile Video Players 

* Using the application *AVPlayer* on android you can loop the video until you fully understand the move.
* Using the *VLC player* on android you can visualize a video in slow motion

##Existing moves

* [barrel roll](http://www.youtube.com/v/mLkkUDXE65Y?start=21&end=26&autoplay=1&loop=1)
* [lindy circle](http://www.youtube.com/v/CF0KIsQR6A4?start=145&end=150&autoplay=1&loop=1)
* [lindy circle from open](http://www.youtube.com/v/pnWF9Lb7QaU?start=87&end=94&autoplay=1&loop=1)
* [swing out from closed](http://www.youtube.com/v/YSnlHV_GCA0?start=60&end=64&autoplay=1&loop=1)
* [swing out from open](http://www.youtube.com/v/YSnlHV_GCA0?start=67&end=71&autoplay=1&loop=1)
* [texas tommy](http://www.youtube.com/v/YSnlHV_GCA0?start=84&end=89&autoplay=1&loop=1)
* [texas tommy2](http://www.youtube.com/v/U9PJO-Keu-M?start=64&end=71&autoplay=1&loop=1)
* [texas tommy from closed](http://www.youtube.com/v/GzyQldsVDb0?start=15&end=21&autoplay=1&loop=1)
* [inside turn swingout from open](http://www.youtube.com/v/9XkYi-s5YWw?start=101&end=107&autoplay=1&loop=1)
* [inside turn swingout fromclosed](http://www.youtube.com/v/TlUwWjbyeN0?start=29&end=33&autoplay=1&loop=1)
* [the nothing](http://www.youtube.com/v/rfUdoXikhMc?start=17&end=21&autoplay=1&loop=1)
* [she goes](http://www.youtube.com/v/rbxqTcKj2U8?start=21&end=27&autoplay=1&loop=1)
* [treading water](http://www.youtube.com/v/rbxqTcKj2U8?start=33&end=39&autoplay=1&loop=1)
* [he goes](http://www.youtube.com/v/CF0KIsQR6A4?start=99&end=104&autoplay=1&loop=1)
* [tuck turn](http://www.youtube.com/v/uDARWpHsF-Y?start=150&end=154&autoplay=1&loop=1)
* [sugar push](http://www.youtube.com/v/KJGrzuTPj2o?start=92&end=97&autoplay=1&loop=1)
* [kick through](http://www.youtube.com/v/dPjS6QVqltk?start=107&end=120&autoplay=1&loop=1)
* [under arm turn](http://www.youtube.com/v/uDARWpHsF-Y?start=117&end=121&autoplay=1&loop=1)
* [send out](http://www.youtube.com/v/EHubFEiS4tk?start=305&end=310&autoplay=1&loop=1)
* [side pass](http://www.youtube.com/v/bv_Xsyy3uAY?start=58&end=64&autoplay=1&loop=1)
* [she goes he goes](http://www.youtube.com/v/91FZSR9wQKk?start=55&end=61&autoplay=1&loop=1)
* [promenade](http://www.youtube.com/v/CF0KIsQR6A4?start=109&end=114&autoplay=1&loop=1)
* [reverse promenade](http://www.youtube.com/v/CF0KIsQR6A4?start=116&end=121&autoplay=1&loop=1)
* [cudle](http://www.youtube.com/v/USXmK5QXwCc?start=139&end=146&autoplay=1&loop=1)
* [sweetheart](http://www.youtube.com/v/cjQIwvnfI3Q?start=141&end=149&autoplay=1&loop=1)
* [belt slide](http://www.youtube.com/v/USXmK5QXwCc?start=56&end=60&autoplay=1&loop=1)
* [lindy hop basket](http://www.youtube.com/v/yR-H2MKsOTM?start=148&end=156&autoplay=1&loop=1)
* [tandem charleston](http://www.youtube.com/v/hlkp-XMeQOM?start=65&end=82&autoplay=1&loop=1)
* [tandem charleston2](http://www.youtube.com/v/jU0NWSu2x0o?start=28&end=37&autoplay=1&loop=1)
* [tandem - Windshield wiper](http://www.youtube.com/v/jU0NWSu2x0o?start=35&end=46&autoplay=1&loop=1)
* [tandem - follower turn](http://www.youtube.com/v/jU0NWSu2x0o?start=49&end=57&autoplay=1&loop=1)
* [tandem - Push away exit](http://www.youtube.com/v/jU0NWSu2x0o?start=59&end=67&autoplay=1&loop=1)
* [Airplane Charleston ](http://www.youtube.com/v/-eQaOZXJdkA?start=19&end=30&autoplay=1&loop=1)
* [s-turn into tandem charleston](http://www.youtube.com/v/5MEfGPNf3nE?start=33&end=43&autoplay=1&loop=1)
* [scoots](http://www.youtube.com/v/0nbTtgY-aQ8?start=31&end=41&autoplay=1&loop=1)


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

## TODO

Using OpenCV we could improve the quality of the vidoes by running some video stabilization method, background substraction and contrast enhancement.
we could also denoise the sound on some videos.













