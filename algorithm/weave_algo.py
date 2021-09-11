import random
from .base_algo import BaseAlgo

class WeaveAlgo(BaseAlgo):
    def recover_random_number(self):
        super().recover_random_number()

        for i in range(self.img_arr.shape[0]):
            rand_num = random.randrange(0, self.img_arr.shape[0])
            self.generated_random_num.append(rand_num)
        
        for i in range(self.img_arr.shape[1]):
            rand_num = random.randrange(0, self.img_arr.shape[1])
            self.generated_random_num.append(rand_num)
    
    def encrypt(self):
        super().encrypt()

        for i in range(self.img_arr.shape[0]):
            rand_num = random.randrange(0, self.img_arr.shape[0])
            self.img_arr[[i, rand_num]] = self.img_arr[[rand_num, i]]
        
        for i in range(self.img_arr.shape[1]):
            rand_num = random.randrange(0, self.img_arr.shape[1])
            self.img_arr[:, [i, rand_num]] = self.img_arr[:, [rand_num, i]]


    def decrypt(self):
        super().decrypt()

        for i in range(self.img_arr.shape[1] - 1, -1, -1):
            rand_num = self.generated_random_num.pop()
            self.img_arr[:, [i, rand_num]] = self.img_arr[:, [rand_num, i]]
            
        for i in range(self.img_arr.shape[0] - 1, -1, -1):
            rand_num = self.generated_random_num.pop()
            self.img_arr[[i, rand_num]] = self.img_arr[[rand_num, i]]
        