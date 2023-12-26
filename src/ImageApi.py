import requests
import json
import random

class PhotoApi:
    def __init__(self,apiKey):
        self.mainUrl = "https://api.pexels.com/v1/"
        self.headers = {"Authorization":apiKey}

    def getPhoto(self,index,page,query,color):
        url = self.mainUrl + "search?query={}&page={}&color={}".format(query,page,color)
        r = requests.get(url,headers=self.headers).json()
        return r['photos'][index]

    def getRandomPhoto(self,query,color):
        index = random.randint(0,16)
        page = random.randint(0,300)
        return getPhoto(index,page,query,color)
    

