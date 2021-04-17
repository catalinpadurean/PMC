#Application 6: Webcam Motion Detector with OpenCV

import cv2
import time


first_frame = None
#Creat a video object
my_video = cv2.VideoCapture(0, cv2.CAP_DSHOW) #The argument for VideoCapture can either be the index of your camera(if you have multiple cameras: 0,1,2... or it could be the name of the video file you are loading: "movie.mp4")

while True:
    check, frame = my_video.read() #check is a boolean and frame is an numpy array

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
        if cv2.contourArea(countour) < 1000:
            continue
        (x, y, w, h ) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 3)
       
    cv2.imshow("Capturing", gray_frame)
    cv2.imshow("Delta", delta_frame)
    cv2.imshow("Threshold", thres_frame)
    cv2.imshow("Color frame", frame)

    #Wait how much time you need between frames
    key = cv2.waitKey(1) #1000=1 second

    #Stop the code if 'q' is pressed from keyboard
    if key == ord('q'):
        break
#Release the camera
my_video.release()
cv2.destroyAllWindows()
