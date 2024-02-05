# Question 1

Interpolation search is more effective than binary search for the following reasons: it can find the key in fewer divisions of the array, since it will be more accurate
in locating the expected location of the key. Its performance also improves when data is uniformly distributed, since it estimates based on a slope calculation.

# Question 2

Interpolation search heavily relies on the assumption that data is uniformly distributed. In cases where data is not, its performance will suffer, with the potential
of becoming even slower than binary search for extremely slanted datasets.

# Question 3

If the data will not be linear, but will be predictable according to some other distribution, we can implement that distribution in the calculation step of the algorithm.
(That is, the part where we calculate the "slope" of the data -- (y1 - y2)  / (x1 - x2).)

# Question 4

If data is not sorted, linear search is the only valid option (of the three offered), since both binary and interpolation search require sorted data in order to function
properly. If either of these algorithms were run on unsorted data (even if just one element was out of place!), it would have the potential to fail. Although it is not
impossible that these algorithms could succeed on unsorted data, that would rely on sheer luck. They're cheating -- they could technically be right, but never could be trusted.

# Question 5

Linear search will always* outperform binary and interpolation search when the key is the first value in the dataset. This is linear's best case, which is O(1), and 
the worst case for the others: O(log(n)). (*it'll need to be a dataset larger than one item, or they'll tie.)

# Question 6

If you were concerned about this edge case, you could "improve" the algorithms by having them check the first and last elements of the array before beginning, or alternatively, you could do the first split of the array and then compare to the first or last element depending on the key <-> middle comparison. Obviously, this
is not a great idea unless you're expecting the key to be explicitly the first or last element of the array. (It slows down n-2 cases to speed up only 2.)
