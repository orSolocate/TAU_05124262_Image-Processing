import cv2
import matplotlib.pylab as plt

img = cv2.imread('C:\\Users\\Or\Documents\Studies\TAU\Term1\Image Processing\Lab\koala.png')
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_rgb=cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

h,s,v=cv2.split(img_hsv)

img_hsv_restored=cv2.merge((h,s,v))
difference = cv2.subtract(img_hsv, img_hsv_restored)
b, g, r = cv2.split(difference)
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("The images are completely Equal")