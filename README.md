warai
=====
This is a program for obscuring the faces in photo or video with another image or logo. It is written in python, and depends upon Intel's OpenCV libraries, and the Python Imaging Library (PIL). 

This is the very first python program I wrote, so please forgive the 
general crappyness.
Usage
-----
Once one has the requisite libraries installed, simply run warai.py overlay input output on the command line, and warai will overlay all the faces in file input with file overlay, and save the new file as output.

NOTE: the overlay must be a square image, and generally a png with transparency works best.

WARNING TO VERSION 0.2 USERS: The video feature is currently VERY kludgy, and will suck up MASSIVE amounts of disk space (think at least two orders of magnitude above the size of the original video. It also requires ffmpeg to be installed! 

Changelog (migrated from google code)
-------------------------------------
0.2: Cleaned up main function, added rudimentary video support

0.1.1: Fixed two bugs: now works with alphaless PNGs and overlays smaller than the faces.

0.1: First release of warai, currently can overlay jpg, png, and gifs with a square image. 
