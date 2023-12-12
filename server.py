import socket
import DH
import five_round_feistel_with_RC4
import md5
import shutil

bold_code = '\033[1m'
reset_code = '\033[0m'

# Get the terminal width for beautifying the output
def get_terminal_width():
    try:
        col, _ = shutil.get_terminal_size()
        return col
    except Exception as error:
        print(f"Error getting terminal size: {error}")
        return 80  # Default width

# Design the welcome message
def cntr_txt(msg):
    trmnl_width = get_terminal_width()
    pad_width = max(0, (trmnl_width - len(msg)) // 2)
    pad = '-' * pad_width
    return pad + msg + pad

def server():
    host = 'localhost'
    port = 12345

    # Create a socket object
    server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_soc.bind((host, port))

    # Listen for incoming connections
    server_soc.listen(1)
    welcome=cntr_txt("Welcome to TLS Communication channel")
    print(f"\n\n{bold_code}{welcome}{reset_code}\n\n+++++++++SERVER SIDE+++++++++\n\n")
    print("Server listening on {}:{}".format(host, port))

    # Accept a client connection
    client_soc, addr = server_soc.accept()
    print("\n\nConnected to client: {}\n\n".format(addr))

    # Perform the Diffie-Hellman key exchange
    server_priv_k, server_pub_k = DH.gen_key()
    client_soc.send(str(server_pub_k).encode())
    client_pub_k = int(client_soc.recv(1024).decode())
    sh_sec = DH.get_shared_secret(server_priv_k, client_pub_k)
    sh_sec_x = hex(sh_sec)[2:]

    term_width=get_terminal_width()
    print("="*term_width)

    # Print Shared secret
    print(f"\n\nShared Key: {bold_code}{sh_sec_x}{reset_code}\n\n")

    # Message Loop
    i=1
    while True:
        # Receive the combined message from the client
        rec_msg = client_soc.recv(1024).decode()
        if not rec_msg:
            break
        print("="*term_width)
        print(f"\n\nReceived data: {bold_code}{rec_msg}{reset_code}")
        # Split the combined message using the delimiter
        delimiter = "#"  # Choose a delimiter that is not part of the hashed or encrypted message
        encr_msg_hash, encr_msg = rec_msg.split(delimiter)
    

        # Perform MD5 authentication on the decrypted message
        if md5.md5(encr_msg.encode()) == encr_msg_hash:
            print("\n\nMessage authenticated successfully!")
        else:
            print("\n\nMessage authentication failed.")

        # Decrypt the message using RC4 with 5 Feistel rounds
        decr_msg_x = five_round_feistel_with_RC4.five_round_feistel_with_RC4(encr_msg, sh_sec_x, False)
        decr_msg = bytes.fromhex(decr_msg_x).decode()
        print(f"\n\nReceived hashed message: {bold_code}{encr_msg_hash}{reset_code}")
        print(f"Received encrypted message: {bold_code}{encr_msg}{reset_code}")
        print(f"Decrypted message {i}: {bold_code}{decr_msg}{reset_code}\n\n")
        i+=1
    

    # Close the connection
    client_soc.close()

if __name__ == '__main__':
    server()