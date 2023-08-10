import numpy as np
import cv2
import pyautogui as pag
import datetime, os

class SSApp:

    def __init__(self):
        
        self.mainController = pag.screenshot()

        self.outputFolder = "./ScreenShots"
        isExist = os.path.exists(self.outputFolder)

        if not isExist:
            os.mkdir(self.outputFolder)

    def _takeScreenShot(self):

        try:
            self.GetImg = cv2.cvtColor(np.array(self.mainController), cv2.COLOR_RGB2BGR)
            getTime = datetime.datetime.now().strftime("%I_%M_%S_%p")
            fileName = str(self.outputFolder)+"/Screen_Shot_"+str(getTime)+".png"
            cv2.imwrite(fileName, self.GetImg)
            return fileName
        except:
            return False

    def runModule(self):
        action = self._takeScreenShot()

        if action != False:
            print(action)
        else:
            print("Error found.")


classObj = SSApp()
classObj.runModule()
