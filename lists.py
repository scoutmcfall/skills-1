"""Skills 1: lists.py

Complete the following functions. To get a better idea of how each function
should behave, see the examples in test_lists.py.
"""


def get_words_by_first_letter(words, letter):
    """Return a list of all words that start with the given letter."""
    word_l = []
    for word in words:
        if letter in word[0]:
            word_l.append(word)
    return word_l
    # TODO: replace this with your code


def filter_by_length(items, length):
    """Return a list of all items with the given length."""
    item_l = []
    for item in items:
        if len(item) == length:
            item_l.append(item)
    return item_l    
    
    # TODO: replace this with your code


def words_in_common(words1, words2):
    """Return strings that words1 and words2 have in common."""
    in_common = []
    for word in words1:
        if word in words2:
            in_common.append(word)
            #get rid of duplicates somehow- use a set and then a list?
    for i in in_common:
       if i in in_common[1:]:
           #take the word out
           in_common.pop(in_common[i])
    #in_common = set(in_common)
    return in_common
    
#am I just comparing words 1 and 2?
    #if words1 == words2:
        #in_common.append(words1)
    #return in_common


def every_other_item(items):
    """Return a list with every other element items (start with index 0)."""
    every_other = []
    #for item in items:
        #every_other.append(item)
        #items[i]
    every_other.extend(items[0::2])
    return every_other 
    # TODO: replace this with your code


def smallest_n_items(items, n):
    """Return the n smallest values in the given list, in descending order.

    You can assume that `n` will be less than the length of the list.
    """
    items.sort()
    #list.reverse()?
    smallest_items = items[0:n]
    smallest_items.reverse()
    return smallest_items
    # TODO: replace this with your code


def get_index(items, value):
    """Search for a value in items and return its index.

    If the value doesn't exist in items, return None. If the value appears more
    than once, return the index of the first occurrence of the value.
    """
    #index = []
    for i in range(len(items)):
        if items[i] in value:
            #index = items[i]
            return i #still not returning the index
        elif value not in items[i]:
            continue
        else:
            return None
    #return index
    #index = []
    #for i in items:
        #if items[i] in value:
            #index.append(i)
    #return index
    
    #make a list of tuples consisting of value, index
    #if value in tuple list, return index?


if __name__ == "__main__":
    import sys
    from pathlib import Path

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        try:
            import pytest
            pytest.main([f"test_{Path(__file__).name}"])
        except ModuleNotFoundError:
            print("Unable to run tests because 'pytest' wasn't found :(")
            print("Run the command below to install pytest:")
            print()
            print("    pip3 install pytest")
