from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    # clientSocket = socket(AF_INET, SOCK_STREAM)
    # clientSocket.bind(("", port))
    # clientSocket.listen(1)
    # connectionSocket, addr = clientSocket.accept()
    # getting error message redelcating port and mailserver
    # port = 1025
    # mailserver ='127.0.0.1'

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # clientSocket.connect((port, mailserver))
    clientSocket.listen(1)
    # clientSocket.accept()
    # clientSocket, recv = clientSocket.accept()

    # Fill in end

    recv = clientSocket.recv(1024).decode()
    # print(recv)
    if recv[:3] != '220':
    # print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
    # print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailfromCommand = 'MAIL FROM: <arzoofhussain@gmail.com>\r\n'
    # to test command
    # print(mailfromCommand)
    clientSocket.send(mailfromCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
    # print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcpttoCommand = 'RCPT to: <ah5997@nyu.edu>\r\n'
    # to test command
    # print(rcpttoCommand)
    clientSocket.send(rcpttoCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
    # print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'data\r\n'
    # to test command
    # print(dataCommand)
    clientSocket.send(dataCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
    # print('250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    messagedata = 'message data\r\n'
    # to test command
    # print(messagedata)
    clientSocket.send(messagedata.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
    # print('250 reply not received from server.')
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    messageend = '\r\n.\r\n'
    # to test command
    # print(messageend)
    clientSocket.send(messagedata.encode() + messageend.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
    # print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'quit\r\n'
    # to test command
    # print(quitCommand)
    clientSocket.send(quitCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':


# print('250 reply not received from server.')
# Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
