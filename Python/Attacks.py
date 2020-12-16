import hashlib
import string
import random
import time

# Find collisions faster than the usual comparison method with the birthday paradox
# Parameter `bit_range` is the number of bits you want to collide
# TO-DO : use Rho method to reduce the complexity
def birthday_collisions_attack(bit_range):
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str.encode()
        space_size = bit_range//4
    for i in range(100):
        t1 = time.time()
        lookup_table = {}
        # Optimalement 2**(bit_range//2)
        for _ in range(60000000):
            random_binary = get_random_string(12)
            result = hashlib.sha256(random_binary).hexdigest()[:space_size]
            lookup_table[result] = random_binary
        for _ in range(60000000):
            random_binary2 = get_random_string(12)
            result2 = hashlib.sha256(random_binary2).hexdigest()[:space_size]
            if result2 in lookup_table and lookup_table[result2] != random_binary2:
                print(random_binary2)
                print(lookup_table[result2])
                break
        t2 = time.time()
        print(t2-t1)
