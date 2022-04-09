from re import X
import socket 
import threading
from unittest import result

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                 bye="Thank you comeback later!"
                 conn.send(bye.encode(FORMAT))
                 connected = False

            print(f"[{addr}] {msg}")
            
            res=calculator(msg)
            print(res)
            conn.send(str(res).encode(FORMAT))

    conn.close()

def brackets(Allexp,Oneexp):
        result=""
        leng=len(Oneexp)
        for i in range(0,leng):
            if(i==leng-1):
                break
            if Allexp[i]=="+":
                result=float(Oneexp[i-1])+float(Oneexp[i+1])
                i=i+1
            if Allexp[i]=="-":
                result=float(Oneexp[i-1])-float(Oneexp[i+1])
                i=i+1
            if Allexp[i]=="/":
                result=float(Oneexp[i-1])/float(Oneexp[i+1])
                i=i+1
            if Allexp[i]=="*":
                result=float(Oneexp[i-1])*float(Oneexp[i+1])
                i=i+1
        return result

def numparser(Allexp):
        leng=len(Allexp)
        print(leng)
        arrnum=[]
        num=""
        x=0
        for i in range(leng):
            print(num)
            if(Allexp[i]=="+" or Allexp[i]=="-" or Allexp[i]=="*" or Allexp[i]=="/" or Allexp[i]=="(" or Allexp[i]==")" or i==leng-1):
                if(num==""):
                    num=Allexp[i]
                elif(Allexp[i]!="+" and Allexp[i]!="-" and Allexp[i]!="*" and Allexp[i]!="/" and Allexp[i]=="(" and Allexp[i]==")"):
                    num=num+Allexp[i]
                print("masuk")
                arrnum.append(num)
                num=""
            if(Allexp[i]!="+" and Allexp[i]!="-" and Allexp[i]!="*" and Allexp[i]!="/" and Allexp[i]!="(" and Allexp[i]!=")"):
                    num=num+Allexp[i]
               
                 
        return arrnum
        
def operatorparser(Allexp):
        leng=len(Allexp)
        arrop=[]
        for i in range(0,leng):
            if(Allexp[i]=="+" or Allexp[i]=="-" or Allexp[i]=="*" or Allexp[i]=="/" or Allexp[i]=="(" or Allexp[i]==")"):
                    arrop.append(Allexp[i])
          
        return arrop

def checkbranch(exp):
    res=""
    for i in range (0,len(exp)):
        if(exp[i]=="("):
            x=i+1
            for x in range (x,len(exp)):
                if(exp[x]==")"):
                    print("dalam: "+res)
                    temp=res
                    res=calculator(res)
                    print("hasil bracket "+str(res))
                    return exp.replace("("+temp+")",str(res))
                elif(exp[x]=="("):
                    exp=exp.replace(exp[x:len(exp)],checkbranch(exp[x:len(exp)]))
                    print("bracket dalam:"+exp)
                    res=res+exp[x]
                else:
                    res=res+exp[x]
    return exp                
            
def calculator(Allexp):
        leng=len(Allexp)
        brch=checkbranch(Allexp)
        if(str(brch).find("(") and str(brch)!=None):
            str(brch).replace("(","")         
            str(brch).replace(")","")
        print("string jadi "+str(brch))
        Allexp=str(brch)
        arrnum=numparser(Allexp)
        print(arrnum)
        arrop=operatorparser(Allexp)
        print(arrop)
        res=arrnum[0]
        for i in range (0,len(arrop)):
              if(arrop[i]=="+"):
                  res=float(res)+float(arrnum[i+1])
              if(arrop[i]=="-"):
                  res=float(res)-float(arrnum[i+1])
              if(arrop[i]=="/"):
                  res=float(res)/float(arrnum[i+1])
              if(arrop[i]=="*"):
                  res=float(res)*float(arrnum[i+1])  
        return res            

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()