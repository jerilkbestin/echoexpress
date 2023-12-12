import random

# Generate a large prime number
p = 621113

# Choose a primitive root modulo p
g = 1000

def gen_key():
    # Choose a random private key
    priv_k = random.randint(1, p - 1)

    # Compute the public key
    pub_k = pow(g, priv_k, p)

    return priv_k, pub_k

def get_shared_secret(priv_k, pub_k):
    # Compute the shared secret
    sh_sec = pow(pub_k, priv_k, p)

    return sh_sec

# def DH_gen_key():


#     # Alice generates her key pair
#     own_private_key, own_public_key = generate_key()
#     return own_private_key,own_public_key

# def DH_shared_secret(oppo_publickey,own_private_key):
#     # Alice and Bob exchange public keys
#     shared_secret = compute_shared_secret(own_private_key, oppo_publickey, p)
#     #bob_shared_secret = compute_shared_secret(bob_private_key, alice_public_key, p)

#     # The shared secrets should be the same
#     # print("Alice's shared secret:", shared_secret)
#     return shared_secret