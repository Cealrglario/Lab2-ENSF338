import timeit
import random
import scipy
import numpy as np

# PART 1

def linear_search(data, key):
    for i in range(len(data)):
        if data[i] == key:
            return i
    return -1

def binary_search(data, low, high, key):
    if high >= low:
        
        mid = (high + low) // 2

        if data[mid] == key:
            return mid

        if data[mid] > key:
            binary_search(data, low, mid - 1, key)
        else:
            binary_search(data, mid + 1, high, key)
    
    else:
        return -1

# PART 2

"""

times_taken_linear = []
times_taken_binary = []

for i in [1000, 2000, 4000, 8000, 16000, 32000]:
    time_taken_binary = 0
    time_taken_linear = 0
    for j in range(1000):

        vector = list(range(i))
        rand = random.randint(0, i - 1)

        time_taken_linear += timeit.timeit(lambda: linear_search(vector, rand), number=100)
        time_taken_binary += timeit.timeit(lambda: binary_search(vector, 0, i, rand), number=100)

    times_taken_linear.append(time_taken_linear / 1000)
    times_taken_binary.append(time_taken_binary / 1000)

print(f"Times for linear search: {times_taken_linear}") 
# Times for linear search: 
# [0.0016881841001886641, 0.003661749600083567, 0.00739551550001488, 0.01569475700010662, 0.03233653780019086, 0.06321908050014463]

print(f"Times for binary search: {times_taken_binary}")
# Times for binary search: 
# [0.00014319270008127205, 0.00016219960007583722, 0.00018089720007264987, 0.00019989000022178517, 0.00022064459994726348, 0.0002375494998850627]

"""

# PART 3

times_taken_linear = [0.0016881841001886641, 0.003661749600083567, 0.00739551550001488, 0.01569475700010662, 0.03233653780019086, 0.06321908050014463]
times_taken_binary = [0.00014319270008127205, 0.00016219960007583722, 0.00018089720007264987, 0.00019989000022178517, 0.00022064459994726348, 0.0002375494998850627]


def log(n, a, b):   # y = a(log(n)) + b
    return a * np.log(n) + b

def linear(n, m, b): # y = mn + b
    return m * n + b

log_params = scipy.optimize.curve_fit(log, [1000, 2000, 4000, 8000, 16000, 32000], times_taken_binary)

linear_params = scipy.optimize.curve_fit(linear, [1000, 2000, 4000, 8000, 16000, 32000], times_taken_linear)

print(f"Function for binary search: f(n) = {log_params[0][0]}log(n) + {log_params[0][1]}")
print(f"Function for linear search: f(n) = {linear_params[0][0]}(n) + {linear_params[0][1]}")

# Fuction for binary search: f(n) = 2.7457033955570277e-05log(n) + -4.651695205324285e-05
# Function for linear search: f(n) = 1.9937325106896526e-06(n) + -0.0002682205552768944

# PART 4

"""

We use a logarithmic fit for binary search since we know binary search has O(log(n)).
We use a linear fit for linear search since we know linear search has O(n).

The important thing to note is that the second parameters are relatively small, indicating
that the fit chosen is appropriate - we would expect a small value for b in log(n) + b if we
are assuming that the complexity is O(log(n)). We can also confirm these values using pyplot:
the binary search is slower initially, but very quickly becomes more efficient as
the x-axis is traversed.

"""