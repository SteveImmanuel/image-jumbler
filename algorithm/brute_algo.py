import random
from .base_algo import BaseAlgo

class BruteAlgo(BaseAlgo):
    def recover_random_number(self):
        super().recover_random_number()

        for i in range(self.img_arr.shape[0]):
            for j in range(self.img_arr.shape[1]):
                x = random.randrange(0, self.img_arr.shape[0])
                y = random.randrange(0, self.img_arr.shape[1])
                self.generated_random_num.append((x,y))
    
    def encrypt(self):
        super().encrypt()

        for i in range(self.img_arr.shape[0]):
            for j in range(self.img_arr.shape[1]):
                x = random.randrange(0, self.img_arr.shape[0])
                y = random.randrange(0, self.img_arr.shape[1])
                
                temp = self.img_arr[i][j].copy() 
                self.img_arr[i][j] = self.img_arr[x][y].copy() 
                self.img_arr[x][y] = temp 

    def decrypt(self):
        super().decrypt()

        for i in range(self.img_arr.shape[0] - 1, -1, -1):
            for j in range(self.img_arr.shape[1] - 1, -1, -1):
                x, y = self.generated_random_num.pop()

                temp = self.img_arr[i][j].copy() 
                self.img_arr[i][j] = self.img_arr[x][y].copy() 
                self.img_arr[x][y] = temp 