from find_sequence import *
import pytest

def test_find_sequence_zero_len_pattern():
    assert find_sequence("","") == 0
    assert find_sequence("a","") == 0
    assert find_sequence([],[]) == 0
    assert find_sequence([1],[]) == 0

def test_find_sequence_simple_pattern():
    assert find_sequence([2,1,2,1],[1]) == 1

def test_find_sequence_complex():
    assert find_sequence([1,3,2,2,1,3,2,2,1],[2,2]) == 2

def test_find_sequence_at_ends():    
    assert find_sequence([1,2,3],[2,3]) == 1
    assert find_sequence([1,2,3],[3]) == 2
    assert find_sequence([1,2,3],[1,2,3]) == 0
    assert find_sequence([1,2,3],[1]) == 0

def test_find_sequence_versions_with_strings():  
    check_find("", "")
    check_find("", "a")
    check_find("a", "")
    check_find("h", "h")
    check_find("hello", "l")
    check_find("hello", "lo")
    check_find("hello", "elo")
    check_find("hello", "ell")
    check_find("hello", "h")
    check_find("hello", "o")
    check_find("hello", "O")
    
def check_find(text, pattern):    
    assert find_sequence(text, pattern) == text.find(pattern)
    assert find_sequence_v1(text, pattern) == text.find(pattern)
    assert find_sequence_v2(text, pattern) == text.find(pattern)
    assert find_sequence_v3(text, pattern) == text.find(pattern)

def test_subsequence_match_bad_start_index():
    with pytest.raises(IndexError):
        subsequence_match("abc","c",3)
    with pytest.raises(IndexError):
        subsequence_match("abc","c",-4)
    with pytest.raises(IndexError):
        subsequence_match("abc","cc",2)

def test_subsequence_match():
    assert subsequence_match("","", 0) == True
    assert subsequence_match("a","", 0) == True
    assert subsequence_match("ab","", 1) == True
    assert subsequence_match("abc","c",0) == False
    assert subsequence_match("abc","c",1) == False
    assert subsequence_match("abc","c",2) == True
    assert subsequence_match("abc","c",-3) == False
    assert subsequence_match("abc","c",-2) == False
    assert subsequence_match("abc","c",-1) == True
    assert subsequence_match("abcd","bc",1) == True
    assert subsequence_match("abcd","bc",0) == False
    assert subsequence_match("abcd","abc",0) == True
    assert subsequence_match("abcd","bcd",1) == True
    assert subsequence_match("abcd","d",3) == True


