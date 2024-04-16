import hashlib


def hash_file(file_path, hash_algorithm='SHA256'):
    # Choose the hashing algorithm
    hash_function = hashlib.new(hash_algorithm)

    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Read the file content in chunks
        chunk_size = 4096
        while chunk := file.read(chunk_size):
            # Update the hash object with the chunk
            hash_function.update(chunk)

    # Get the hexadecimal digest of the hash
    file_hash = hash_function.hexdigest()

    return file_hash


def hash_string(input_string):
    # Create a sha256 hash object
    sha_signature = hashlib.sha256(input_string.encode('utf-8')).hexdigest()
    return sha_signature


# open and read the file after the appending:
f = open("te.txt", "r")
print(repr(f.read()))
print(hash_string(f.read()) == '5ec3b43337028cb522b22b5b6e7933f07302f9c8bafc67b4a866668978d3a8ff')
print(hash_string(
    f'0:\n1 2\n1:\n1 1\n2:\n2 3\n3:\n4 5\n4:\n0 0\n5:\n2 5\n4 5\nA:\nB:\n') == '5ec3b43337028cb522b22b5b6e7933f07302f9c8bafc67b4a866668978d3a8ff')