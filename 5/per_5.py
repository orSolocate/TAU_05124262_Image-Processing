#Or Bahari 204356315
#Yonatan Rodin 20084603

import cv2
import numpy as np
from skimage import color,img_as_ubyte
from skimage.util import random_noise

## Q2
#a
img=cv2.imread('koala.png')
img=color.rgb2gray(img)
img=img_as_ubyte(img)

cv2.imwrite('koala_grey.png',img)

#b- based on https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html
N=5
kernel=np.ones((N,N),np.float32)/np.square(N)
img_blurred=cv2.filter2D(img,-1 ,kernel)
cv2.imwrite('koala_grey_blurred.png',img_blurred)

#c
# we need to multiply by 255 because random_noise return values in range [0,1]
img_blurred_gauss=random_noise(img_blurred,mode='gaussian')*255.0
cv2.imwrite('koala_grey_blurred_noise.png',img_blurred_gauss)

## Q3
#a - Inverse Filter
def invFilter(kernel,img):
    DFT_kernel=np.fft.fft2(kernel)
    #in practice we can't divide in 0, so we solve this
    DFT_kernel[DFT_kernel==0]=0.00001

    DFT_inv=1/DFT_kernel
    inv=np.fft.ifft2(DFT_inv)
    inv=np.absolute(inv)
    res=cv2.filter2D(img,-1,inv)
    res=res/(np.max(res))*255.0 #normalizing back to [0,255]
    return res

#b - Pseudo Inverse Filter
def pseudoInvFilter(kernel,img,epsilon):
    DFT_kernel=np.fft.fft2(kernel)
    DFT_pseudo_kernel=np.zeros(np.shape(DFT_kernel))

    DFT_pseudo_kernel[np.absolute(DFT_kernel)<epsilon]=0
    DFT_pseudo_kernel[np.abs(DFT_kernel) >= epsilon] = (1 / DFT_kernel)[np.abs(DFT_kernel) >= epsilon]

    inv=np.fft.ifft2(DFT_pseudo_kernel)
    inv=np.absolute(inv)
    res=cv2.filter2D(img,-1,inv)
    res=res/(np.max(res))*255.0 #normalizing back to [0,255]
    return res

#c - Wiener Filter
def wienerFilter(kernel,img,sigma=0.01,alpha=0.095):
    DFT_kernel=np.fft.fft2(kernel)
    DFT_wiener_kernel=np.zeros(np.shape(DFT_kernel))
    for i in range(0,len(DFT_kernel)):
        for j in range(0,DFT_kernel.shape[1]):
            DFT_wiener_kernel[i,j]=np.conjugate(DFT_kernel[i,j])/(np.square((np.abs(DFT_kernel[i,j])))+alpha*sigma*(i**2+j**2))

    inv=np.fft.ifft2(DFT_wiener_kernel)
    inv=np.absolute(inv)
    res=cv2.filter2D(img,-1,inv)
    res=res/(np.max(res))*255.0 #normalizing back to [0,255]
    return res


img_invFilter=invFilter(kernel,img_blurred_gauss)
img_psuedo_Filter=pseudoInvFilter(kernel,img_blurred_gauss,0.08)
img_wiener_Filter=wienerFilter(kernel,img_blurred_gauss,0.01,0.01)

cv2.imwrite('koala_grey_invFilter.png',img_invFilter)
cv2.imwrite('koala_grey_psuedoInvFilter.png',img_psuedo_Filter)
cv2.imwrite('koala_grey_wienerFilter.png',img_wiener_Filter)






