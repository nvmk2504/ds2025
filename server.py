import socket
import os

def send_file_to_client(conn, filename):
    if os.path.exists(filename):
        try:
            with open(filename, 'rb') as file:
                print(f"Sending file: {filename}")
                while chunk := file.read(1024):
                    conn.send(chunk)
            print(f"File {filename} sent successfully!")
        except Exception as error:
            print(f"Error sending file: {error}")
            conn.send(b"Error sending file!")
    else:
        print(f"File {filename} not found!")
        conn.send(b"File not found!")

def server_program():
    host = '127.0.1.125'
    port = 2002

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port)) 
    server_socket.listen(1)         
    print(f"Server listening on {host}:{port}...")

    try:

        conn, address = server_socket.accept()
        print(f"Connection from {address} has been established.")

        filename = r'E:\distrbuted system\task1\host\transfer_file.txt'

        send_file_to_client(conn, filename)

    except Exception as error:
        print(f"An error occurred: {error}")
    finally:
        conn.close()
        server_socket.close()
        print("Connection closed. Server shut down.")

if __name__ == '__main__':
    server_program()