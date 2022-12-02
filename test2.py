import psutil
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
print('The CPU usage is: ', psutil.cpu_percent(4),'%')