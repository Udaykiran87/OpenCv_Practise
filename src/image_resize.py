# let's start with the Imports
import cv2
import numpy as np
import os
from pathlib import Path

# get the image path to be read
filepath = str(Path("../images/Taj-Mahal.jpg"))

# create folder if not present already to store any images from the script
os.makedirs('output_images', exist_ok=True)

# Read the image using imread function
image = cv2.imread(filepath)
cv2.imshow('Original Image', image)

# let's downscale the image using new  width and height
down_width = 300
down_height = 200
down_points = (down_width, down_height)
resized_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)

# let's upscale the image using new  width and height
up_width = 600
up_height = 400
up_points = (up_width, up_height)
resized_up = cv2.resize(image, up_points, interpolation= cv2.INTER_LINEAR)


# Scaling Up the image 1.2 times by specifying both scaling factors
scale_up_x = 1.2
scale_up_y = 1.2
# Scaling Down the image 0.6 times specifying a single scale factor.
scale_down = 0.6

scaled_f_down = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_LINEAR)
scaled_f_up = cv2.resize(image, None, fx= scale_up_x, fy= scale_up_y, interpolation= cv2.INTER_LINEAR)

# Scaling Down the image 0.6 times using different Interpolation Method
res_inter_nearest = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_NEAREST)
res_inter_linear = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_LINEAR)
res_inter_area = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_AREA)

# Display images and press any key to check next image
cv2.imshow('Resized Down by defining height and width', resized_down)
cv2.waitKey(0)
cv2.imshow('Resized Up image by defining height and width', resized_up)
cv2.waitKey(0)

cv2.imshow('Resized Down by defining scaling factor', scaled_f_down)
cv2.waitKey(0)
cv2.imshow('Resized Up image by defining scaling factor', scaled_f_up)
cv2.waitKey(0)

cv2.imshow('Scaled Down by using INTER_NEAREST interpolation', res_inter_nearest)
cv2.waitKey(0)
cv2.imshow('Scaled Down by using INTER_LINEAR interpolation', res_inter_linear)
cv2.waitKey(0)
cv2.imshow('Scaled Down by using INTER_AREA interpolation', res_inter_area)
cv2.waitKey(0)

# Concatenate images in horizontal axis for comparison
vertical= np.concatenate((res_inter_nearest, res_inter_linear, res_inter_area), axis = 0)
# Display the image Press any key to continue
cv2.imshow('Inter Nearest :: Inter Linear :: Inter Area', vertical)
cv2.waitKey(0)

#press any key to close the windows
cv2.destroyAllWindows()