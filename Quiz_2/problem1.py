import hashlib
import time

# easy hash :ef0ebbb77298e1fbd81f756a4efc35b977c93dae
# Medium hash: 0bc2f4f2e1f8944866c2e952a5b59acabd1cebf2
# Leet hacker hash: 9d6b628c1f81b4795c0266c0f12123c1e09a7ad3
# Hint: The salt term here is: dfc3e4f0b9b5fb047e9be9fb89016f290d2abb06
# Extra Credit: 44ac8049dd677cb5bc0ee2aac622a0f42838b34d

def sha1_hash(string):
    return hashlib.sha1(string.encode('utf-8')).hexdigest()

def bf_sha1(hash_to_break, password_file):
    count = 0
    start_time = time.time()
    with open(password_file, 'r') as file:
        for password in file:
            password = password.strip()  # Remove potential new line characters
            count += 1
            # For salted passwords, concatenate the salt and the password
            #password = 'redbull'+ password # comment out this line of code in easy, medium and salt
            if sha1_hash(password) == hash_to_break:
                end_time = time.time()
                return password, count, end_time - start_time
    end_time = time.time()  # If the password was not found
    return None, count, end_time - start_time

# For leet hacker hash
hash_to_break = 'dfc3e4f0b9b5fb047e9be9fb89016f290d2abb06'  # hash 
password_file = 'password.txt'  # the path of 100000 passwords list
result, tries, time_taken = bf_sha1(hash_to_break, password_file) 


if result:
    print(f"dfc3e4f0b9b5fb047e9be9fb89016f290d2abb06") # change the hash if the question need
    print(f"Password: {result}")
    print(f"Took {tries} attempts to crack input hash. Time taken: {time_taken} seconds")
else:
    print(f"Password not found in the passwords.txt\n Tries: {tries}, Time: {time_taken} seconds")
