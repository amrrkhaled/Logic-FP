from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import sys
from PyQt5.QtGui import QImage, QPixmap,QIcon,QColor
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from pyzbar.pyzbar import decode
import numpy as np
from cv import ComputerVision
from wifioop import WifiCommunication
from ps4controlleroop import GameController
import pygame
import json
import struct
import os
import threading


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        
        palette = QtGui.QPalette()

        # Load the image as a QImage and convert it to RGB
        image = QtGui.QImage("imgs/mono-background.jpg")
        image = image.convertToFormat(QtGui.QImage.Format_RGB888)
        
        # Get the window size
        window_size = 2.2*MainWindow.size()

        # Calculate the scaled image
        scaled_image = image.scaled(window_size, 16, Qt.FastTransformation)

        # Create a QPixmap from the QImage
        background_image = QtGui.QPixmap.fromImage(scaled_image)

        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(background_image))
        MainWindow.setPalette(palette)
        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(780, 50, 400, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 800, 400, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 750, 400, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 750, 400, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 800, 400, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(800, 710, 400, 100))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1430, 710, 400, 100))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(120, 860, 400, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")


        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1030,800, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
       
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        
        
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(885, 800, 70, 70))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(885, 900, 70, 70))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 900, 70, 70))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1020, 900, 70, 70))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 875, 70, 70))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(750, 800, 70, 70))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1550, 810, 70, 70))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1550, 900, 70, 70))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(1450, 855, 70, 70))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(1650, 855, 70, 70))
        self.pushButton_10.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Add a QLabel to display the webcam feed
        self.webcam_label = QLabel(self.centralwidget)
        self.webcam_label.setGeometry(620, 125, 700, 600)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.label.setStyleSheet("color: black;font-family: Consolas;")
        self.label_2.setStyleSheet("color: black;font-weight: bold;font-family: Consolas;")
        self.label_3.setStyleSheet("color: black;font-weight: bold;font-family: Consolas;")
        self.label_4.setStyleSheet("color: black;font-weight: bold;font-family: Consolas;")
        self.label_5.setStyleSheet("color: black;font-weight: bold;font-family: Consolas;")
        self.label_6.setStyleSheet("color: black;font-weight: bold;font-family: Consolas;")
        self.label_7.setStyleSheet("color: black;font-weight: bold;font-family: Consolas;")
        self.label_8.setStyleSheet("color: black;font-weight: bold;font-family: Consolas;")
        self.label_9.setStyleSheet("color: black;font-weight: bold;font-family: Consolas;")

        
        self.pushButton.setIconSize(QtCore.QSize(60, 60))  # Set a larger size for the icon
        self.pushButton.setFlat(True)
        self.pushButton_2.setIconSize(QtCore.QSize(60, 60))  # Set a larger size for the icon
        self.pushButton_2.setFlat(True) 
        self.pushButton_3.setIconSize(QtCore.QSize(60, 60))  # Set a larger size for the icon
        self.pushButton_3.setFlat(True) 
        self.pushButton_4.setIconSize(QtCore.QSize(60, 60))  # Set a larger size for the icon
        self.pushButton_4.setFlat(True)
        self.pushButton_5.setIconSize(QtCore.QSize(60, 60))  # Set a larger size for the icon
        self.pushButton_5.setFlat(True)
        self.pushButton_6.setIconSize(QtCore.QSize(60, 60))  # Set a larger size for the icon
        self.pushButton_6.setFlat(True)
        self.pushButton_7.setIconSize(QtCore.QSize(60, 60))  # Set a larger size for the icon
        self.pushButton_7.setFlat(True)
        self.pushButton_8.setIconSize(QtCore.QSize(60, 60))  # Set a larger size for the icon
        self.pushButton_8.setFlat(True)
        self.pushButton_9.setIconSize(QtCore.QSize(60, 60))  # Set a larger size for the icon
        self.pushButton_9.setFlat(True)
        self.pushButton_10.setIconSize(QtCore.QSize(60, 60))  # Set a larger size for the icon
        self.pushButton_10.setFlat(True)
        
        self.pushButton.setIcon(QtGui.QIcon('imgs/up-arrow.png'))  
        self.pushButton_2.setIcon(QtGui.QIcon('imgs/down-arrow.png'))
        self.pushButton_3.setIcon(QtGui.QIcon('imgs/left-arrow.png'))
        self.pushButton_4.setIcon(QtGui.QIcon('imgs/right-arrow.png'))
        self.pushButton_5.setIcon(QtGui.QIcon('imgs/joystick.png'))
        self.pushButton_6.setIcon(QtGui.QIcon('imgs/stop2.png'))
        self.pushButton_7.setIcon(QtGui.QIcon('imgs/up-gripper.png'))
        self.pushButton_8.setIcon(QtGui.QIcon('imgs/down-gripper.png'))
        self.pushButton_9.setIcon(QtGui.QIcon('imgs/hold.png'))
        self.pushButton_10.setIcon(QtGui.QIcon('imgs/release.png'))



        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(1025,850, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
   
    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot Simulator"))
        self.label.setText(_translate("MainWindow", "Camera View"))
        self.label_2.setText(_translate("MainWindow", "Target Coordinates"))
        self.label_3.setText(_translate("MainWindow", "Current Coordinates"))
        self.label_4.setText(_translate("MainWindow", "(0,0)"))
        self.label_5.setText(_translate("MainWindow", "(0,0)"))
        self.label_6.setText(_translate("MainWindow", "Motion Control"))
        self.label_7.setText(_translate("MainWindow", "Gripper Control"))
        self.label_9.setText(_translate("MainWindow", "Speed: 0"))


        
    
  

    

class RobotSimulator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.simulator=ComputerVision()
        self.communication=WifiCommunication()
        self.wificonnect()
        self.setup_slider()
        
        #####################################################################
        self.button_keys = {}
        self.running = True
        

        pygame.init()
        self.initialize_controller()
        self.load_button_mapping("ps4_keys.json")
        self.joystick_thread = threading.Thread(target=self.run)
        self.joystick_thread.daemon = True  # Allow the thread to exit when the main program exits

        # Start the joystick input thread
        self.joystick_thread.start()
        # self.run()
        ########################################################################
      
        # Set the focus policy to receive key events
        self.setFocusPolicy(Qt.StrongFocus)

       
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.videocapture)

    # Thread for recieving coordinates
        # self.navigation_thread = threading.Thread(target=self.navigation)
        # self.navigation_thread.daemon = True  # Allow the thread to exit when the main program exits
        # # self.timer.timeout.connect(self.navigation)

        # # Start the navigation thread
        # self.navigation_thread.start()
      
     ################################################################################### 
        self.timer.start(30)  # Set the timer interval (in milliseconds)
        self.myData_old=None
       
        # Icon to the Window
        app_icon = QIcon("imgs/robot(1).png")  
        self.setWindowIcon(app_icon)



        
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            print("Up arrow key pressed")
            self.ui.pushButton.animateClick()
            self.ui.label_8.setText("Forward")
            self.data = 0b00001  # Use an integer
            self.communication.send(self.data)

        elif key == Qt.Key_Down:
            print("Down arrow key pressed")
            self.ui.pushButton_2.animateClick()
            self.ui.label_8.setText("Backward")
            self.data = 0b00010  # Use an integer
            self.communication.send(self.data)


        elif key == Qt.Key_Left:
            print("Left arrow key pressed")
            self.ui.pushButton_3.animateClick()
            self.ui.label_8.setText("Left")
            self.data = 0b00100  # Use an integer
            self.communication.send(self.data)

        elif key == Qt.Key_Right:
            print("Right arrow key pressed")
            self.ui.pushButton_4.animateClick()
            self.ui.label_8.setText("Right")
            self.data = 0b01000  # Use an integer
            self.communication.send(self.data)

        elif key == Qt.Key_S:
            print("Robot Stopped")
            self.ui.pushButton_6.animateClick()
            self.ui.label_8.setText("Robot Stopped")
        elif key == Qt.Key_U:
            print("Gripper Up")
            self.ui.pushButton_7.animateClick()
            self.ui.label_8.setText("Gripper Up")
        elif key == Qt.Key_D:
            print("Gripper Down")
            self.ui.pushButton_8.animateClick()
            self.ui.label_8.setText("Gripper Down")
        elif key == Qt.Key_H:
            print("Box Holding")
            self.ui.pushButton_9.animateClick()
            self.ui.label_8.setText("Holding")
        elif key == Qt.Key_R:
            print("Box Releasing")
            self.ui.pushButton_10.animateClick()
            self.ui.label_8.setText("Releasing")

    #################################################################################################
    

    
        

    def initialize_controller(self):
        self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        for joystick in self.joysticks:
            joystick.init()
   

    def load_button_mapping(self, button_mapping_file):
        with open(button_mapping_file, 'r') as file:
            self.button_keys = json.load(file)

    def handle_button_press(self, button_id):
        control = None
        for key, value in self.button_keys.items():
            if button_id == value:
                control = key
                break
        if control:
            print(f"{control} pressed")
        if control == "up_arrow":
            self.ui.label_8.setText("Forward")
            self.data = 0b00001  # Use an integer
            self.communication.send(self.data)
        if control == "down_arrow":
            self.ui.label_8.setText("Backward")
        if control == "left_arrow":
            self.ui.label_8.setText("Left")
        if control == "right_arrow":
            self.ui.label_8.setText("Right")
        if control == "right_stick_click":
            self.ui.label_8.setText("Robot Stopped")





    def handle_button_release(self, button_id):
        control = None
        for key, value in self.button_keys.items():
            if button_id == value:
                control = key
                break
        if control:
            print(f"{control} released")
            self.data = 0b00111  # Use an integer
            # self.communication.send(self.data)


    def run(self):
        self.running = True
        while self.running:
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.JOYBUTTONDOWN:
                    self.handle_button_press(event.button)
                elif event.type == pygame.JOYBUTTONUP:
                    self.handle_button_release(event.button)
                
        pygame.quit()

 ###################################################################################################3       


    def videocapture(self):
        ret, frame = self.simulator.OpenCamera()
        
        if ret:
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format_BGR888)
            pixmap = QPixmap.fromImage(q_image)
            self.ui.webcam_label.setPixmap(pixmap)

            myData = self.simulator.QrReader(frame)
            
            if myData is not None:
                if myData != self.myData_old:  # Check if the data has changed
                    self.myData_old = myData  # Update the previous data
                    print("QR Code Data:", myData)  # Debug statement
                    self.ui.label_5.setText(str(myData))
        else:
            print("Failed to capture frame from the webcam")  
    
    def wificonnect(self):
        self.communication.connect()

    def navigation(self):
        while True:
            self.coordinates=self.communication.received()
            self.ui.label_4.setText(self.coordinates)
    

    def setup_slider(self):
        self.ui.horizontalSlider.setMinimum(0)
        self.ui.horizontalSlider.setMaximum(255)
        self.ui.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.ui.horizontalSlider.setTickInterval(10)
        self.ui.horizontalSlider.valueChanged.connect(self.update_slider_value)

    def update_slider_value(self, value):
        self.ui.label_9.setText(f"Speed: {value}")    




        
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = RobotSimulator()
    MainWindow.show()
    MainWindow.showMaximized()
    sys.exit(app.exec_())

