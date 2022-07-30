import cv2
import numpy

def getFingerprint(img):
    img = numpy.asarray(img)
    img = cv2.resize(img,(8,8),interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    ## =========== Total 為像素和初始值等於0 ===========
    Total = 0
    ahash_str = ''
    for i in range(8):
        for j in range(8):
            Total = Total + gray[i,j]
    avg = Total / 64

    for i in range(8):                  
        for j in range(8):
            if  gray[i,j]>avg:
                ahash_str=ahash_str+'1'
            else:
                ahash_str=ahash_str+'0'

    return ahash_str