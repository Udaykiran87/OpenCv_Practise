import cv2
import numpy as np

import os
from pathlib import Path

# get the image path to be read
filepath = str(Path("../images/Taj-Mahal.jpg"))

# create folder if not present already to store any images from the script
os.makedirs('output_images/filter_image/', exist_ok=True)

# Reading the image
image = cv2.imread(filepath)

# Print error message if image is null
if image is None:
    print('Could not read image')

# Apply identity kernel
kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)

cv2.imshow('Original', image)
cv2.imshow('Identity', identity)

cv2.waitKey()
cv2.imwrite('output_images/filter_image/identity.jpg', identity)
cv2.destroyAllWindows()

# Apply blurring kernel
kernel2 = np.ones((5, 5), np.float32) / 25
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)

cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)

cv2.waitKey()
cv2.imwrite('output_images/filter_image/blur_kernel.jpg', img)

"""
Apply blur using `blur()` function
"""
img_blur = cv2.blur(src=image, ksize=(5,5)) # Using the blur function to blur an image where ksize is the kernel size

# Display using cv2.imshow()
# cv2.imshow('Original', image)
cv2.imshow('Blurred', img_blur)

cv2.waitKey(0)
cv2.imwrite('output_images/filter_image/blur.jpg', img_blur)

"""
Apply Gaussian blur
"""
# sigmaX is Gaussian Kernel standard deviation
# ksize is kernel size
gaussian_blur = cv2.GaussianBlur(src=image, ksize=(5,5), sigmaX=0, sigmaY=0)

# cv2.imshow('Original', image)
cv2.imshow('Gaussian Blurred', gaussian_blur)

cv2.waitKey()
cv2.imwrite('output_images/filter_image/gaussian_blur.jpg', gaussian_blur)


"""
Apply Median blur
"""
# medianBlur() is used to apply Median blur to image
# ksize is the kernel size
median = cv2.medianBlur(src=image, ksize=5)

# cv2.imshow('Original', image)
cv2.imshow('Median Blurred', median)

cv2.waitKey()
cv2.imwrite('output_images/filter_image/median_blur.jpg', median)


"""
Apply sharpening using kernel
"""
kernel3 = np.array([[0, -1,  0],
                   [-1,  5, -1],
                    [0, -1,  0]])
sharp_img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel3)

cv2.imshow('Original', image)
cv2.imshow('Sharpened', sharp_img)

cv2.waitKey()
cv2.imwrite('output_images/filter_image/sharp_image.jpg', sharp_img)


cv2.destroyAllWindows()