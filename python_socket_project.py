
# Name: Thomas Czartoryski
# NUID: 001583855
# Secret Flag: a7c02c63ef6b74777c3e8e10ada5a3c89b06538b1df2032ef177943eef443ca8
# High Level Approach of Client :
#     In order to know where to send and receive data from
#     a server ID has to be created by taking the server name and port number
#     The client socket ( communicates with a server) is created so a connection is established
#     The first thing sent to the server is the introduction message to authenticate the sender and start communication
#     That message is first  encoded from string into bytes to send that message over
#     Program enters a while loop , therefore same instructions will be repeated unless told otherwise
#     The server will send over expression messages, these messages have a header followed by a mathematical expression
#     Once the message is received from the server , it is decoded back to string format (regular words)
#     The mathematical expression is isolated from the message and then evaluated using the eval() function
#     The solution is attached to a header and encoded and sent to the server
#     This process repeats until the secret flag is sent back
#     This is done by checking the header of each message until the header corresponding to the flag is recognized
#     The program then breaks out of the while loop, socket is closed, connection is terminated
#
# Testing of Program :
#     Multiple steps were taken to make the code error free
#     Output messages that print out the messages sent and recieved helped in debugging
#     The initial design of the program just had the introduction message and the evaluation of an expression
#     This was then scaled during a while loop, however I needed to know when the while loop would terminate
#     Initially I used a counter that stopped after 1000 expressions were evaluated
#     However, since I didnt know when the flag would appear this solution resulted in bugs
#     I then decided to have the while loop run indefinitely and then break out of the program after a certain criteria
#     Since I recently learned that strings are arrays and can be indexed I use that concept to check for headers
#     Initially, there was some confusion on how I could evaluate the expressions
#     I knew I needed to isolate the expression from the rest of the message to solve it
#     After a few ideas, I settled on using string indices
#     Upon research online I stumbled across the python eval () function which ended up working well and was not buggy
#     When I first tested my code I recieved an error because the flag message was being evaluated
#     I then decided to put the if statement/ break statement before the evaluation statement
#     After I finally got the secret flag on the sample server, I changed the server adress and tried on the actual server
#     And it worked on the first try on the actual server
#


print( 'Client program started.' )

# Socket Package Is Imported
from socket import *

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
