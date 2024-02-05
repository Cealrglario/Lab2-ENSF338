'''
3.1) A profiler is a tool used to measure a program's performance by analyzing information about its execution. It allows
developer insight into time spent in different areas of a program's code, and thus allows developers to identify areas
within a program that could use more optimization/streamlining. 

There are two main types of profilers. The deterministic profiler records the time spent in each function within a program, and also
how many times a certain function is called. Mainly used to identify bottlenecks within a program. A statistical profiler 
analyzes the state of a program at certain recorded intervals, rather than measuring how many times a function is called. 
This instead provides a statistic on what areas of the code the program spends the most time in, rather than discrete data in the form 
of how many times a function is called/time spent within each function.

3.2) Benchmarking is typically used to measure the performance of a function or an entire program against a set standard to determine,
relative to a set of criteria, how well your program/function runs. Meanwhile, profiling does not compare your code to a set standard.
Profiling is moreso used to identify "weak points" within your code, so that you can optimize/streamline those bottlenecks. In
layman's terms, benchmarking is a comparison of your code to some set standard, meanwhile profiling is the process of
identifying what parts of your code are not up to par so that you can speed up your program.

'''

# 3.3)

import timeit
import cProfile

def sub_function(n):
    # Sub-function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # Third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

profiler = cProfile.Profile()

profiler.enable()

test_function()
third_function()

profiler.disable()

profiler.print_stats()

'''
3.4) The VAST majority of the execution time of the above code relied within "third_function". Other functions were called much more,
such as "sub_function" being called more than "third_function", but despite that, "third_function" took up almost the entire
execution time of the code. If we were to try to optimize the code above, we would definitely start at trying to optimize
"third_function".

'''