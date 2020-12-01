import numpy as np
import cv2
import skimage as ski
import sys
import argparse

img_in_filename = 'test_img/blurry_moon.tif'

parser = argparse.ArgumentParser(description='Applies the High-Boost Filter to the input image and returns an output image')
parser.add_argument('-i','--img_file_name', type=str,
					help='input image file (ex. \'folder/img.png\')')
if len(sys.argv) > 1:
	img_in_filename = parser.parse_args().img_file_name

img_in = cv2.imread(img_in_filename,1)
imgfile_folder,imgfile_name = img_in_filename.split('/')
imgfile_name,imgfile_extension = imgfile_name.split('.')

print(imgfile_folder)
print(imgfile_name)
print(imgfile_extension)
cv2.namedWindow('input_imgfile', cv2.WINDOW_NORMAL)
cv2.imshow("input_imgfile", img_in)

cv2.waitKey()
cv2.destroyAllWindows()
