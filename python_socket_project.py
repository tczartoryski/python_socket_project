# Secret Flag: a7c02c63ef6b74777c3e8e10ada5a3c89b06538b1df2032ef177943eef443ca8
# Socket Package Is Imported
from socket import *


print( 'Client program started.' )

# Creates server ID using server info
server_name = 'phase.coe.neu.edu'
server_port = 12000
server_ID = ( server_name , server_port )

# Creates and connects client socket
client_socket = socket( AF_INET , SOCK_STREAM )
print( 'Client socket created.' )
client_socket.connect( server_ID )
print( 'Client socket connected.' )

# Creates Introduction Message
intro_message = "EECE2540 INTR 001583855"
print( 'Sent string:' , intro_message )

# Encodes string into bytes
# Sends message to server.
client_socket.send( intro_message.encode() )
print( 'Client sent message to server at:' , server_ID )

# While loop to evaluate expressions until told to terminate
while(True):
    # Receives message from server
    message_from_server = client_socket.recv( 2048 )
    print( 'Client received message from server at:' , server_ID )

    # Convert message (bytes) to  string.
    output_string = message_from_server.decode()
    # Display output string.
    print( 'Received string:' , output_string )

    # Terminates if header of output string is for a secret flag
    if output_string[:13] == 'EECE2540 SUCC' :
        break

    # Creates a message by concatenating the header onto the evaluation of the expression part of the ouput string
    result_message = "EECE2540 RSLT " + str(eval(output_string[14:]))
    print("Sent String: "+ result_message)
    client_socket.send(result_message.encode())

# Closes the client socket.
client_socket.close()
print( 'Client socket closed.' )

print( 'Client program terminated.' )
