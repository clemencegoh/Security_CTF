import string
from typing import List

def caesar(plaintext: bytes, key: int, mode: str="e") -> bytes:
    key = key%256
    ciphertext: bytes = b''
    for i in plaintext:
        i = ord(i)
        ciphertext += bytes([i + key if mode.lower() == "e" else i - key])
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

def vignere(plaintext: bytes, key: bytes) -> bytes:
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
        ciphertext_list.append(caesar(plaintext_list[i], char, "e"))

    # finally, stitch it all back
    for j in range(len(ciphertext_list[0])):
        for i in range(len(ciphertext_list)):
            if(ciphertext_list[i] == b""):
                continue
            ciphertext += bytes([ciphertext_list[i][0]])
            ciphertext_list[i] = ciphertext_list[i][1:]
    return ciphertext


print(vignere("abcdefg ", b"\x02\x02\x02\x02\x02"))

