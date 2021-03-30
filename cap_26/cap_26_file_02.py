# Face detection

import cv2

face_cascade = cv2.CascadeClassifier("hfd.xml") #Cascade classifier object
#Load image where you want to search for a face using cascade classifier
image = cv2.imread("photo.jpg")
#It is recommended to use grayscale version of the image when looking for faces
#Use another variable to open the original image and pass the cv2.COLOR_BGR2GRAY flag to convert the image from RGB to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Show the color version of image
cv2.imshow("Color", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Show the gray version of image
# cv2.imshow("Gray", image_gray)
# cv2.waitKey(0)
# cv.destroyAllWindows()