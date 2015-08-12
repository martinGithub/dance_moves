# Lindy Hop Moves Videos Maker
This project contains a python script that downloads videos from *youtube* and edit them automatically to create on your computer a short video file of about 5s for each lindy move listed below. You can transfert these video files to your smartphone and watch them whenever you forgot the details of a move.

## Mobile Video Players 

* Using the application *AVPlayer* on android you can loop the video until you fully understand the move.
* Using the *VLC player* on android you can visualize a video in slow motion

##Existing moves

* [barrel roll](http://www.infinitelooper.com/?v=mLkkUDXE65Y#/21;26)
* [lindy circle](http://www.infinitelooper.com/?v=CF0KIsQR6A4#/145;150)
* [lindy circle from open](http://www.infinitelooper.com/?v=pnWF9Lb7QaU#/87;94)
* [swing out from closed](http://www.infinitelooper.com/?v=YSnlHV_GCA0#/60;64)
* [swing out from open](http://www.infinitelooper.com/?v=YSnlHV_GCA0#/67;71)
* [texas tommy](http://www.infinitelooper.com/?v=YSnlHV_GCA0#/84;89)
* [texas tommy2](http://www.infinitelooper.com/?v=U9PJO-Keu-M#/64;71)
* [texas tommy from closed](http://www.infinitelooper.com/?v=GzyQldsVDb0#/15;21)
* [inside turn swingout from open](http://www.infinitelooper.com/?v=9XkYi-s5YWw#/101;107)
* [inside turn swingout fromclosed](http://www.infinitelooper.com/?v=TlUwWjbyeN0#/29;33)
* [the nothing](http://www.infinitelooper.com/?v=rfUdoXikhMc#/17;21)
* [she goes](http://www.infinitelooper.com/?v=rbxqTcKj2U8#/21;27)
* [treading water](http://www.infinitelooper.com/?v=rbxqTcKj2U8#/33;39)
* [he goes](http://www.infinitelooper.com/?v=CF0KIsQR6A4#/99;104)
* [tuck turn](http://www.infinitelooper.com/?v=uDARWpHsF-Y#/150;154)
* [sugar push](http://www.infinitelooper.com/?v=KJGrzuTPj2o#/92;97)
* [kick through](http://www.infinitelooper.com/?v=dPjS6QVqltk#/107;120)
* [under arm turn](http://www.infinitelooper.com/?v=uDARWpHsF-Y#/117;121)
* [send out](http://www.infinitelooper.com/?v=EHubFEiS4tk#/305;310)
* [side pass](http://www.infinitelooper.com/?v=bv_Xsyy3uAY#/58;64)
* [she goes he goes](http://www.infinitelooper.com/?v=91FZSR9wQKk#/55;61)
* [promenade](http://www.infinitelooper.com/?v=CF0KIsQR6A4#/109;114)
* [reverse promenade](http://www.infinitelooper.com/?v=CF0KIsQR6A4#/116;121)
* [cudle](http://www.infinitelooper.com/?v=USXmK5QXwCc#/139;146)
* [sweetheart](http://www.infinitelooper.com/?v=cjQIwvnfI3Q#/141;149)
* [belt slide](http://www.infinitelooper.com/?v=USXmK5QXwCc#/56;60)
* [lindy hop basket](http://www.infinitelooper.com/?v=yR-H2MKsOTM#/148;156)
* [tandem charleston](http://www.infinitelooper.com/?v=hlkp-XMeQOM#/65;82)
* [tandem charleston2](http://www.infinitelooper.com/?v=jU0NWSu2x0o#/28;37)
* [tandem - Windshield wiper](http://www.infinitelooper.com/?v=jU0NWSu2x0o#/35;46)
* [tandem - follower turn](http://www.infinitelooper.com/?v=jU0NWSu2x0o#/49;57)
* [tandem - Push away exit](http://www.infinitelooper.com/?v=jU0NWSu2x0o#/59;67)
* [Airplane Charleston ](http://www.infinitelooper.com/?v=-eQaOZXJdkA#/19;30)
* [s-turn into tandem charleston](http://www.infinitelooper.com/?v=5MEfGPNf3nE#/33;43)
* [scoots](http://www.infinitelooper.com/?v=0nbTtgY-aQ8#/31;41)
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













