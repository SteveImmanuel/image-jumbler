import random
import os
import numpy as np
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Jumble all pixels in an image based on a key')
required_args = parser.add_argument_group('required arguments')
required_args.add_argument('-k', help='Encryption key', required=True)
required_args.add_argument('-i', help='Input path', required=True)
parser.add_argument('-d', help='If presents, will decrypt instead of encrypt', action='store_true')
parser.add_argument('-o', help='Output path (if ommited, result will be saved in curdir', required=False)

args = parser.parse_args()

key = args.k
random.seed(key)

relative_path = args.i
basename, ext = os.path.splitext(relative_path)
in_abs_path = os.path.join(os.path.abspath('.'), relative_path)
out_abs_path = args.o

if not args.d:
    print('encrypting...')
    original_img = Image.open(in_abs_path)

    for i in range(original_img.size[0]):
        for j in range(original_img.size[1]):
            x = random.randrange(0, original_img.size[0])
            y = random.randrange(0, original_img.size[1])
            
            pix1 = original_img.getpixel((i, j))
            pix2 = original_img.getpixel((x, y))
            original_img.putpixel((i, j), pix2)
            original_img.putpixel((x, y), pix1)
    
    if not out_abs_path:
        out_abs_path = os.path.join(os.path.abspath('.'), f'{basename}_enc{ext}')
    original_img.save(out_abs_path)

else:
    enc_img = Image.open(in_abs_path)
    generated_random_num = []

    print('recovering random number...')
    for i in range(enc_img.size[0]):
        for j in range(enc_img.size[1]):
            x = random.randrange(0, enc_img.size[0])
            y = random.randrange(0, enc_img.size[1])
            generated_random_num.append((x,y))

    print('decrypting...')
    for i in range(enc_img.size[0] - 1, -1, -1):
        for j in range(enc_img.size[1] - 1, -1, -1):
            x, y = generated_random_num.pop()
            pix1 = enc_img.getpixel((i, j))
            pix2 = enc_img.getpixel((x, y))
            enc_img.putpixel((i, j), pix2)
            enc_img.putpixel((x, y), pix1)

    if not out_abs_path:
        out_abs_path = os.path.join(os.path.abspath('.'), f'{basename}_dec{ext}')
    enc_img.save(out_abs_path)
    
print('finished')
