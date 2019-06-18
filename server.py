import socket
import pickle
import struct
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9999))

s.listen(5)
clientsocket, address = s.accept()
print(f"connection from {address} has been established")

while True:
    check, frame = cap.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    data = pickle.dumps(frame, 0)
    size = len(data)
    clientsocket.sendall(struct.pack(">L", size) + data)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break

cap.release()    

