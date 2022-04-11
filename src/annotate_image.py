# Import dependencies
import cv2
import numpy as np

import os
from pathlib import Path

# get the image path to be read
filepath = str(Path("../images/Taj-Mahal.jpg"))

# create folder if not present already to store any images from the script
os.makedirs('output_images/annotate_image/', exist_ok=True)

# Reading the image
image = cv2.imread(filepath)

# Display Image
cv2.imshow('Original Image',image)
cv2.waitKey(0)
# Print error message if image is null
if image is None:
    print('Could not read image')
# Draw line on image
imageLine = image.copy()
# Draw the image from point A to B
pointA = (200,80)
pointB = (450,80)
cv2.line(imageLine, pointA, pointB, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
cv2.imshow('Image Line', imageLine)
cv2.waitKey(0)


# Make a copy of image
imageCircle = image.copy()
# define the center of circle
circle_center = (415,190)
# define the radius of the circle
radius =100
#  Draw a circle using the circle() Function
cv2.circle(imageCircle, circle_center, radius, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)
# Display the result
cv2.imshow("Image Circle",imageCircle)
cv2.waitKey(0)


# make a copy of the original image
imageFilledCircle = image.copy()
# define center of the circle
circle_center = (415,190)
# define the radius of the circle
radius =100
# draw the filled circle on input image
cv2.circle(imageFilledCircle, circle_center, radius, (255, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
# display the output image
cv2.imshow('Image with Filled Circle',imageFilledCircle)
cv2.waitKey(0)


# make a copy of the original image
imageRectangle = image.copy()
# define the starting and end points of the rectangle
start_point =(300,115)
end_point =(475,225)
# draw the rectangle
cv2.rectangle(imageRectangle, start_point, end_point, (0, 0, 255), thickness= 3, lineType=cv2.LINE_8)
# display the output
cv2.imshow('imageRectangle', imageRectangle)
cv2.waitKey(0)


# make a copy of the original image
imageEllipse = image.copy()
# define the center point of ellipse
ellipse_center = (415,190)
# define the major and minor axes of the ellipse
axis1 = (100,50)
axis2 = (125,50)
# draw the ellipse
#Horizontal
cv2.ellipse(imageEllipse, ellipse_center, axis1, 0, 0, 360, (255, 0, 0), thickness=3)
#Vertical
cv2.ellipse(imageEllipse, ellipse_center, axis2, 90, 0, 360, (0, 0, 255), thickness=3)
# display the output
cv2.imshow('ellipse Image',imageEllipse)
cv2.waitKey(0)

# make a copy of the original image
halfEllipse = image.copy()
# define the center of half ellipse
ellipse_center = (415,190)
# define the axis point
axis1 = (100,50)
# draw the Incomplete/Open ellipse, just a outline
cv2.ellipse(halfEllipse, ellipse_center, axis1, 0, 180, 360, (255, 0, 0), thickness=3)
# if you want to draw a Filled ellipse, use this line of code
cv2.ellipse(halfEllipse, ellipse_center, axis1, 0, 0, 180, (0, 0, 255), thickness=-2)
# display the output
cv2.imshow('halfEllipse',halfEllipse)
cv2.waitKey(0)


# make a copy of the original image
imageText = image.copy()
#let's write the text you want to put on the image
text = 'Taj Mahal!'
#org: Where you want to put the text
org = (50,350)
# write the text on the input image
cv2.putText(imageText, text, org, fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 2.5, color = (250,225,100))
# display the output image with text over it
cv2.imshow("Image Text",imageText)
cv2.waitKey(0)
cv2.destroyAllWindows()