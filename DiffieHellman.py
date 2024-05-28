import secrets

# Function to perform modular exponentiation
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Diffie-Hellman key exchange algorithm
def diffie_hellman(p, g):
    # Generate private keys (random integers)
    a = secrets.randbelow(p)
    b = secrets.randbelow(p)
    
    # Compute public keys
    A = mod_exp(g, a, p)
    B = mod_exp(g, b, p)
    
    # Exchange public keys and compute shared secret
    shared_secret_A = mod_exp(B, a, p)
    shared_secret_B = mod_exp(A, b, p)
    
    assert shared_secret_A == shared_secret_B, "Shared secrets do not match!"
    
    return shared_secret_A

# Example usage
if __name__ == "__main__":
    # Example of a large prime number and a base
    p = 23  # A large prime number
    g = 5   # A primitive root modulo p
    
    shared_secret = diffie_hellman(p, g)
    print(f"Shared secret: {shared_secret}")
