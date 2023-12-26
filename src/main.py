from InstaApi import IntaApid
from ImageApi import PhotoApi
from imageManipulator import ImageManipulator
from utils import *

wof = ImageManipulator()

wof.loadImage("https://images.pexels.com/photos/7055165/pexels-photo-7055165.jpeg")
wof.cutImageCenter(1080,1080)
wof.show()
