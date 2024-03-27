"""
Tweaked HackerRank CountSort Problem.
Link: https://www.hackerrank.com/challenges/countingsort2/problem
Performance: Too Slow
Time Complexity: O(n^2)
"""

def selectionSort(arr):
    # create storage
    sorted_arr = []
    # compare current element with all others until the smallest is found
    # remove the smallest and add it to storage
    while len(arr) >= 1:
        smallest = arr[0]
        smallest_idx = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_idx = i
        # print(smallest)
        sorted_arr.append(arr.pop(smallest_idx))
    return sorted_arr
      
