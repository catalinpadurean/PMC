#Application 6: Webcam Motion Detector with OpenCV

import cv2
import pandas as pd
import time

from datetime import datetime as dt


first_frame = None
status_list = [None, None] #Add two None items to avoid "list index out of range" when comparing the last two elements of this list
times = []
data_frame = pd.DataFrame(columns = ["Start, End"])
length = None
#Creat a video object
my_video = cv2.VideoCapture(0, cv2.CAP_DSHOW) #The argument for VideoCapture can either be the index of your camera(if you have multiple cameras: 0,1,2... or it could be the name of the video file you are loading: "movie.mp4")

while True:
    check, frame = my_video.read() #check is a boolean and frame is an numpy array
    status = 0
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21,21), 0) #Blur image

    if first_frame is None:
        first_frame = gray_frame
        continue
    delta_frame = cv2.absdiff(first_frame, gray_frame) #calculate difference between first frame and gray frame

    #cv.2threshold method returns a tupple, and the second item is the frame we need to use
    thres_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] #Use threshold method to calculcate the diff, select threshold 30, and if diff is grater than threshol value assign 255 for that pixel
    thres_frame = cv2.dilate(thres_frame, None, iterations=2) #Second param is None because we don't have kerney array, Third param is 2, the bigger the param is the smoother the image will be

    (cnts,_) = cv2.findContours(thres_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for countour in cnts:
        if cv2.contourArea(countour) < 10000:
            continue
        status = 1
        (x, y, w, h ) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 3)
    status_list.append(status)  
    if status_list[-1] != status_list[-2]:
        times.append(dt.now())

    cv2.imshow("Capturing", gray_frame)
    cv2.imshow("Delta", delta_frame)
    cv2.imshow("Threshold", thres_frame)
    cv2.imshow("Color frame", frame)

    #Wait how much time you need between frames
    key = cv2.waitKey(1) #1000=1 second

    #Stop the code if 'q' is pressed from keyboard
    if key == ord('q'):
        if status == 1:
            times.append(dt.now())
        break

if len(times) %2 !=0:
    length = len(times) - 1
else:
    length = len(times)
for i in range(0, length, 2):
    data_frame = data_frame.append({"Start":times[i], "End": times[i+1]}, ignore_index=True)
data_frame.to_csv("j:\Work\PMC\cap_27\APP6.csv")
#Release the camera
my_video.release()
cv2.destroyAllWindows()
