from top_scores import TopScores
import pytest

def test_top_scores_empty():
    "Test to make sure an empty list behaves like an empty list."
    ts = TopScores()
    assert len(ts) == 0
    with pytest.raises(IndexError):
        ts.get_player(0)
    with pytest.raises(IndexError):
        ts.get_score(0)


def test_top_scores_one():
    "Test to make sure a single element in the list is only a single element."
    ts = TopScores()
    ts.add("Mark",121)
    assert len(ts) == 1
    assert ts.get_player(0) == "Mark"
    assert ts.get_score(0) == 121
    with pytest.raises(IndexError):
        ts.get_player(1)
    with pytest.raises(IndexError):
        ts.get_score(1)

    
def test_top_scores_size_one():
    "If we set the list to max size 1, it should only hold on to the max player score."
    ts = TopScores(1)
    ts.add("Mark",121)
    ts.add("Bob",12) # Bob should not get added
    assert len(ts) == 1
    assert ts.get_player(0) == "Mark"
    assert ts.get_score(0) == 121
    with pytest.raises(IndexError):
        ts.get_player(1)
    with pytest.raises(IndexError):
        ts.get_score(1)
    ts.add("Fred",121.1) # Fred should replace Mark
    assert len(ts) == 1
    assert ts.get_player(0) == "Fred"
    assert ts.get_score(0) == 121.1

def test_top_scores_size_three():
    "If we set the list to max size 3, it should handle many cases."
    ts = TopScores(3)
    assert len(ts) == 0
    ts.add("Mark",121)
    assert len(ts) == 1
    ts.add("Bob",12) # add to end
    assert len(ts) == 2
    ts.add("Fred",121.1) # Move to Front
    assert len(ts) == 3
    assert ts.get_player(0) == "Fred"
    assert ts.get_score(0) == 121.1
    with pytest.raises(IndexError):
        ts.get_player(3)
    with pytest.raises(IndexError):
        ts.get_score(3)
    assert ts.get_player(1) == "Mark"
    assert ts.get_score(1) == 121
    assert ts.get_player(2) == "Bob"
    assert ts.get_score(2) == 12
    # Now add something to middle of pack
    ts.add("Middle",121.01)
    assert len(ts) == 3
    assert ts.get_player(0) == "Fred"
    assert ts.get_score(0) == 121.1
    assert ts.get_player(1) == "Middle"
    assert ts.get_score(1) == 121.01
    assert ts.get_player(2) == "Mark"
    assert ts.get_score(2) == 121
    # add, but no change
    ts.add("End",0)
    assert len(ts) == 3
    assert ts.get_player(0) == "Fred"
    assert ts.get_score(0) == 121.1
    assert ts.get_player(1) == "Middle"
    assert ts.get_score(1) == 121.01
    assert ts.get_player(2) == "Mark"
    assert ts.get_score(2) == 121
    # add at end
    ts.add("NewEnd",121.00001)
    assert len(ts) == 3
    assert ts.get_player(0) == "Fred"
    assert ts.get_score(0) == 121.1
    assert ts.get_player(1) == "Middle"
    assert ts.get_score(1) == 121.01
    assert ts.get_player(2) == "NewEnd"
    assert ts.get_score(2) == 121.00001
    # head of pack
    ts.add("Head",1000)
    assert len(ts) == 3
    assert ts.get_player(0) == "Head"
    assert ts.get_score(0) == 1000
    assert ts.get_player(1) == "Fred"
    assert ts.get_score(1) == 121.1
    assert ts.get_player(2) == "Middle"
    assert ts.get_score(2) == 121.01











