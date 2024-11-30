import socket

def client_program():
    host = '127.0.1.125'
    port = 2002
    filename = 'received_transfer_file.txt'

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print(f"Connected to server {host}:{port}, receiving file...")

            with open(filename, 'wb') as file:
                while (data := client_socket.recv(1024)):
                    file.write(data)

            print(f"File received successfully! Saved as {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    client_program()