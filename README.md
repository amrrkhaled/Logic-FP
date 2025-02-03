# Robot Control System with PyQt5 GUI

## Overview

This project is a robotic control system featuring a **Python GUI (PyQt5)** that communicates with a robot over **WiFi (ESP)**. The system provides multiple control mechanisms, including:

- **Joystick Control:** Sends movement commands to the robot.
- **IMU-based Glove Control:** Tracks hand movements via an **IMU sensor** in a glove to control the robot.
- **Camera Feedback:** Displays real-time camera feed from the robot in the GUI.
- **QR Code Scanning:** Detects and processes QR codes from the camera feed.

## Features

- 🕹️ **Joystick-based control** for smooth movement.
- ✋ **IMU-based glove control** to move the robot by hand gestures.
- 📡 **WiFi communication with ESP module** for seamless robot commands.
- 🎥 **Live camera feed** displayed in the GUI.
- 🔍 **QR code scanning** capability.

## Technologies Used

- **Python** (for the GUI and logic)
- **PyQt5** (for the graphical interface)
- **ESP8266/ESP32** (for WiFi communication)
- **OpenCV** (for camera processing and QR scanning)
- **IMU Sensor** (for gesture-based control)
- **Joystick Module** (for manual control)

## Installation

### Prerequisites
Ensure you have the following installed:

- Python 3.x
- `PyQt5`
- `opencv-python`
- `pyserial`
- `numpy`

### Setup
 Clone the repository:
   ```sh
   git clone https://github.com/amrrkhaled/Logic-FP.git
   cd your-repo
