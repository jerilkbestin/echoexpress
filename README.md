# EchoExpress
One-way Chatbox between client and server protected by a simple TLS model.


Welcome to the demonstration of **EchoExpress**, a one-way chatbox utilizing TLS for secure communication. In this setup, we employ socket programming for communication, Diffie-Hellman for key exchange, and a combination of weak cipher algorithms for encryption and authentication.

It's important to note that this setup is not secure due to the deployment of weak cipher algorithms. This project is for educational purposes only. For a truly secure communication system, it is recommended to use more robust cryptographic methods.

**Programming language:**
python3 (required)

**Libraries required:**
socket
shutil
binascii
random
struct


**Guidelines for setting up:**
1. Download all the python files.
2. Please use python3 to run the files.
3. Please install the above-mentioned libraries if not present (first proceed to step 4 and check if the installation is required). Use the command "pip3 install <library>". 
4. Open two terminals.
5. Run "python3 server.py" on one.
6. Run "python3 client.py" on the other.
7. Please run them in the sequence mentioned.
9. You can see the shared secret is already shown.
10. Please type the message on the client end.
11. You will see the message received on the server end.
12. To exit, press Enter without typing any message on the client end.

Here is the YouTube link to an illustration of the project as well as a small introduction to TLS: https://www.youtube.com/watch?v=v-UUr_g9KSs

Description of each file:

client.py
It initiates the socket connection to server

server.py
It listens for communication on the localhost on port 12345.

pggen.py
Used for generating the large prime number and its primitive modulo for DH.py

MD5.py
Following constants are used as the initial hash values: 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476 (four 32 bit values)
The message is padded to form 512 bits.
The message is divided into 16 32-bit blocks. Each of the 32 bits is further divided into four parts on which bitwise XOR, AND, OR, and bit rotations are performed along with the initial hash values.
It is then updated through the 64 rounds.
It produces a hash value after concatenating the four values.

five_round_feistel_with_RC4.py
For the RC4, part we have a function for the s-box and encryption function. The key is provided from the pre-shared secret.
The key and parts of the message are given to RC4 for encryption through the five-round Feistel network.

DH.py
For DH, I have used the large prime number 621113 and its primitive root modulo 1000. This was calculated based on a code I have submitted “pggen.py”.
![image](https://github.com/jerilkbestin/echoexpress/assets/38150358/39ff9772-d63b-4266-b2e4-3bbb393dcc78)
