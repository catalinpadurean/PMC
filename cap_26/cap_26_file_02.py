# Face detection

import cv2
import os

#Load image where you want to search for a face using cascade classifier
#use 'this_folder' to compute the path, otherwise the cv2 won't recognize the correct path for the file.
this_folder = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(this_folder, "photo.jpg")
my_xml = os.path.join(this_folder, "hfd.xml")
face_cascade = cv2.CascadeClassifier(my_xml) #Cascade classifier object
image = cv2.imread(my_file)
#It is recommended to use grayscale version of the image when looking for faces
#Use another variable to open the original image and pass the cv2.COLOR_BGR2GRAY flag to convert the image from RGB to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Use detect multiscale method to search for the xml characteristics in the image.
#It will return the coordinates of the face from the image (Upper left corner of the rectangle that contains the face)

faces = face_cascade.detectMultiScale(
image_gray, #File name
scaleFactor = 1.05, #scaleFactor will decrease by 5% the image and will search in a smaller image for another face. Smaller value=higher accuracy
minNeighbors = 5)  #number of neighbors to search around the window

#faces is a numpy.ndarray object with 4 values [X, Y, W, H] => X = line of UpperLeftCorner| Y = colum of UpperLeftCorner| W = width of rectangle | H = Height of rectangle
#print(faces)

for x, y, w, h in faces:
    image = cv2.rectangle(image,
    (x,y),      # tupple with coordinates for UpperLeftCorner
    (x+w, y+h), # tupple with coordinates for BottomRightCorner
    (0,255,0),  # Color of rectangle
    3)          # Width of rectangle


resized_image = cv2.resize(image, (int(image.shape[1]/3), int(image.shape[0]/3)))
#Show the color version of image
# cv2.imshow("Color", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#Show the gray version of image
# cv2.imshow("Gray", image_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#Show the resized color version of image
cv2.imshow("Col Resz", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()