import random
import sys
import os
import numpy as np
from PIL import Image

key = 'asdwqe'
random.seed(key)

filename = 'email_2.png'
name, ext = os.path.splitext(filename)
print('encrypting')
original_img = Image.open(filename)
# original_img.save('test.jpeg')

# a = np.array(original_img)
# # print(a)

# # test = Image.open('test.jpg')
# # b = np.array(test)
# # print(a-b)

# test2 = Image.fromarray(a)
# c = np.array(test2)
# print(a-c)
# test2.save('test2.jpeg')

# test2 = Image.open('test2.jpeg')
# c = np.array(test2)
# print(a-c)

for i in range(original_img.size[0]):
    for j in range(original_img.size[1]):
        x = random.randrange(0, original_img.size[0])
        y = random.randrange(0, original_img.size[1])
        
        pix1 = original_img.getpixel((i, j))
        pix2 = original_img.getpixel((x, y))
        original_img.putpixel((i, j), pix2)
        original_img.putpixel((x, y), pix1)

original_img.save(f'{name}_enc.{ext}')


enc_img = Image.open(f'{name}_enc.{ext}')
generated_random_num = []

print('recovering random number')
random.seed(key)

for i in range(enc_img.size[0]):
    for j in range(enc_img.size[1]):
        x = random.randrange(0, enc_img.size[0])
        y = random.randrange(0, enc_img.size[1])
        generated_random_num.append((x,y))

print('decrypting')

for i in range(enc_img.size[0] - 1, -1, -1):
    for j in range(enc_img.size[1] - 1, -1, -1):
        x, y = generated_random_num.pop()
        pix1 = enc_img.getpixel((i, j))
        pix2 = enc_img.getpixel((x, y))
        enc_img.putpixel((i, j), pix2)
        enc_img.putpixel((x, y), pix1)

enc_img.save(f'{name}_dec.{ext}')

# original_img = Image.open('doge.jpg')
# dec_img = Image.open('test.jpg')

# for i in range(original_img.size[0]):
#     for j in range(original_img.size[1]):
#         pixel_original = original_img.getpixel((i, j))
#         pixel_dec = dec_img.getpixel((i, j))
#         print('dif', pixel_original[0] - pixel_dec[0], pixel_original[1] - pixel_dec[1], pixel_original[2] - pixel_dec[2])
#     break