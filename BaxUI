#python
import cv2
import numpy as np

import os
import sys
import argparse

import rospy

import cv
import cv_bridge
import baxter_interface
from baxter_core_msgs.msg import ITBState

import std_msgs.msg
from sensor_msgs.msg import Image


wheelLast = 0
def showList(the_array):
	rospy.sleep(0.4)
	selected = 1
	runit = True
	while runit == True:
		img = cv2.imread('ku.png')
		width = 350
		height = 65
		gap = 35

		startLX=100
		startL2X=560
		startLY=175
		offset=height+gap
		font = cv2.FONT_HERSHEY_SIMPLEX
		fontoffsetX = 42
		fontoffsetY = 20
		purple = (50,13,30)
		blue = (255,168,0)
		

		for i in range(len(the_array)):
			if i == selected:
				color = blue
			else:
				color = purple
			if i < 4:
				cv2.rectangle(img,(startLX ,startLY + (i*offset)),(startLX+width,startLY+height + (i*offset)),color,-1)
				cv2.putText(img,the_array[i][0],(startLX+fontoffsetY,startLY + (i*offset)+fontoffsetX), font, 1,(255,255,255),2)
			elif i < 8:
				j = i - 4
				cv2.rectangle(img,(startL2X ,startLY + (j*offset)),(startL2X+width,startLY+height + (j*offset)),color,-1)
				cv2.putText(img,the_array[i][0],(startL2X+fontoffsetY,startLY + (j*offset)+fontoffsetX), font, 1,(255,255,255),2)
		# cv2.imshow('MENU',img)
		cv2.imwrite('temp.png',img)
		send_image()

		#print "selected:" + str(selected)
		navigator = rospy.wait_for_message('/robot/itb/right_itb/state', ITBState, 3)
		#print navigator

		if navigator.buttons[1] == True:
			runit = False

		if navigator.buttons[0] == True:
			if the_array[selected][1] != "":
				globals()[the_array[selected][1]]()
			else:
				print "nothing defined"

		global wheelLast
		if wheelLast < navigator.wheel:
			if selected > 0:
				selected = selected - 1
			wheelLast = navigator.wheel

		if wheelLast > navigator.wheel:
			if selected < len(the_array)-1:
				selected = selected + 1
			wheelLast = navigator.wheel
	reset_display()





def showOption(the_array):
	rospy.sleep(0.4)
	selected = 0
	runit = True
	while runit == True:
		img = cv2.imread('ku.png')
		width = 350
		height = 65
		gap = 35

		startLX=100
		startL2X=560
		startLY=175
		offset=height+gap
		font = cv2.FONT_HERSHEY_SIMPLEX
		fontoffsetX = 42
		fontoffsetY = 20
		purple = (50,13,30)
		blue = (255,168,0)
		green = (0,255,0)
		

		for i in range(len(the_array)-1):
			if i == selected:
				color = green
			else:
				color = purple

			cv2.putText(img,the_array[0][0],(startLX+fontoffsetY,startLY+fontoffsetY), font, 1,(0,0,0),2)

			cv2.putText(img,"currently set to:",(startLX+fontoffsetY,startLY+fontoffsetY+50), font, 0.6,(0,0,0),2)
			cv2.putText(img,globals()[the_array[0][1]],(startLX+fontoffsetY+20,startLY+fontoffsetY+70), font, 0.6,(0,0,0),2)

			cv2.rectangle(img,(startL2X ,startLY + (i*offset)),(startL2X+width,startLY+height + (i*offset)),color,-1)
			cv2.putText(img,the_array[i+1][0],(startL2X+fontoffsetY,startLY + (i*offset)+fontoffsetX), font, 1,(255,255,255),2)
		# cv2.imshow('Menu',img)
		cv2.imwrite('temp.png',img)
		send_image()

		navigator = rospy.wait_for_message('/robot/itb/right_itb/state', ITBState, 3)
		#print navigator

		if navigator.buttons[1] == True:
			runit = False

		if navigator.buttons[0] == True:
			if the_array[selected][1] != "":
				globals()[the_array[0][1]] = the_array[selected+1][1]
			#else:
				#print "nothing defined"

		global wheelLast
		if wheelLast < navigator.wheel:
			if selected > 0:
				selected = selected - 1
			wheelLast = navigator.wheel

		if wheelLast > navigator.wheel:
			if selected < len(the_array)-1:
				selected = selected + 1
			wheelLast = navigator.wheel




def send_image():
    img = cv.LoadImage('temp.png')
    msg = cv_bridge.CvBridge().cv_to_imgmsg(img, encoding="bgr8")
    pub = rospy.Publisher('/robot/xdisplay', Image, latch=True)
    pub.publish(msg)
    # Sleep to allow for image to be published.

def reset_display():
    img = cv.LoadImage('rosblocks.png')
    msg = cv_bridge.CvBridge().cv_to_imgmsg(img, encoding="bgr8")
    pub = rospy.Publisher('/robot/xdisplay', Image, latch=True)
    pub.publish(msg)

def main():
	rospy.init_node('rsdk_xdisplay_image', anonymous=True)

