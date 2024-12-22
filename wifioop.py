import socket
import struct

class WifiCommunication:
   def __init__(self):
    # ESP Access Point (AP) information
         self.esp_ssid = "esp_ap" 
         self.esp_password = "esp_password" 
         self.esp_ip = "192.168.4.1"   # The IP address of your ESP
   def connect(self):
        # Create a socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(5)

        # Connect to the ESP's access point
        self.s.connect((self.esp_ip, 80))  # 80 is a common port for HTTP on ESPs

   def send(self,data):     # Data to send
        self.data_to_send = struct.pack('B', data)
        # Send data
        self.s.send(self.data_to_send)
   
   def received(self):     # Data to send

        # Receive data from the ESP (if needed)
        self.received_data = self.s.recv(1024)
        # print("Received data:", received_data.decode())
        return self.received_data.decode()
        # Close the socket
#    def close(self):     
#         self.s.close()
