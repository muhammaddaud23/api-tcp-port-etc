#!/usr/bin/env python3

"""
This code is used to get data directly from specified HOST and PORT
The data is stored and plotted after user press ctrl+c key
"""

import socket
import numpy as np
import time
import matplotlib.pyplot as plt

HOST = '127.0.0.1'
PORT = 50080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_inet untuk IPv4, sedangkan SOCK_stream untuk tcp
s.connect((HOST, PORT))

start_time = time.time()
result = np.array([])

try:
	while True:
		msg = s.recv(512)
		tem = np.frombuffer(msg,dtype=np.float32)
		result = np.concatenate([result,tem])
		#print(type(tem))
except KeyboardInterrupt:
	pass

print(len(tem))
duration = start_time - time.time()

y = np.array(result)
x = np.linspace(0,duration,len(result))
plt.scatter(x,y,color='black')
plt.xlabel('Time')
plt.ylabel('Strength')
plt.show()
