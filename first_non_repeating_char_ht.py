def first_non_repeating_char(string):
    # generate a dictionary of character counts
    # then iterate through the counts, checking for count==1
    counts = {}
    for c in string:
        counts[c] = counts.get(c, 0) + 1
        
    for k, v in counts.items(): # order will always be guaranteed in Python 3.7+
        if v == 1:
            return k
    return None



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
