import numpy as np 
import copy
import random
from math import e
import statistics
import json
import os.path
from os import path
import argparse
import threading

import cv2
from PIL import Image
from matplotlib import cm
import concurrent.futures

import dot_series
import ToDot

def start(d1):
	return d1.start()


d = []

d.append( ToDot.ToDot("C:\\Users\\Andrew\\Documents\\Python projects\\calculated Dots\\", "look.png", "fool4.png",
		number_of_dots = 300, blur_amount = 17, diff_blur_amount = 17, starting_img = "fool3.png") )

"""
d.append( ToDot.ToDot("C:\\Users\\Andrew\\Desktop\\Python Stuff\\projects\\calculated Dots\\", "look3.png", "final2.png",
		number_of_dots = 50, blur_amount = 5, diff_blur_amount = 5) )
"""


with concurrent.futures.ThreadPoolExecutor() as executor:

	results = executor.map(start, d)
	
	i = -1
	for result in results:
		#for result in concurrent.futures.as_completed( results ):
		i += 1
		#print(result.result())
		cv2.imshow("newimg" + str(i), result )
		
		
cv2.waitKey(0)
cv2.destroyAllWindows()