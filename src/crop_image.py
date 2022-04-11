# Import packages
import cv2
import numpy as np

import os
from pathlib import Path

# get the image path to be read
filepath = str(Path("../images/Taj-Mahal.jpg"))

# create folder if not present already to store any images from the script
os.makedirs('output_images', exist_ok=True)

img = cv2.imread(filepath)
print(img.shape) # Print image shape
cv2.imshow("original", img)

# Cropping an image
cropped_image = img[80:280, 150:330]

# Display cropped image
cv2.imshow("cropped", cropped_image)

# Save the cropped image
cv2.imwrite("output_images/Cropped Image.jpg", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()