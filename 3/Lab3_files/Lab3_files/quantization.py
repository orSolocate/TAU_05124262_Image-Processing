import matplotlib.pyplot as plt
import numpy as np

def quant_img (img,N):
    #uniform quantization of an image to values [0,N]
    min_val=np.min(img)
    max_val=np.max(img)
    quant_range=(max_val-min_val)/N
    quant_uniform=min_val + np.floor((quant_range*np.floor_divide(img-min_val,quant_range)))
    #explanation: we normalize the values of the image to the window quant_uniform, and round down
    return quant_uniform

img=plt.imread("lena512.bmp")

quant=quant_img(img,20)
plt.imshow(quant,cmap='gray')
plt.show()
plt.imshow(quant,cmap='gray')