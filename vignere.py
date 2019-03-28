import string
from typing import List

def caesar(plaintext: bytes, key: int, mode: str="e") -> bytes:
    key = key%256
    ciphertext: bytes = b''
    for i in plaintext:
        ciphertext += bytes([(i + key)%256 if mode.lower() == "e" else (i - key)%256])
    return ciphertext

def shiftCipher(inp:str, k:int, mode:str="e") -> str:
    output = ""
    for i in inp:
        curr = string.printable.find(i)
        if(mode.lower() == "e"):
            curr += k
        elif(mode.lower() == "d"): 
            curr -= k
        else: 
            raise ValueError("")
        curr = curr%len(string.printable)
        output += string.printable[curr]
    return output

# print(caesar(b"1ab2", 50))

def vignere(plaintext: bytes, key: bytes, mode: str = "e") -> bytes:
    if (type(key) == str):
        key = key.encode()
    plaintext_list: List[List[bytes]] = []
    ciphertext_list: List[List[bytes]] = []
    ciphertext: bytes = b''
    
    for i in range(len(key)):
        # splits the input into multiple different lists
        plaintext_list.append(plaintext[i::len(key)])
    
    # then we encrypt each sublist with caesar cipher
    for i, char in enumerate(key):
        ciphertext_list.append(caesar(plaintext_list[i], char, mode))

    # finally, stitch it all back
    for j in range(len(ciphertext_list[0])):
        for i in range(len(ciphertext_list)):
            if(ciphertext_list[i] == b""):
                continue
            ciphertext += bytes([ciphertext_list[i][0]])
            ciphertext_list[i] = ciphertext_list[i][1:]
    return ciphertext

x = vignere(b"\x01abcdefg ", b"\x06\xfe\x04\x03\x02")

print(x)
print(vignere(x, b"\x06\xfe\x04\x03\x02", "d"))


# with open("week3/writeup.pdf", "rb") as f:
#     x = f.readlines()
#     x = b''.join(x)
#     print(x)
#     l = vignere(x, b"\x06\x05\x04\x03\x02\x04\x03\x02\x04\xff\x02")
#     print(vignere(l, b"\x06\x05\x04\x03\x02\x04\x03\x02\x04\xff\x02", "d"))

# a 0.5mb file takes 10s to encrypt
# q. inefficient