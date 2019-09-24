# -*- coding: utf-8 -*-
import json
from sikuli.Sikuli import *
from java.awt import Robot
from java.awt import Color
from java.awt import Rectangle

#設定編碼
reload(sys)
sys.setdefaultencoding('utf-8')
#獲得系統編碼格式
type = sys.getfilesystemencoding()
tableList=[]
class TargetObj:
    targetName="Allen"
    targetAcc="BU001"
    targetAmount="0.01"
    def __init__(self, _targetName, _targetAcc, _targetAmount):
        print(" Create TargetObj!!")
        self.targetName = _targetName
        self.targetAcc = _targetAcc
        self.targetAmount=_targetAmount


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
    kpassword=buConfigObj['kpassword']

    targetObj=TargetObj("陈智铭", "6216911304021889", "0.01")
    
    openWebSiter(buurl,username,password,kpassword,targetObj)
    #loginAndOpenGame(username,password)

def openWebSiter(buurl,username,password,kpassword,targetObj):
    if screenRegion.exists("ie_win7.png"):
        screenRegion.find("ie_win7.png").click()
        wait("addressBar_win7.png", 2)
        screenRegion.find("addressBar_win7.png").click()
        wait("addressBar_win7.png", 2)
        paste(targetObj.targetName.encode(type))
        #screenRegion.find("addressBar_win7.png").type(buurl)
        screenRegion.find(Pattern("navBtn_win7.png").similar(0.9)).click()
    else:
        screenRegion.find("ie.png").click()
        screenRegion.find(Pattern("addressBar.png").similar(0.6)).click()
        paste(buurl)
        screenRegion.find("navBtn.png").click()

    #wait("loginBtn.png", 2)

    if screenRegion.exists("accountExist.png"):
        print(" account Exist!!")
        screenRegion.find(Pattern("passwordInput.png").similar(0.7)).click()
        screenRegion.find(Pattern("passwordInput.png").similar(0.7)).type(password)
        screenRegion.find("loginBtn.png").click()
        #screenRegion.find("accountExist.png").click()
        #screenRegion.find(Pattern("clearAccountInputBtn.png").similar(0.4)).click()
    else: 
        print(" account not Exist!!")
        screenRegion.find("accountInput.png").paste(username)

        if screenRegion.exists("passwordInputExist.png"):
            print(" passwordInput Exist!!")
            screenRegion.find("loginBtn.png").click()
        else:
            print(" passwordInput not Exist!!")
            screenRegion.find(Pattern("passwordInput.png").similar(0.)).click()
            screenRegion.find(Pattern("passwordInput.png").similar(0.9)).type(password)
            screenRegion.find("loginBtn.png").click()

    wait("transTab.png", 5)
    screenRegion.find(Pattern("transTab.png").similar(0.7)).hover()
    wait(Pattern("transBtn.png").similar(0.9), 2)
    screenRegion.find(Pattern("transBtn.png").similar(0.9)).click()


    wait("transTab.png", 3)
    screenRegion.type(Key.PAGE_DOWN)
    wait("targetNameInput.png", 2)
    screenRegion.find(Pattern("targetNameInput.png").similar(0.9)).click()
    screenRegion.find(Pattern("targetNameInput.png").similar(0.9)).paste(targetObj.targetName.encode("utf-8"))

    screenRegion.find(Pattern("targetAccInput.png").similar(0.9)).click()
    screenRegion.find(Pattern("targetAccInput.png").similar(0.9)).type(targetObj.targetAcc)

    screenRegion.find(Pattern("targetAmountInput.png").similar(0.9)).click()
    screenRegion.find(Pattern("targetAmountInput.png").similar(0.9)).type(targetObj.targetAmount)
    

    


    
    

if __name__ == "__main__":
    screenRegion = Screen()
    readConfig()
    #getTableInfo()
    #load config
    #login
    
    #observeFunc(folder_tblRegion)
    #observeFunc(file_tblRegion)