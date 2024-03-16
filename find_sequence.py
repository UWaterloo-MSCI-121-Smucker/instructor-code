
# In this file I show several different ways of writing find_sequence, which
# is basically a version of str.find that works for lists or any sequence, e.g.
# it also works for strings.

# This is the version I showed in class, March 15, 2024.  I don't
# like how it has this strange check for j == len(pattern)-1 at 
# each step of the inner loop.  Also, I think using break can be 
# confusing for students.
def find_sequence_v1(text, pattern):
    """
    This function takes as input two lists.  The function
    returns the index of the first occurence of the pattern 
    found in the text.  For example find_sequence([1,3,2,3,2],[3,2]) 
    returns 1. If the pattern is not found in the text, the 
    function returns -1.
    """
    if len(pattern) == 0:
        return 0
    if len(pattern) > len(text):
        return -1
    
    for i in range(len(text)-len(pattern)+1):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break

            if j == len(pattern)-1:
                return i
            
    return -1

# So, I rewrote find_sequence_v1 into this function that uses
# while loops and a flag named found_match to exit the inner
# loop early rather than use a break statement.  
def find_sequence_v2(text, pattern):
    """
    This function takes as input two lists.  The function
    returns the index of the first occurence of the pattern 
    found in the text.  For example find_sequence([1,3,2,3,2],[3,2]) 
    returns 1. If the pattern is not found in the text, the 
    function returns -1.
    """
    i = 0 
    while i < len(text)-len(pattern)+1:
        j = 0
        found_match = True
        while j < len(pattern) and found_match:
            if text[i+j] != pattern[j]:
                found_match = False            
            j = j + 1
        if found_match:
            return i
        i = i + 1
    return -1                      

# This is a version I wrote that I think is easier to understand
# and shows how breaking your solution into functions can often
# make it easier to solve.
def find_sequence_v3(text, pattern):
    """
    This function takes as input two lists.  The function
    returns the index of the first occurence of the pattern 
    found in the text.  For example find_sequence([1,3,2,3,2],[3,2]) 
    returns 1. If the pattern is not found in the text, the 
    function returns -1.
    """
    for i in range(len(text)-len(pattern)+1):
        if subsequence_match(text, pattern, i):
            return i
    return -1 

def subsequence_match(text, pattern, start_index):
    """
    This function returns true if the pattern matches the subsequence of
    the same length as the pattern starting at text[start_index], otherwise
    it returns false.  If len(pattern) is zero, this function always
    returns True.  The start_index must reference an element in 
    range(len(text)-len(pattern)+1) or else an IndexError will occur.
    """    
    for i in range(len(pattern)):
        if text[start_index + i] != pattern[i]:
            return False
        
    return True


# this is the same as find_sequence_v3, but uses slicing instead of
# a function to check if the sequence matches.  So, if you understand
# slicing, this version is the simplest to read, and also saves you 
# the trouble of having to test the subsequence match function. It does
# rely on the fact that a slice of [0:0] on a len zero sequence is the
# empty sequence, which I find super subtle, but with lots of tests, I
# am confident it works correctly.  I doubt that I would have been able 
# to write this function correctly without lots of testing.
def find_sequence(text, pattern):
    """
    This function takes as input two lists.  The function
    returns the index of the first occurence of the pattern 
    found in the text.  For example find_sequence([1,3,2,3,2],[3,2]) 
    returns 1. If the pattern is not found in the text, the 
    function returns -1.  If len(pattern) is zero, 
    """
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            return i
    return -1 










