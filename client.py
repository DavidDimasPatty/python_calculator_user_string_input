import socket

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

def string_check(inpcheck):
    brackets=0
    res=True
    operator=["+","-","/","*"]
    num=["0","1","2","3","4","5","6","7","8","9"]
    for i in range (0,len(inpcheck)):
        if(i==len(inpcheck)-1 and brackets!=0):
            res=False
            break
        if(inpcheck[i]=='('):
            brackets=brackets+1
            if(inpcheck[i-1] in num and i!=0):
                res=False
                break
            if(inpcheck[i+1] in operator and i!=len(inpcheck)-1):
                res=False
                break
        if(inpcheck[i]==')'):
            brackets=brackets-1
            if(inpcheck[i+1] in num and i!=len(inpcheck)-1):
                res=False
                break
            if(inpcheck[i-1] in operator and i!=0):
                res=False
                break
        if(inpcheck[i] in operator):
            if(inpcheck[i-1] in operator and i!=0):
                res=False
                break
            if(inpcheck[i+1] in operator and i!=len(inpcheck)-1):
                res=False
                break
    return res    
    
    
print("Hello, thank you for using one line calculator!")
print("input q to quit calculator")
while True:
    print("Input math expressions:")
    inp_user=input()
    if(inp_user=="q"):       
        send(DISCONNECT_MESSAGE)
        break
    check_string=string_check(inp_user)
    if check_string==True:
        send(inp_user)
    else:       
        send("fail")
    