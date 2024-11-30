import socket

def cl():
    host = '127.0.1.125'
    port = 2002
    fn = 'received_transfer_file.txt'

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cs:
            cs.connect((host, port))
            print(f"Connected to server {host}:{port}, receiving file...")

            with open(fn, 'wb') as fw:
                while (data := cs.recv(1024)):
                    fw.write(data)

            print(f"File received successfully! Saved as {fn}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    cl()