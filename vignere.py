from typing import List, Dict

def caesar(plaintext: bytes, key: int, mode: str="e") -> bytes:
    key = key%256
    ciphertext: bytes = b''
    for i in plaintext:
        ciphertext += bytes([(i + key)%256 if mode.lower() == "e" else (i - key)%256])
    return ciphertext

# print(caesar(b"1ab2", 50))

# def shiftCipher(inp:str, k:int, mode:str="e") -> str:
#     output = ""
#     for i in inp:
#         curr = string.printable.find(i)
#         if(mode.lower() == "e"):
#             curr += k
#         elif(mode.lower() == "d"): 
#             curr -= k
#         else: 
#             raise ValueError("")
#         curr = curr%len(string.printable)
#         output += string.printable[curr]
#     return output

def vignere(plaintext: bytes, key: bytes, mode: str = "e") -> bytes:
    if (type(plaintext) == str):
        plaintext = plaintext.encode()
    if (type(key) == str):
        key = key.encode()
    plaintext_list: List[List[bytes]] = []
    ciphertext_list: List[List[bytes]] = []
    ciphertext: bytes = b''
    
    # splits the input into multiple different lists
    for i in range(len(key)):
        plaintext_list.append(plaintext[i::len(key)])
    
    # then we encrypt each sublist with caesar cipher
    for i, char in enumerate(key):
        ciphertext_list.append(caesar(plaintext_list[i], char, mode))

    # finally, stitch it all back
    for _ in range(len(ciphertext_list[0])):
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

# spacebar is 32. we just shift all the most common letters to 32.

# decryptor:
def splitter(text: bytes, keylength: int) -> List[bytes]:
    keylength = keylength%256
    split_text: List[bytes] = []
    for i in range(keylength):
        split_text.append(text[i::keylength])
    return split_text

def freq_analysis(text: bytes) -> Dict[bytes, int]:
    counts: Dict[bytes, int] = {}
    for i in range(256):
        counts[i] = 0
    for i in text:
        counts[i] += 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts

print(freq_analysis(b"abcacdddlkfoweilnaa"))