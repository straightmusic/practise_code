import os
from PIL import Image
import DHash

imgNames = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
imgName2Pic = {}
DHashValue = {}

def cmpHash(hash1,hash2):              
    n=0                                #n表示漢明距離初始值為0
    if len(hash1)!=len(hash2):         #hash長度不同則返回-1代表傳參出錯
        return -1
    for i in range(len(hash1)):        #for迴圈逐一判斷
        if hash1[i]!=hash2[i]:         #不相等則n+1，最終為相似度
           n=n+1
    return n

def getIngDHashVal(imgName):
    global imgName2Pic
    imgPath = os.path.abspath(os.path.join(os.path.dirname(__file__),'pic/'+imgName))
    img = Image.open(imgPath)
    value = DHash.getFingerprint(img)
    imgName2Pic[imgName]=img
    return value


if __name__ == '__main__':
    ans = ''
    testValue = getIngDHashVal('test.jpg')
    diff = 100
    for name in imgNames:
        imgVal = getIngDHashVal(name)
        HammingDistance = cmpHash(testValue, imgVal)
        if HammingDistance < diff:
            diff = HammingDistance
            ans = name

    imgName2Pic['test.jpg'].show()
    imgName2Pic[ans].show()
