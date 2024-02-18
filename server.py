import socket
from openai import OpenAI
def start_receiver():
    try:
        HOST = ''
        print(HOST)
        PORT = 9999
        receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        receiver_socket.bind((HOST, PORT))
        receiver_socket.listen(1)
        print("Waiting for a connection from the sender...")

        while True:
            sender_socket, sender_address = receiver_socket.accept()
            print(f"concted to {sender_address}")
            received_message = sender_socket.recv(1024)
            # if i send this from the clint it will close the server.py program
            if '{% exit %}' in received_message.decode('utf-8'):
                sender_socket.close()
                receiver_socket.close()
                exit()
            print(f"Received message: {received_message.decode('utf-8')}")
            modified_message = gpt(received_message.decode('utf-8'))
            print(f"message sent: {modified_message}")
            sender_socket.sendall(modified_message.encode())
            print(f"message sent: {modified_message}")
            sender_socket.close()

    except Exception as e:
        print(e)
        sender_socket.close()
        receiver_socket.close()
        exit()
def gpt(prompt):
    defult_api_key = ""
    client = OpenAI(api_key= defult_api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-3.5-turbo",
    )
    answer = chat_completion.choices[0].message.content
    return answer

def main():
    start_receiver()



if __name__ == "__main__":
    main()
