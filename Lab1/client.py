import socket

def cl():
    host = '127.0.0.1'
    port = 25041
    fn = 'received_transfer_file.txt'

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cs:
            cs.connect((host, port))
            print(f"Connected to server {host}:{port}")

            with open(fn, 'wb') as fw:
                while (data := cs.recv(1024)):
                    fw.write(data)

            print(f"successfully")
    except Exception as e:
        print(f"Error")

if __name__ == '__main__':
    cl()