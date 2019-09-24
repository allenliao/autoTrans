import json
from sikuli.Sikuli import *
from java.awt import Robot
from java.awt import Color
from java.awt import Rectangle


tableList=[]

def readConfig():
    Settings.ObserveScanRate = 0.2# the observer will look every 5 seconds
    buConfigFile = open('buconfig.json','r')
    #buconfigFile.read()
    buConfigStr=buConfigFile.read()
    #print buConfigStr
    
    buConfigObj=json.loads(buConfigStr)
    buurl=buConfigObj['buurl']
    username=buConfigObj['username']
    password=buConfigObj['password']
    
    openWebSiter(buurl)
    #loginAndOpenGame(username,password)

def openWebSiter(buurl):
    #buurl="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe "+buurl
    #buurl="C:\Program Files\Internet Explorer\iexplore.exe "+buurl
    #print buurl
    #openApp(buurl)
    screenRegion.find("ie.png").click()


    
    

if __name__ == "__main__":
    screenRegion = Screen()
    readConfig()
    #getTableInfo()
    #load config
    #login
    
    #observeFunc(folder_tblRegion)
    #observeFunc(file_tblRegion)