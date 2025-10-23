def find_duplicates(nums):
    # check if item in nums exists before adding to uniques.
    # if true, set value to True, otherwise keep False
    uniques = {}
    for i in nums:
        if uniques.get(i) is None:
            uniques[i] = False
        else:
            uniques[i] = True
    
    # generate duplicates output
    duplicates = [k for k, v in uniques.items() if v]
    return duplicates



print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""


"""
ALT Solution:
def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
 
    duplicates = []
    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)
 
    return duplicates
"""
