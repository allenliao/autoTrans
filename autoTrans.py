#!/usr/bin/python
# -*- coding: utf-8 -*- 

import json
import urllib
from sikuli.Sikuli import *
from java.awt import Robot
from java.awt import Color
from java.awt import Rectangle

# 使得 sys.getdefaultencoding() 的值为 'utf-8'  
reload(sys)                      # reload 才能调用 setdefaultencoding 方法  
#sys.setdefaultencoding('utf-8')  # 设置 'utf-8'  
#獲得系統編碼格式
_type = sys.getfilesystemencoding()

#s=urllib.urlopen('http://bj.58.com/hezu/')

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
    targetName=["targetName"]

    targetObj=TargetObj("陈智铭", "6216911304021889", "0.01")
    print targetObj.targetName.decode("utf-8").encode('gb18030') #utf-8 gb18030 GB2312 Unicode


    openWebSiter(buurl,username,password,kpassword,targetObj)


def openWebSiter(buurl,username,password,kpassword,targetObj):
    paste(targetObj.targetName.decode("utf-8"))

    if screenRegion.exists("ie_win7.png"):
        screenRegion.find("ie_win7.png").click()
        wait("addressBar_win7.png", 2)
        screenRegion.find("addressBar_win7.png").click()
        wait("addressBar_win7.png", 2)
        paste(targetObj.targetName.decode("utf-8"))
        #screenRegion.find("addressBar_win7.png").type(buurl)
        screenRegion.find(Pattern("navBtn_win7.png").similar(0.9)).click()
    else:
        screenRegion.find("ie.png").click()
        wait(Pattern("addressBar.png").similar(0.8), 10)
        screenRegion.find(Pattern("addressBar.png").similar(0.8)).click()
        wait("addressBar.png", 2)
        #paste(buurl)
        paste(targetObj.targetName.decode("utf-8").encode('gb18030'))
        wait("navBtn.png", 2)
        screenRegion.find(Pattern("navBtn.png").similar(0.7)).click()

    #wait("loginBtn.png", 2)
    sleep(5)

    if screenRegion.exists("accountExist.png"):
        print(" account Exist!!")
        screenRegion.find(Pattern("passwordInput.png").similar(0.7)).click()
        screenRegion.find(Pattern("passwordInput.png").similar(0.7)).type(password)
        screenRegion.find("loginBtn.png").click()
        #screenRegion.find("accountExist.png").click()
        #screenRegion.find(Pattern("clearAccountInputBtn.png").similar(0.4)).click()
    else: 
        print(" account not Exist!!")
        screenRegion.find("accountInput.png").click()
        paste(username)

        #if screenRegion.exists(Pattern("passwordInputExist.png").similar(0.9)):
        #    print(" passwordInput Exist!!")
        #    screenRegion.find("loginBtn.png").click()
        #else:
        print(" passwordInput not Exist!!")
        screenRegion.find(Pattern("passwordInput.png").similar(0.9)).click()
        paste(password)
        screenRegion.find("loginBtn.png").click()

    sleep(5)
    #wait("transTab.png", 5)
    screenRegion.find(Pattern("transTab.png").similar(0.7)).hover()
    sleep(2)
    screenRegion.find(Pattern("transBtn.png").similar(0.7)).click()

    sleep(5)
    #wait("transPage.png", 8)
    screenRegion.type(Key.PAGE_DOWN)
    screenRegion.find(Pattern("targetNameInput.png").similar(0.98)).click()
    paste(targetObj.targetName.decode("utf-8"))

    screenRegion.find(Pattern("targetAccInput.png").similar(0.9)).click()
    screenRegion.find(Pattern("targetAccInput.png").similar(0.9)).type(targetObj.targetAcc)

    screenRegion.find(Pattern("targetAmountInput.png").similar(0.9)).click()
    screenRegion.find(Pattern("targetAmountInput.png").similar(0.9)).type(targetObj.targetAmount)

    screenRegion.find(Pattern("nextBtn.png").similar(0.7)).click()
    

    


    
    

if __name__ == "__main__":
    screenRegion = Screen()
    readConfig()
    #getTableInfo()
    #load config
    #login
    
    #observeFunc(folder_tblRegion)
    #observeFunc(file_tblRegion)