import socket
from _thread import *

#initial set up and direct dec of what port and sever ip to host
sever='' #need ipv4 address of hosting comp for local connections 
port=5555




#sets up type of socket and general initialization 
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#bind the socket to a sever and a port
try:
    soc.bind((sever,port))
except socket.error as e:
    str(e)

#sets the amount of instances allowed to connect and opens up the port
soc.listen(2)

def Client_Threaded(connection):
    conn.send(str.encode("Connected"))


    response=""
    #uses while loop to keep connection with client
    while True:
        #check response
        try:
            #sets the amounts of bits passed between sever and client 
            data=conn.recv(3000)
            response=data.decode("utf-8")

            #checks data 
            if data is None:
                print("Connection lost")
                break
            else:
                print("Data Received: ", response)

            conn.sendall(str.encode(response))
        except:
            break

    print("Con Lost")
    #Closes connection to allow for it to be reopened later
    conn.close()

while True:
    conn, addr=soc.accept()
    print("Client Connected: "conn)

    start_new_thread(Client_Threaded, (conn,))