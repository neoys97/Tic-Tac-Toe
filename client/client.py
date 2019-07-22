import socket                
import threading
import UI
connection = socket.socket()          

def receive():
   global connection
   try:
      while not UI.endGame:
         msg = connection.recv(1024).decode()
         if (msg):
            print("received message:", msg)
            msg = msg.split(":")
            newBoard = []
            for info in msg:
               newBoard.append(list(info))
            UI.boardInfo = newBoard
            UI.updateBoard()
            UI.my_turn = True
            if (UI.endGame):
               break
   finally:
      print("closing connection...")
      connection.close()

def send(connection):
   msg = ""
   for ele in UI.boardInfo:
      msg += "".join(ele)
      msg += ":"
   print (msg[:-1])
   connection.send(msg[:-1].encode())
   
def main():
   address = '127.0.0.1'
   port = 12345                

   connection.connect((address, port)) 
   print ("Connected to the server at", address)
   t = threading.Thread(target=receive)
   t.start()

   UI.start(connection)

if __name__ == "__main__":
   main()
