from xmlrpc.server import SimpleXMLRPCServer

def save(name, data):

    try:
        with open(name, 'wb') as file:
            file.write(data.data)
        return f"File '{name}' received and saved."
    except Exception as e:
        return f"Failed to save file: {e}"

if __name__ == '__main__':

    server = SimpleXMLRPCServer(('127.0.0.1', 25041), allow_none=True)
    server.register_function(save, "save_file")
    print("Server running at 127.0.0.1:25041")
    server.serve_forever()