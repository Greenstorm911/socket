import socket

def send_message(message):
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sender_address = ('', 9999)  

    try:
        sender_socket.connect(sender_address)
        sender_socket.sendall(message.encode('utf-8'))
        print(f"Sent message: {message}")

        # Receive the modified string back from the receiver
        modified_message = sender_socket.recv(1024)
        print(f"Modified message received: {modified_message.decode('utf-8')}")

    finally:
        sender_socket.close()

    return modified_message.decode('utf-8')

def main():
    message = input()
    print(send_message(message))
    
if __name__ == '__main__':
    main()