import random

def generate_random_list(n):
    result = []
    for i in range(n):
      x = random.randint(1,n)
      if x not in result:
            result.append(x)]
    return result


## Don't edit testcases below, it's cheating!

import time

# SMALL TEST
start = time.time()
generate_random_list(100)
test_time = (time.time() - start) * 1000
print(f'Small test took {test_time:.1f} ms')
assert test_time < 100, 'Too slow!'

# LARGE TEST
start = time.time()
generate_random_list(20000)
test_time = (time.time() - start) * 1000
print(f'Large test took {test_time:.1f} ms')
assert test_time < 100, 'Too slow!'
