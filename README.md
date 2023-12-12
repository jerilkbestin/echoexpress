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

Here is the youtube link to an illustration of the project as well as a small introduction to TLS: https://www.youtube.com/watch?v=v-UUr_g9KSs
