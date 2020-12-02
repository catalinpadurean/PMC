#Write a script that will resize all images in a directory to 100x100

import cv2
import glob
import os

this_directory = os.path.dirname(os.path.abspath(__file__))
target_folder = "sample_images"

this_folder = os.path.join (this_directory, target_folder)
files = os.listdir(this_folder)

for image in files:
    my_img_path = os.path.join(this_folder, image)
    my_img = cv2.imread(my_img_path, 0)
    my_img_re = cv2.resize(my_img, (100,100))
    cv2.imshow("Resized image",my_img_re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    my_img_re_path = os.path.join(this_folder, image.rsplit(".",1)[0]+"_resized_.jpg")
    cv2.imwrite(my_img_re_path, my_img_re)