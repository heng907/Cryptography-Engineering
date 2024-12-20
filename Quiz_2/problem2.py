import hashlib
import time

video_path = 'video.mp4'

# Hash functions to test
hash_functions = {
    'MD5': hashlib.md5(),
    'SHA1': hashlib.sha1(),
    'SHA-224': hashlib.sha224(),
    'SHA-256': hashlib.sha256(),
    'SHA-512': hashlib.sha512(),
    'SHA3-224': hashlib.sha3_224(),
    'SHA3-256': hashlib.sha3_256(),
    'SHA3-512': hashlib.sha3_512()
}

# Function to calculate and time hash
def calculate_hash(hash_func, file_path):
    start_time = time.time()  # Start timer
    with open(file_path, 'rb') as file:  # Open file in binary mode
        while chunk := file.read(8192):  # Read file in chunks of 8 KB
            hash_func.update(chunk)  # Update hash with each chunk
    end_time = time.time()  # End timer
    return end_time - start_time, hash_func.hexdigest()  # Return time taken and hash value

# Calculate hash and time for each hash function
execution_times = {}
for name, func in hash_functions.items():
    execution_times[name], _ = calculate_hash(func, video_path)

# Print out the execution times
print("(a)\nExecution times for each hash function:")
for name, time_taken in execution_times.items():
    print(f"{name}: {time_taken} seconds")

# Find and print the fastest hash function
fastest_hash = min(execution_times, key=execution_times.get)
print("\n(b)")
print(f"The fastest hash function is: {fastest_hash}")

# Print the ranking of hash functions by speed
print("\n(c)\nRanking of hash functions by speed:")
sorted_times = sorted(execution_times.items(), key=lambda x: x[1])
for rank, (name, time) in enumerate(sorted_times, start=1):
    print(f"{rank}. {name}: {time} seconds")
