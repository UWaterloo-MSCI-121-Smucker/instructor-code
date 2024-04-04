from remove_duplicates import remove_duplicates

def test_remove_duplicates_empty():
    assert remove_duplicates([]) == []

def test_remove_duplicates_one():
    assert remove_duplicates([1]) == [1]

def test_remove_duplicates_two():
    assert remove_duplicates([1,1]) == [1]
    assert remove_duplicates([1,2]) == [1,2]
    assert remove_duplicates([2,1]) == [2,1]

def test_remove_duplicates_long():
    assert remove_duplicates([5,78,2,3,78,1,78,1,5,0]) == [5,78,2,3,1,0]
    assert remove_duplicates([1,1,1]) == [1]
    assert remove_duplicates([2,1,1,4,1,1,1,1,1,1,5,-1,6,2]) == [2,1,4,5,-1,6]



