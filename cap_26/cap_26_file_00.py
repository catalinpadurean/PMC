#Python for Image and Video Processing with OpenCV
import cv2
import os

#load image file
#use 'this_folder' to compute the path, otherwise the cv2 won't recognize the correct path for the file.
this_folder = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(this_folder, "galaxy.jpg")

#Display image(as read from cv2) as an array and some properties of the image in different formats
img = cv2.imread(my_file,0) #BlackWhite
print(img)
print(img.shape)
print(img.ndim)

img2 = cv2.imread(my_file, 1) #RGB
print(img2)
print(img2.shape)
print(img2.ndim)

#Display image as an image
cv2.imshow("BlackWhite_Galaxy",img)
cv2.waitKey(2000)#Timeout to close window
cv2.destroyAllWindows()

#Comment this lines for now and work in black white only for the rest of the chapter
#cv2.imshow("RBG_Galaxy",img2)
#cv2.waitKey(0)#Timeout to close window. If 0, close at key press
#cv2.destroyAllWindows()

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Resized_Galaxy",resized_image)
cv2.waitKey(0)#Timeout to close window
cv2.destroyAllWindows()

#Write the new image in a new file
my_resized_iamge = os.path.join(this_folder, "galaxy_resized.jpg")
cv2.imwrite(my_resized_iamge, resized_image)