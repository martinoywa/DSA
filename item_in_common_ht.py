# Uses a dictionary to solve the problem that creates an O(n) time complexity.
def item_in_common(list1, list2):
    # generate a dict from items in list1
    # check if list2 has an item as key in dict
    list1_dict = {k: 1 for k in list1}
    for i in list2:
        if list1_dict.get(i) is not None:
            return True
    return False



list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""
