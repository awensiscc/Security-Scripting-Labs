import hashlib


def hash_file(filepath, hash_algo='sha256'):
    # Create a new hash object based on the specified algorithm
    hash_obj = hashlib.new(hash_algo)
    
    # Open the file in binary read mode and read the entire content at once
    with open(filepath, 'rb') as f:
        file_data = f.read()
    
    # Update the hash with the file data
    hash_obj.update(file_data)
    
    # Return the hexadecimal digest of the hash
    return hash_obj.hexdigest()

print("\n")
print(hash_file("output.txt"))


print("\n")
