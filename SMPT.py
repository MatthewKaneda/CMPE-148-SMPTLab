from socket import *
import smtplib
import base64

msg = "\r\n I love computer networks!"

endmsg = "\r\n.\r\n"

# Choose mail server and call it mailserver
mailserver = ("mail.smtp2go.com", 2525)

# Create socket called clientSocket and establish a TCP connection with mailserver

# Start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

# End

recv = clientSocket.recv(1024).decode()

print(f'Connection Request message: {recv}')

if recv[:3] != '220':
	print('220 reply not received from server')

# Send HELO command and print server response.

heloCommand = 'EHLO Alice\r\n'

clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024).decode()

print(recv1)

if recv1[:3] != '250':
	print('HELO: 250 reply not received from server')

# Login for SMTP server
username = "matthew.kaneda@sjsu.edu"
password = "cTVxOWh0MzEydWsw"

auth = (f'\x00{username}\x00{password}').encode()
auth_64 = base64.b64encode(auth)
auth_message = "AUTH PLAIN ".encode()+auth_64+"\r\n".encode()
clientSocket.send(auth_message)
recv_auth = clientSocket.recv(1024)

print(f"Auth message: {recv_auth}")
if recv_auth != '235':
	print('AUTH: 235 reply not received from server')

# Send MAIL FROM command and print server response

# Start
mail_from = "MAIL FROM: <fakeemail@fake.com> \r\n"
clientSocket.send(mail_from.encode())
recv_from = clientSocket.recv(1024).decode()
print(f"MAIL FROM message: {recv_from}")
if recv_from[:3] != '250':
	print('MAIL FROM: 250 reply not received from server')

# End

# Send RCPT TO command and print server response

# Start
rcpt_to = "RCPT TO: <destinationemail@fake.com> \r\n"
clientSocket.send(rcpt_to.encode())
recv_rcpt = clientSocket.recv(1024).decode()
print(f"RCPT TO message: {recv_rcpt}")
if recv_rcpt[:3] != '250':
	print('RCPT TO: 250 reply not received from server')

# End

# Send DATA command and print server response

# Start
data = "DATA\r\n"
clientSocket.send(data.encode())
recv_data = clientSocket.recv(1024).decode()
print(f"DATA message: {recv_data}")
if recv_data[:3] != '354':
	print('DATA: 354 reply not received from server')

# End

# Send message data
# Message ends with a single period
# Start
subject = "Subject: CMPE 148 SMTP Lab \r\n\r\n"
clientSocket.send(subject.encode())
message = "\r\n Hi Professor Bond, Please give us all A's! Thank you!"
print(f"Message to send: {message}")
clientSocket.send(message.encode())
clientSocket.send("\r\n.\r\n".encode())
recv_message_data = clientSocket.recv(1024).decode()
print(f"Message Data: {recv_message_data}")
if recv_message_data[:3] != '250':
	print('MESSAGE + PERIOD: 250 reply not received from server')

# End

# Sent QUIT command and get server response

# Start
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv_quit = clientSocket.recv(1024).decode()
print(f"QUIT message: {recv_quit}")
clientSocket.close()

# End





