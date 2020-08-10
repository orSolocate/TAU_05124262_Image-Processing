import skimage.transform as ski
import matplotlib.pylab as plt
import cv2

img = cv2.imread('C:\\Users\\Or\Documents\Studies\TAU\Term1\Image Processing\Lab\koala.png')
print("img shape is: {0}".format(img.shape))
cv2.imshow(winname='image',mat=img)
# resize

resized_img=ski.resize(img,(50,50),anti_aliasing=True)
print("resized_img shape is: {0}".format(resized_img.shape))
cv2.imshow('100x100',resized_img)

rescaled_img=ski.rescale(img,(2,1.5,1))
cv2.imshow('rescaled 2,1.5,1',rescaled_img)

rot90=ski.rotate(img,90)
rot2=ski.rotate(img,2,resize=False)
rot2_resize=ski.rotate(img,2,resize=True)

