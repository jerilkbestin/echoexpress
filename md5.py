import struct

# Constants for MD5 rounds
constants = [
    0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476
]

# Functions for MD5 rounds
functions = [
    lambda b, c, d: (b & c) | (~b & d),
    lambda b, c, d: (d & b) | (~d & c),
    lambda b, c, d: b ^ c ^ d,
    lambda b, c, d: c ^ (b | ~d)
]

# Rotation amounts for each round
rotations = [
    [7, 12, 17, 22] * 4,
    [5, 9, 14, 20] * 4,
    [4, 11, 16, 23] * 4,
    [6, 10, 15, 21] * 4
]

# Padding function
def md5_pad(msg):
    # Append padding bits and length to the message
    orig_len = len(msg) * 8

    # Pre-processing: add a single 1 bit
    msg += b"\x80"

    # Padding with zeros
    while len(msg) % 64 != 56:
        msg += b"\x00"

    # Append the original message length in bits as a 64-bit little-endian integer
    msg += struct.pack("<Q", orig_len)

    return msg

# Left rotate function
def md5_left_rotate(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

# MD5 hash function
def md5_hash(msg):
    # Initialize hash values (A, B, C, D)
    h0 = constants[0]
    h1 = constants[1]
    h2 = constants[2]
    h3 = constants[3]

    # Step 1: Padding
    pad_msg = md5_pad(msg)

    # Step 2: Process the message in 512-bit (64-byte) blocks
    for i in range(0, len(pad_msg), 64):
        block = pad_msg[i:i + 64]

        # Break the block into 16 words (each word is 32 bits)
        words = struct.unpack("<16I", block)

        # Initialize hash values for this block
        a = h0
        b = h1
        c = h2
        d = h3

        # Main MD5 rounds
        for j in range(64):
            f = functions[j // 16](b, c, d)
            g = j % 16

            temp = d
            d = c
            c = b
            b = (b + md5_left_rotate((a + f + constants[j // 16] + words[g]) & 0xFFFFFFFF, rotations[j // 16][j % 4])) & 0xFFFFFFFF
            a = temp

        # Update hash values for this block
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF

    # Step 3: Produce the final hash value
    hash = struct.pack("<4I", h0, h1, h2, h3)

    return hash.hex()

# Main function
def md5(msg):

    # Calculate MD5 hash
    hash_value = md5_hash(msg)
    
    return hash_value