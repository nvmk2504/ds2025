import xmlrpc.client

def upload(name):

    try:
        with open(name, 'rb') as file:
            binary_data = file.read()
        response = rpc_server.save_file(name, xmlrpc.client.Binary(binary_data))
        print(response)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':

    rpc_server = xmlrpc.client.ServerProxy('http://127.0.0.1:25041')

    file_to_send = 'transfer_file.txt'
    upload(file_to_send)