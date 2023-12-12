import binascii

class RC4_K:
    def __init__(self, k):
        # Initialize RC4 key object with S-box values and the provided key
        self.S = list(range(256))
        self.k = k

def hex_to_bytes(x_str):
    # Convert a hexadecimal string to bytes
    x_str = x_str.replace(" ", "").replace("0x", "")
    if len(x_str) % 2 != 0:
        x_str = "0" + x_str
    return bytes.fromhex(x_str)

def RC4_k(rc4_k, k, klen):
    # Key-scheduling algorithm for RC4
    j = 0
    for i in range(256):
        j = (j + rc4_k.S[i] + k[i % klen]) % 256
        rc4_k.S[i], rc4_k.S[j] = rc4_k.S[j], rc4_k.S[i]

def RC4(rc4_k, msg):
    # RC4 encryption or decryption algorithm
    i, j = 0, 0
    proc_msg = bytearray()

    for k in range(len(msg)):
        i = (i + 1) % 256
        j = (j + rc4_k.S[i]) % 256
        rc4_k.S[i], rc4_k.S[j] = rc4_k.S[j], rc4_k.S[i]

        n = rc4_k.S[(rc4_k.S[i] + rc4_k.S[j]) % 256]

        proc_msg.append(msg[k] ^ n)

    return proc_msg

def feistel_encrypt(msg, k):
    # Feistel network encryption
    block_len = len(msg) // 2
    L_block = msg[:block_len]
    R_block = msg[block_len:]

    rc4_k = RC4_K(k)
    RC4_k(rc4_k, k, len(k))

    for _ in range(5):
        L_block, R_block = R_block, bytes(a ^ b for a, b in zip(L_block, R_block))

    encr_msg = L_block + R_block
    return encr_msg

def feistel_decrypt(encr_msg, k):
    # Feistel network decryption
    block_len = len(encr_msg) // 2
    L_block = encr_msg[:block_len]
    R_block = encr_msg[block_len:]

    rc4_key = RC4_K(k)
    RC4_k(rc4_key, k, len(k))

    for _ in range(5):
        R_block, L_block = L_block, bytes(a ^ b for a, b in zip(R_block, L_block))

    org_msg = L_block + R_block
    return org_msg

def five_round_feistel_with_RC4(msg_x, sh_sec_x, encrypt=True):
    # RC4 encryption or decryption with 5-round Feistel network
    k = hex_to_bytes(sh_sec_x)
    msg = hex_to_bytes(msg_x)

    if encrypt:
        processed_msg = feistel_encrypt(msg, k)
    else:
        processed_msg = feistel_decrypt(msg, k)

    processed_msg_x = binascii.hexlify(processed_msg).decode()
    # print("Input Message (Hex):", message_hex)
    # print("Processed Message (Hex):", processed_message_hex)
    return processed_msg_x
