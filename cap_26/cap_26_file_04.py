#Capturing video
#Reading images one by one and use loop to create an video
import cv2
import time


#Creat a video object
my_video = cv2.VideoCapture(0, cv2.CAP_DSHOW) #The argument for VideoCapture can either be the index of your camera(if you have multiple cameras: 0,1,2... or it could be the name of the video file you are loading: "movie.mp4")
interations = 0
while True:
    interations = interations + 1
    check, frame = my_video.read() #check is a boolean and frame is an numpy array
    # print(type(check))
    # print(type(frame))
    # print(check)
    # print(frame)

    #Halt the script for as long you need to capture the video
    # time.sleep(3)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray_frame)
    #Wait how much time you need between frames
    key = cv2.waitKey(1) #1000=1 second
    #Stop the code if 'q' is pressed from keyboard
    if key == ord('q'):
        break
print(f"Number of iterations: {interations}")
#Release the camera
my_video.release()
cv2.destroyAllWindows()
