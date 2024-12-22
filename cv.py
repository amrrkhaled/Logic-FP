import cv2
import numpy as np
from pyzbar.pyzbar import decode

class ComputerVision:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.myData = None  # Initialize myData

    def OpenCamera(self):
        # self.cap = cv2.VideoCapture(0)
        success, img = self.cap.read()
        return success, img

    def QrReader(self, img):
        for qrCode in decode(img):
            self.myData = qrCode.data.decode('utf-8')
            pts = np.array([qrCode.polygon], np.int32)
            pts = pts.reshape(-1, 1, 2)
            # cv2.polylines(img, [pts], True, (255, 0, 0), 5)
        return self.myData

    # def close(self):
    #     self.cap.release()
