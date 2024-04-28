'''
 > BASIC INFO ABOUT THE CODE

 - Folowing code is used for Analysing the captured image from the camera and run a YOLO V5 algorithm on it for Object detection from
   the image.
 - Currently we are trying to detect car , bus , truck , human and bike 

## The fucntion returns :
    1. IMAGE with sqares around the objected detected.
    2. Upon closing the window returns a "total count" of all types of vechiles detected in terminal   

'''

import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

im = cv2.imread(r'Images/cars5.jpg')
# im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()
#print('Number of cars in the image is '+ str(label.count('car')))

car = label.count('car')
bus = label.count('bus')
truck = label.count('truck')
motorcycle = label.count('motorcycle')
vechile = car + bus + truck + motorcycle
print('Number of vechile in the image is :',vechile )
