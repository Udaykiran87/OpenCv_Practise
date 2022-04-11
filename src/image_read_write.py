# import the cv2 library
import cv2
import os
from pathlib import Path

# get the image path to be read
filepath = str(Path("../images/Taj-Mahal.jpg"))

# create folder if not present already to store any images from the script
os.makedirs('output_images', exist_ok=True)

# The function cv2.imread() is used to read an image.
img_grayscale = cv2.imread('../images/Taj-Mahal.jpg',0)

# The function cv2.imshow() is used to display an image in a window.
cv2.imshow('graycsale image',img_grayscale)

# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv2.waitKey(0)

# cv2.destroyAllWindows() simply destroys all the windows we created.
cv2.destroyAllWindows()

# The function cv2.imwrite() is used to write an image.
cv2.imwrite('output_images/grayscale.jpg',img_grayscale)