from base_algo import BaseAlgo
from abc import override

class WeaveAlgo(BaseAlgo):
    @override
    def recover_random_number(self):
        return super().recover_random_number()
    
    @override
    def encrypt(self):
        return super().encrypt()

    @override
    def decrypt(self):
        return super().decrypt()
        