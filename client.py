import socket  # Import the socket module for networking
import DH  # Import the Diffie-Hellman module for key exchange
import five_round_feistel_with_RC4  # Import the RC4 encryption module
import md5  # Import the MD5 hashing module
import shutil

bold_code = '\033[1m'
reset_code = '\033[0m'

# Get the terminal width for beautifying the output
def get_terminal_width():
    try:
        col, _ = shutil.get_terminal_size()
        return col
    except Exception as error:
        print(f"Error: {error}")
        return 80  # Default width

# Design the welcome message
def cntr_txt(msg):
    trmnl_width = get_terminal_width()
    pad_width = max(0, (trmnl_width - len(msg)) // 2)
    pad = '-' * pad_width
    return pad + msg + pad

def client():
    # Server details
    host = 'localhost'
    port = 12345

    # Create a socket object
    client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_soc.connect((host, port))
    welcome=cntr_txt("Welcome to TLS Communication channel")
    print(f"\n\n{bold_code}{welcome}{reset_code}\n\n+++++++++SERVER SIDE+++++++++\n\n")
    print("Connected to server: {}:{}\n\n".format(host, port))

    # Perform the Diffie-Hellman key exchange
    client_priv_k, client_pub_k = DH.gen_key()
    server_pub_k = int(client_soc.recv(1024).decode())
    client_soc.send(str(client_pub_k).encode())
    sh_sec = DH.get_shared_secret(client_priv_k, server_pub_k)
    sh_sec_x = hex(sh_sec)[2:]

    ter_width=get_terminal_width()
    print("="*ter_width)

    # Print Shared secret
    print(f"\n\nShared Key: {bold_code}{sh_sec_x}{reset_code}\n\n")
    

    # Message Loop
    i=1
    while True:
        # Send a plaintext message to the server
        print("="*ter_width)
        msg = input(f"\n\nEnter message {bold_code}{i}{reset_code}: ")
        if not msg:
            break
        # Convert plaintext message to hexadecimal
        msg_x = msg.encode().hex()
        

        # Encrypt the message using RC4
        encr_msg = five_round_feistel_with_RC4.five_round_feistel_with_RC4(msg_x, sh_sec_x, True)

        # Hash the encrypted message using MD5
        encr_msg_hash = md5.md5(encr_msg.encode())
        
        # Choose a delimiter that is not a valid hexadecimal character
        delimiter = "#"  

        # Combine hashed and encrypted messages with a delimiter
        final_msg = encr_msg_hash + delimiter + encr_msg

        # Send the combined message to the server
        client_soc.send(final_msg.encode())
        print(f"\n\nSent encrypted with authentication hash message: {bold_code}{final_msg}{reset_code}\n\n")
        i+=1

    # Close the connection
    client_soc.close()

if __name__ == '__main__':
    client()
