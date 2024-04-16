import hashlib


def hash_string(input_string):
    # Create a sha256 hash object
    sha_signature = hashlib.sha256(input_string.encode('utf-8')).hexdigest()
    return sha_signature


# open and read the file after the appending:
f = open("ans.txt", "r")
print(repr(f.read()))
print(hash_string(f.read()))
print(hash_string(
    '0:\n1 0\n1:\n2 3\n2:\n4 2\n3:\n4 5\n4:\n2 1\n5:\n0 3\n1 4\nA:10\nB:'))
print(hash_string(
    '0:\n1 0\n1:\n2 3\n2:\n4 2\n3:\n4 5\n4:\n2 1\n5:\n0 3\n1 4\nA:10\nB:\n'))
print(hash_string(
    '0:\n1 0\n1:\n2 3\n2:\n4 2\n3:\n4 5\n4:\n2 1\n5:\n0 3\n1 4\nA:10\nB:') == '6797e56802e0ff2f5fff1165063f6b8daa5f02b93ed6b905f35e530f82c5661b')
print(hash_string(f.read()) == '6797e56802e0ff2f5fff1165063f6b8daa5f02b93ed6b905f35e530f82c5661b')
print(hash_string(
    '0:\n1 0\n1:\n2 3\n2:\n4 2\n3:\n4 5\n4:\n2 1\n5:\n0 3\n1 4\nA:10\nB:\n') == '6797e56802e0ff2f5fff1165063f6b8daa5f02b93ed6b905f35e530f82c5661b')
