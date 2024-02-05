'''
1.1) The code implements the Fibonacci sequence up to n numbers using recursion. It simply calls
smaller iterations of itself until n is 0 or 1, then adds everything up from there.

1.2) No. While divide and conquer algorithms typically use recursion, this implementation does not actually "divide"
any data to make the processing of said data easier in any way. Divide and conquer algorithms must, in some way, divide a given 
piece of data over and over until it can be processed in the smallest possible blocks, making processing of it quicker than
if it were processed as one large, whole block.

1.3) The function is O(2^n) since each call of the function calls two more iterations of the function. One turns into two turns into four,
so on so forth.

'''

## 1.4)
## Note, I used ChatGPT to help provide ideas as to how to "memoize" the given function.

def func(n):
    if n == 0 or n == 1:
        return n
    
    else:
        return func(n-1) + func(n-2)

cache = {0: 1, 1: 1}

def opt_func(n):
    if n in cache:
        return cache[n]
    
    else:
        cache[n] = opt_func(n-1) + opt_func(n-2)

    return cache[n]
    
'''

1.5) The optimized algorithm has a time complexity of O(n) since it does not need to recursively calculate numbers already stored within
the cache. For example, if you've already calculated func(14), then func(15) simply uses the cache to complete its calculation instead of 
recursively calling itself over and over again.

'''
## 1.6)

import timeit
import matplotlib.pyplot as plt

unoptimized_results = []
optimized_results = []

for i in range(35):
    time_taken = timeit.timeit(lambda:func(i), number = 1)
    unoptimized_results.append(time_taken)

for i in range(35):
    time_taken = timeit.timeit(lambda:opt_func(i), number = 1)
    optimized_results.append(time_taken)

plt.plot(range(35), unoptimized_results)
plt.xlabel("n")
plt.ylabel("time")
plt.ylim(0, 0.8)
plt.savefig("ex1.6.1.jpg")
plt.close()

plt.plot(range(35), optimized_results)
plt.ylabel("time")
plt.xlabel("n")
plt.ylim(0, 0.000008)
plt.savefig("eg1.6.2.jpg")
plt.close()
