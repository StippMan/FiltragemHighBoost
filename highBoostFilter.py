import numpy as np
import cv2
import skimage as ski
import sys
import argparse

parser = argparse.ArgumentParser(description='Applies the High-Boost Filter to the input image and returns an output image')
parser.add_argument('img_file_name', help='input image file (ex. \'folder/img.png\')')

img_in_filename = parser.parse_args().img_file_name

img_in = cv2.imread("input_images/"+img_in_filename,1)
imgfile_name,imgfile_extension = img_in_filename.split('.')
cv2.namedWindow('input_imgfile', cv2.WINDOW_NORMAL)
cv2.imshow("input_imgfile", img_in)

cv2.waitKey()
cv2.destroyAllWindows()
