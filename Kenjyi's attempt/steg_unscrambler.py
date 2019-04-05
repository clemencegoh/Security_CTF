import numpy as np
from PIL import Image
import imageio


image = imageio.imread("illusion.png")
# image = img.imread("illusion.png")

print(image)

red = []
green = []
blue = []

# Extract last bits of each color from image
# for i in range(len(image)):
#     for j in range(len(image[0])):
#         red.append(int(str(bin(image[i][j][0])[-1:])) * 255)
#         green.append(int(str(bin(image[i][j][1])[-1:])) * 255)
#         blue.append(int(str(bin(image[i][j][2])[-1:])) * 255)
#
# Extract the coord images from the bits
# r_mat = np.reshape(red, (512, 512)).astype(np.uint8)
# r_im = Image.fromarray(r_mat, 'L')
# r_im.show()
# g_mat = np.reshape(green, (512, 512)).astype(np.uint8)
# g_im = Image.fromarray(g_mat, 'L')
# g_im.show()
# b_mat = np.reshape(blue, (512, 512)).astype(np.uint8)
# b_im = Image.fromarray(b_mat, 'L')
# b_im.show()

# Flag coords in each color
r_coord = [(432, 293), (69,27), (19,48), (269,286), (246,317), (182,47), (332, 5), (443, 70), (404,180), (481, 496), (399,65), (40, 282)]
g_coord = [(443, 401), (97,492), (101, 89), (353, 208), (333, 32), (323, 434), (352,23), (472,171), (201, 265), (503, 321), (18,227), (59,325)]
b_coord = [(346, 283), (167, 222), (396, 144), (465, 393), (475, 282), (259, 405), (13, 422), (319, 144), (336, 232), (15, 473), (326,164), (113, 423), (389,302)]

# Extract integer values at each coord
r_int_ls = []
g_int_ls = []
b_int_ls = []

for (x, y) in r_coord:
    for i in range(len(image)):
        for j in range(len(image[0])):
            if x == j and y == i:
                r_int_ls.append(image[i][j][0])

for (x, y) in g_coord:
    for i in range(len(image)):
        for j in range(len(image[0])):
            if x == j and y == i:
                g_int_ls.append(image[i][j][1])

for (x, y) in b_coord:
    for i in range(len(image)):
        for j in range(len(image[0])):
            if x == j and y == i:
                b_int_ls.append(image[i][j][2])

r_flag = ""
g_flag = ""
b_flag = ""

# Convert integer values to string flag via ASCII
for i in r_int_ls:
    r_flag += chr(i)

for i in g_int_ls:
    g_flag += chr(i)

for i in b_int_ls:
    b_flag += chr(i)

flag = g_flag + r_flag + b_flag

print(r_int_ls)
print(r_flag)
print(g_int_ls)
print(g_flag)
print(b_int_ls)
print(b_flag)

print(flag)