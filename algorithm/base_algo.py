import random
from abc import ABC, abstractmethod

class BaseAlgo:
    def __init__(self, key, img_arr):
        self.key = key
        self.generated_random_num = []
        self.img_arr = img_arr

    @abstractmethod
    def recover_random_number(self):
        print('recovering random number...')
        random.seed(self.key)

    @abstractmethod
    def encrypt(self):
        print('encrypting...')
        random.seed(self.key)

    @abstractmethod
    def decrypt(self):
        self.recover_random_number()
        print('decrypting...')

