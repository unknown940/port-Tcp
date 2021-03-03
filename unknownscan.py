import socket
print('''

 ____               __    ______                  
/\  _`\            /\ \__/\__  _\                 
\ \ \L\ \___   _ __\ \ ,_\/_/\ \/   ___   _____   
 \ \ ,__/ __`\/\`'__\ \ \/  \ \ \  /'___\/\ '__`\    
  \ \ \/\ \L\ \ \ \/ \ \ \_  \ \ \/\ \__/\ \ \L\ \     
   \ \_\ \____/\ \_\  \ \__\  \ \_\ \____\\ \ ,__/    
    \/_/\/___/  \/_/   \/__/   \/_/\/____/ \ \ \/     
                                            \ \_\    
                                             \/_/    
''')



host=input('Enter Ip Target\n===>')
for port in range (0,6553):
 a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 a.settimeout(0.1)
 b=a.connect_ex((host, port))
 if b == 0:
     print(port, 'is open')
     break
 else:
     print(port, 'is closed')
