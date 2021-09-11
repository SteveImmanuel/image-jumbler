import os
import argparse
import numpy as np
from PIL import Image
from algorithm import BruteAlgo, WeaveAlgo


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Jumble all pixels in an image based on a key')
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-k', help='Encryption key', required=True)
    required_args.add_argument('-i', help='Input path', required=True)
    parser.add_argument('-d', help='If presents, will decrypt instead of encrypt', action='store_true')
    parser.add_argument('-f', help='Use fast algorithm, but the result is not as good. Defaults to slow algorithm', action='store_true')
    parser.add_argument('-o', help='Output path (if ommited, result will be saved in curdir', required=False)

    args = parser.parse_args()

    key = args.k

    relative_path = args.i
    basename, ext = os.path.splitext(relative_path)
    in_abs_path = os.path.join(os.path.abspath('.'), relative_path)
    out_abs_path = args.o

    input_img = Image.open(in_abs_path)
    img_arr = np.array(input_img)

    if args.f:
        algo = WeaveAlgo(key, img_arr)
    else:
        algo = BruteAlgo(key, img_arr)

    if not args.d:
        if not out_abs_path:
            out_abs_path = os.path.join(os.path.abspath('.'), f'{basename}_enc{ext}')
        algo.encrypt()

    else:
        if not out_abs_path:
            out_abs_path = os.path.join(os.path.abspath('.'), f'{basename}_dec{ext}')
        algo.decrypt()

    result_img = Image.fromarray(algo.img_arr)
    result_img.save(out_abs_path)
        
    print('finished')
