import numpy as np

def initialize_lfsr(seed, size=8):
    """Initializes the LFSR with the given binary seed."""
    state = np.array([int(bit) for bit in seed], dtype=int)
    return np.roll(state, -size)

def step_lfsr(state, polynomial):
    """Performs one step of the LFSR."""
    new_bit = np.bitwise_xor.reduce(state[polynomial])
    state = np.roll(state, -1)
    state[0] = new_bit
    return state

def generate_keystream(initial_state, polynomial, length):
    """Generates a binary keystream."""
    state = initialize_lfsr(initial_state)
    keystream = []
    for _ in range(length):
        state = step_lfsr(state, polynomial)
        keystream.append(state[0])
    return keystream

def encrypt_decrypt(message, keystream):
    """Encrypts or decrypts a binary message."""
    message_bits = np.array([int(bit) for bit in message], dtype=int)
    encrypted_decrypted = np.bitwise_xor(message_bits, keystream)
    result = ''.join(str(bit) for bit in encrypted_decrypted)
    return result

def main():
    plaintext = "ATNYCUWEARESTRIVINGTOBEAGREATUNIVERSITYTHATTRANSCENDSDISCIPLINARYDIVIDESTOSOLVETHEINCREASINGLYCOMPLEXPROBLEMSTHATTHEWORLDFACESWEWILLCONTINUETOBEGUIDEDBYTHEIDEATHATWECANACHIEVESOMETHINGMUCHGREATERTOGETHERTHANWECANINDIVIDUALLYAFTERALLTHATWASTHEIDEATHATLEDTOTHECREATIONOFOURUNIVERSITYINTHEFIRSTPLACE"    
    initial_key = "00000001"
    binary_message = ''.join(format(ord(char), '08b') for char in plaintext)
    characteristic_polynomial = [7, 3, 2, 1]
    keystream = generate_keystream(initial_key, characteristic_polynomial, len(binary_message))
    encrypted_message = encrypt_decrypt(binary_message, keystream)
    decrypted_message = encrypt_decrypt(encrypted_message, keystream)
    decrypted_text = ''.join(chr(int(decrypted_message[i:i+8], 2)) for i in range(0, len(decrypted_message), 8))
    print("Encrypted Message (Binary):\n", encrypted_message)
    print("Decrypted Text:\n", decrypted_text)

main()