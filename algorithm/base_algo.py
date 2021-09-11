import random
from abc import ABC, abstractmethod

class BaseAlgo:
    def __init__(self, seed, key, image_shape):
        random.seed(seed)
        self.generated_random_num = []
        self.key = key
        self.image_shape = image_shape

    @abstractmethod
    def recover_random_number(self):
        pass

    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass

