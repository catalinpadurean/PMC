# For Win10 Pro use: "python -m notebook" to open jupyternotebook in browser
# In PyCharm there seems to be an issue with jupyter notebook. Open jupyter from projects that weren't created with pyCharm
# Using open cv to conver image to array
import cv2
im_g=cv2.imread("smallgray.png",0) #0 means read image in greyscale
print("Greyscale")
print(im_g)
#First element of the array is the value of the first pixel of the image. This rule applies for all pixels
im_g_1=cv2.imread("smallgray.png",1) #1 means read image in RGB
print("RGB")
print(im_g_1)
#First element of each array is the value coresponding in each one of these 3 layers: Red Blue Green for the first pixel. This rule applies for all pixels