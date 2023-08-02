import os
import socket
import pyqrcode
import webbrowser
from time import sleep
from pyqrcode import QRCode
from http.server import CGIHTTPRequestHandler, HTTPServer


hostname = socket.gethostname()                     # PC NAME
print(f"Your PC name is {hostname}")

ip = socket.gethostbyname(hostname)                 # GET IP ADDRESS
serverPort = 8080
print(f"Your current IP address = {ip}")

current_directory = os.getcwd()                     # CURRENT DIR PATH  
print(f"You are sharing content in {current_directory}")

webServer = HTTPServer(("", serverPort), CGIHTTPRequestHandler)
print("Server started http://%s:%s" % (ip, serverPort),)        # SERVER ADDRESS

try:
    url = pyqrcode.create(f"http://{ip}:{serverPort}")
    url.png("myqr.png", scale=8)                                # QR CODE CREATED IN PNG
    sleep(2)
    webbrowser.open("myqr.png")
    webServer.serve_forever()
except KeyboardInterrupt:
    pass                                                        #  "Ctrl + C" to stop server                                     

webServer.server_close()
print("Server stopped.")