# Import essential libraries
import requests
import cv2
import numpy as np
import imutils
import os

# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://192.168.43.37:8080/shot.jpg"

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)

cam = cv2.VideoCapture(1)
cv2.namedWindow("test")

img_counter = 0


# While loop to continuously fetching data from the Url
while True:
    try :
        #img_resp = requests.get(url)
        #img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        #img = cv2.imdecode(img_arr, -1)
        #img = imutils.resize(img, width=1000, height=1800)
        #print(img)
        #print(img_arr)
        #cv2.imshow("Android_cam", img)

        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        #print(frame)

        img_arr = np.array(bytearray(frame), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        #img = imutils.resize(img, width=1000, height=1800)
        #print(img)
        #print(img_arr)
        cv2.imshow("test", frame)

        key = cv2.waitKey(1)
        if key == ord('s'):
            print(" I am here")
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            cam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray,(28,28))
            print("Resized...")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")

            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
