from reverse import reverse_list

def test_reverse_list_odd():
    start = [1,2,3,4,5]
    expected = [5,4,3,2,1]
    reverse_list(start)
    #assert start == excepted
    for i in range(len(start)):
        assert start[i] == expected[i]

def test_reverse_list_empty():
    start = []
    expected = []
    reverse_list(start)
    assert start == expected

def test_reverse_list_even():
    start = [1,2,3,4]
    expected = [4,3,2,1]
    reverse_list(start)
    assert start == expected

def test_reverse_list_one_elt():
    start = [1]
    expected = [1]
    reverse_list(start)
    assert start == expected
    