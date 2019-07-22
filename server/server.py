import socket                
import threading
import UI

connection = None

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
   global connection
   s = socket.socket()          

   port = 12345                

   s.bind(('', port))         

   s.listen(0)      
   print ("Socket is listening at port", port)            

   connection, addr = s.accept()

   print ('Got connection from', addr)

   t = threading.Thread(target=receive)
   t.start()
   
   UI.start(connection)

if __name__ == "__main__":
   main()
