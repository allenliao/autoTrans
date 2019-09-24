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
    screenRegion.find("ie.png").click()
    screenRegion.find(Pattern("addressBar.png").similar(0.6)).click()
    screenRegion.find(Pattern("addressBar.png").similar(0.6)).type("https://ibsbjstar.ccb.com.cn/CCBIS/V6/common/login.jsp")
    screenRegion.find("navBtn.png").click()


    
    

if __name__ == "__main__":
    screenRegion = Screen()
    readConfig()
    #getTableInfo()
    #load config
    #login
    
    #observeFunc(folder_tblRegion)
    #observeFunc(file_tblRegion)