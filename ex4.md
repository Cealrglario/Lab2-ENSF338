# Question 1 

Considering EY128 is an even numbered room, we can start at EY100 and iterate by 2 to ignore odd numbered rooms. 
Assuming for the sake of an example that the rooms are ordered in an "array", we can start at i=0 and iterate by i+2
until i is equal to 28, which is when we've found room EY128. Such code might look like this:

for (i = 0; i != 28; i+=2);

# Question 2

It should, in theory, take 14 steps to reach EY128 if we start at i=0 and iterate by 2 until we reach i=28. In this case,
a 'step' is simply the iteration of i by 2 until is is equal to 28, which would signify the reaching of the room EY128.

# Question 3

It's neither a best nor worst case scenario. It is VERY close to being a worst case scenario, since EY128 would be
very close to the end of an array of rooms from EY100 to EY130, but it is technically not the worst case scenario,
as that would be if we were looking for EY130.

# Question 4

A best case scenario would be if we were looking for EY100, where in this case it'd simply be the very first room in the 
hypothetical array of rooms. A worst case scenario would be if we were looking for EY130, as that would be the very last
room in the array of rooms, and we'd need to iterate over the entire array before reaching our desired room.

# Question 5

Considering the rooms are all sorted in order, a way to optimimize the searching of a specific room would simply be to use
binary search. We could divide the "array of rooms" in half by taking the minimum and maximum value and then dividing that by two then
flooring the result which would give us the index of the midpoint of the array. Then, we can split the array in half with the midpoint index, and then compare the value at the midpoint index and the value that we are searching for. From here, we can decide to search either the lower or upper half of the array based on where the value that we're searching for is relative to the midpoint, and then call the search algorithm recursively on the smaller half of the array we choose to search. This would repeat all above processes (including the splitting of the array and the comparison of the value in question and the midpoint) over and over until either the value we're searching for is finally at the midpoint index of the array, or until the first value in the smallest subarray becomes larger then the last value in the subarray, which would indicate that you've searched all values in the array and didn't find the value in question at all.

An implementation of a binary search would reduce time wasted on searching large parts of the array where the value in question definitely ISN'T (for example, searching the entire first three quarters of an array with linear search even though we know the value is in the last quarter of the array).