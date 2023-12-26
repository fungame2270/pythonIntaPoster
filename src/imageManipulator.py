import cv2
import requests
import numpy as np

class ImageManipulator:
    def __init__(self):
        pass
    def loadImage(self,url):
        resp = requests.get(url, stream=True).raw
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        self.image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    def cutImageCenter(self,width,height):
        imageHeight, imageWidth = self.image.shape[:2]
        centerHeight = int(imageHeight/2)
        centerWidth = int(imageWidth/2)
        self.image = self.image[int(centerHeight-(height/2)):int(centerHeight+(height/2)), int(centerWidth-(width/2)):int(centerWidth+(width/2))] 
    
    def show(self):
        cv2.imshow("woof",self.image)
        cv2.waitKey(0)

