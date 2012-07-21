#!/usr/bin/python

# Warai version 0.1
# Written by Ben 'malzraa' Keller
# last updated 27 July 2008
# Warai is licensed under the GPL v 3.0 

import sys, os, Image, pdb
from opencv.cv import *
from opencv.highgui import *

def detectface(image, overlay, input): #input and image are the PIL and OpenCV objects respectively
	# These lines will find all the faces in an image, and store them in a list of objects
	size = input.size
	if overlay.mode != 'RGBA':
		overlay = overlay.convert('RGBA')
	grayscale = cvCreateImage(cvSize(size[0], size[1]), 8, 1)
	cvCvtColor(image, grayscale, CV_BGR2GRAY)
	storage = cvCreateMemStorage(0)
	cvClearMemStorage(storage)
	cvEqualizeHist(grayscale, grayscale)
	cascade = cvLoadHaarClassifierCascade('haarcascade_frontalface_alt.xml', cvSize(1,1))
	faces = cvHaarDetectObjects(grayscale, cascade, storage, 1.2, 2, CV_HAAR_DO_CANNY_PRUNING, cvSize(100,100))
	if faces: ## This loop overlays all the faces with a square image 1.2 times the dimensions of the face
		for i in faces:
			if int(i.width) > int(i.height):
				dimension = 1.2 * i.width
				size = int(dimension), int(dimension)
			else:
				dimension = 1.2 * i.height
				size = int(dimension), int(dimension)
			overlay = overlay.resize(size)
			input.paste(overlay.convert('RGB'), (int(i.x), int(i.y) ), overlay)
  

def video(video, overlay, output):
	os.makedirs("/tmp/warai/frames/")
	os.system("ffmpeg -i "+video+" -f image2 /tmp/warai/frames/img%09d.png")
	os.system("ffmpeg -i "+video+" -vn /tmp/warai/audio.wav")
	frames = os.listdir("/tmp/warai/frames")
	rate = "24"
	n = 0
	for j in frames:
		j = "/tmp/warai/frames/"+j
		frame = Image.open(j)
		detectface(cvLoadImage(j), overlay, frame)
		frame.save(j)
	os.system("ffmpeg -r "+rate+" -i /tmp/warai/frames/img%09d.png -i /tmp/warai/audio.wav "+output)#This rebuilds the video from the audio and frames
	#Cleanup the ridiculous amount of data left behind
	for i in frames:
		os.remove("/tmp/warai/frames/"+i)
	os.remove("/tmp/warai/audio.wav")
	os.removedirs("/tmp/warai/frames/")
	
def main():
	if len(sys.argv) < 5:
		print 'Usage: warai -flag overlay inputfile outputfile'
		exit()
	overlay = Image.open(sys.argv[2])
	if sys.argv[1] == '-i':
		input = Image.open(sys.argv[3])
		image = cvLoadImage(sys.argv[3])
		detectface(image, overlay, input)
		input.save(sys.argv[3])
	elif sys.argv[1] == '-v':
		video(sys.argv[3], overlay, sys.argv[4])
main()
