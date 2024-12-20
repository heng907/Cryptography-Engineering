# import secrets

# def generate_secure_random_number(num_bytes: int):
#     return secrets.token_bytes(num_bytes)

# # Generate 1MB of cryptographically secure random bytes
# random_bytes = generate_secure_random_number(8388608)
# # write in a file
# with open('random.bin', 'wb') as file:
#     file.write(random_bytes)

import secrets
# the function to generate the secure random number 
def generate_randomNum(num_bits: int): 
    random_bits = secrets.token_bits(num_bits)
    # return ''.join(f'{byte:08b}'for byte in random_bytes)
    return random_bits
# generate 1M bytes random number 
random_bits = generate_randomNum(8388608) # 8388608 = 1024 * 1024 * 8 (bits)
# output a file 'random.bin'
with open('random.bin', 'wb') as file:
    file.write(random_bits)