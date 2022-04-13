import socket
from math import *
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

#Handle Input
def string_check(inpcheck):
  check=True
  try:
    eval(inpcheck)
  except (SyntaxError,NameError,TypeError,ValueError) as e:
    check=False
  return check    
    

#Without variable
def withoutV():
    while True:
        try:
            print("Input math expressions:")
            inp_user=input()
            if(inp_user=="q" or  inp_user=="Q"):       
                break
            check_string=string_check(inp_user)
            if check_string==True:
                send(inp_user)
            else:       
                send("fail")
        except (SyntaxError,NameError,TypeError,ValueError,ZeroDivisionError) as e:
            print("Please enter correct format integer")    
            print()
            
#With variable
def withV():
    while True:
        print("Number of variable")   
        num_variable=0
        try:
            try:
                num_variable=int(input())
                if(num_variable=="q" or  num_variable=="Q"):       
                    break
            except (SyntaxError,NameError,TypeError,ValueError) as e:
                print("variable number must be Integer")
                print()
                break            
            print()
            var=[]
            alp=[]
            for i in range(1,num_variable+1):
                number=int(input(f"{chr(65+i-1)} : "))
                if(number=="q" or  number=="Q"):       
                        break
              
                alp.append(chr(65+i-1))
                var.append(number)
            print("Input math expressions:")
            inp_user=input()
            for i in range (0,len(alp)):
                inp_user=inp_user.replace(alp[i],str(var[i]))
            if(inp_user=="q" or  inp_user=="Q"):       
                break
            check_string=string_check(inp_user)
            if check_string==True:
                send(inp_user)
            else:       
                send("fail")
        except (SyntaxError,NameError,TypeError,ValueError) as e:
            print("Please enter correct format integer")
            print()
      
    
#Main    
print("Hello, thank you for using one line calculator!")
while True:
    print("Select Mode")
    print("A) With Variable")
    print("B) Without Variable")
    print("(INPUT 'A' or 'B' to process next step )")
    print("- Input q to quit calculator -")
    inp_mode=input()
    if(inp_mode=="B" or inp_mode=="b"):
        withoutV()
    elif(inp_mode=="A" or inp_mode=="a"):
        withV()
    elif(inp_mode=="q" or  inp_mode=="Q"):    
            break
    else:
         print("Please select mode")    
    