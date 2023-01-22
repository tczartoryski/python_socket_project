# Python Socket Project
A python project that demonstrates an understanding of network communication protocols. Python is used to implement the client side of a network application design according to the client-server application architecture.  This program establishes a TCP connection with a server running on a remote machine that is constantly listening for TCP connection requests.

After an initial greeting message used by the client to establish a connection with the server, the server asks the client to evaluate a random number of arithmetic expressions. These expressions are sent in messages to the client one at a time, each time the server expects a response message from the client containing the result of expression sent. If the client sends a result message that is incorrect, a failure message will be sent to the client and the connection closed. After a certain number of expressions are evaluated the server returns a flag, this flag is saved and the connection is closed and the application is terminated. 


# High Level Approach of Client :
 In order to know where to send and receive data from, a server ID has to be created by taking the server name and port number and combining them into a tuple.
 The client socket ( which communicates with the server) is created so a connection can be established.
An introduction message is sent to the server to authenticate the sender and start communication.
The introduction message sent to the server is encoded from string into bytes.
The program utilizes a while loop , where the client will listen for expression messages from the server.These messages have a header followed by a mathematical expression.
 
 Once the message is received from the server , it is decoded from bytes back into string format. The mathematical expression is isolated from the message and then evaluated using the eval() function. The solution is then attached to a header, encoded into bytes and sent to the server. This process repeats until the secret flag is sent back. A flag message is identfied by the client by checking the header of each message until the header corresponding to the flag is recognized. The program then breaks out of the while loop, the socket is closed, and theconnection is terminated.
