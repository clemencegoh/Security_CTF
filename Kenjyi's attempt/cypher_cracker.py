
f = open("copypasta_encrypted.txt", "rb")

contents = f.read()
# print(contents)

set_0 = []
set_1 = []
set_2 = []
set_3 = []
set_4 = []

#create lists of each character with the same shift
for i in range(len(contents)):
    if i % 5 == 0:
        set_0.append(contents[i])
    if i % 5 == 1:
        set_1.append(i)
    if i % 5 == 2:
        set_2.append(i)
    if i % 5 == 3:
        set_3.append(i)
    if i % 5 == 4:
        set_4.append(i)
# fl = f.readlines()

# print(set_0)

# print(max(set_0, key=set_0.count))

#ascii for space = 32, calculate shifts
shift_0 = max(set_0, key=set_0.count) - 32
shift_1 = max(set_1, key=set_0.count) - 32
shift_2 = max(set_2, key=set_0.count) - 32
shift_3 = max(set_3, key=set_0.count) - 32
shift_4 = max(set_4, key=set_0.count) - ord("s")

# shift_0 = ord("M")
# shift_1 = ord("O")
# shift_2 = ord("R")
# shift_3 = ord("T")
# shift_4 = ord("Y")

#decrypt set_0
for i in set_0:
    index = set_0.index(i)
    set_0[index] = (i - shift_0) % 256
    set_0[index] = chr(set_0[index])

for i in set_1:
    index = set_1.index(i)
    set_1[index] = (i - shift_1) % 256
    set_1[index] = chr(set_1[index])

for i in set_2:
    index = set_2.index(i)
    set_2[index] = (i - shift_2) % 256
    set_2[index] = chr(set_2[index])

for i in set_3:
    index = set_3.index(i)
    set_3[index] = (i - shift_3) % 256
    set_3[index] = chr(set_3[index])

for i in set_4:
    index = set_4.index(i)
    set_4[index] = (i - shift_4) % 256
    set_4[index] = chr(set_4[index])


# Extract plain text
plain = ""

for i in range(len(set_0)):
    try:
        plain += set_0[i] + set_1[i] + set_2[i] + set_3[i] + set_4[i]
    except:
        pass

key = chr(shift_0 % 256) + chr(shift_1 % 256) + chr(shift_2 % 256) + chr(shift_3 % 256) + chr(shift_4 % 256)

print(plain)

# print(key)
# print(set_0)
f.close()