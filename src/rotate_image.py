# Import packages
import cv2
import numpy as np

import os
from pathlib import Path

# get the image path to be read
filepath = str(Path("../images/Taj-Mahal.jpg"))

# create folder if not present already to store any images from the script
os.makedirs('output_images/rotate_image/', exist_ok=True)

# Reading the image
image = cv2.imread(filepath)

# dividing height and width by 2 to get the center of the image
height, width = image.shape[:2]
# get the center coordinates of the image to create the 2D rotation matrix
center = (width/2, height/2)

# using cv2.getRotationMatrix2D() to get the rotation matrix
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)

# rotate the image using cv2.warpAffine
rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))

cv2.imshow('Original image', image)
cv2.imshow('Rotated image', rotated_image)
# wait indefinitely, press any key on keyboard to exit
cv2.waitKey(0)
# save the rotated image to disk
cv2.imwrite('output_images/rotate_image/rotated_image.jpg', rotated_image)