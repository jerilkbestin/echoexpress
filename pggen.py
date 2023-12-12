from sympy import isprime, randprime

#coded with references online
#In the context of modular arithmetic and number theory, residues refer to the remainders obtained when integers are divided by a specified modulus. 
def check_primitive_root(g, p):
    residues = set(pow(g, i, p) for i in range(1, p))
    return len(residues) == p - 1

def generate_large_prime_and_primitive_root(min_value, max_value, min_root, max_root):
    while True:
        prime = randprime(min_value, max_value)
        if isprime(prime):
            for root in range(min_root, max_root + 1):
                if check_primitive_root(root, prime):
                    return prime, root

# Define the minimum and maximum values for the prime number range
min_value = 10**5
max_value = 10**6

# Define the minimum and maximum values for the primitive root range
min_root = 10**3
max_root = 10**3

# Generate a large prime number and its primitive root
p, g = generate_large_prime_and_primitive_root(min_value, max_value, min_root, max_root)

print("Generated prime number (p):", p)
print("Generated primitive root (g):", g)
