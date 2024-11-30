import socket

HOST = '127.0.1.125'  
PORT = 2002   

se = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
se.bind((HOST, PORT))

se.listen(1)
print(f"Server listening on {HOST}:{PORT}...")

con, addr = se.accept()
print(f"Connected by {addr}")

fn = con.recv(1024).decode('utf-8') 
print(f"Receiving file: {fn}")


with open(fn, 'wb') as f:
    while True:
        
        data = con.recv(1024)
        if not data:
            break  
        f.write(data)

print(f"File {fn} received successfully.")
con.close() 
se.close()