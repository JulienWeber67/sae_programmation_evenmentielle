"""import psutil
import socket
import platform

i=platform.system()
k=platform.release()
u=platform.platform()

print(f"nom:{i},version :{k},platform :{u}")
print('hostname :',socket.gethostname())

print('ram total :',psutil.virtual_memory()[0] , 'bits')
print('ram utilisé :',psutil.virtual_memory()[3], 'bits' )
print('ram restant :',psutil.virtual_memory()[4], 'bits')
print('The CPU usage is: ', psutil.cpu_percent(4),'%')"""
# import required modules
import os
import pyautogui

# prompts message on screen and gets the command
# value in val variable
value = pyautogui.prompt("Enter Shell Command")

# executes the command and returns
# the output in stream variable
stream = os.popen(value)

# reads the output from stream variable
out = stream.read()
pyautogui.alert(out)

#https://www.geeksforgeeks.org/run-shell-command-from-gui-using-python/