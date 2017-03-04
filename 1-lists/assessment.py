"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """

    """Uses new variable called odd_nums to capture list comprehension
    of numbers argument if number modulus 2 is not zero, which would
    indicate an odd number.
    """

    odd_nums = [number for number in numbers if number % 2 != 0]

    return odd_nums

    """
    ALTERNATE ANSWER:

    odd_nums = []

    for number in numbers:
        if number % 2 != 0:
            odd_nums.append(number)

    return odd_nums

    """


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

        >>> print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])
        0 Toyota
        1 Jeep
        2 Toyota
        3 Volvo
    
    """

    """Uses range to iterate over the argument's indices, and print the 
    index and the value at the index.
    """
    
    for idx in range(len(items)):
        print idx, items[idx]


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale", "zebra cakes"],
        ...     ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ]
        ... )
        ['bagel', 'cake', 'cheese', 'kale']
        
    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """

    """Uses new variable called common_foods to capture list comprehension
    of food1 argument if food is in foods2.
    """

    common_foods = [food for food in foods1 if food in foods2]

    return sorted(common_foods)

    """
    ALTERNATE ANSWER:

    # common_foods = []

    # for food in foods1:
    #     if food in foods2:
    #         common_foods.append(food)

    return sorted(common_foods)

    """ 


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """

    """Uses new variable called every_other to capture list comprehension
    of items argument for all items, counting by 2 steps.
    """

    every_other = [item for item in items[::2]]
    return every_other

    """
    ALTERNATE ANSWER:

    every_other = []

    for item in items[::2]:
        every_other.append(item)

    return every_other

    """


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """

    """Uses n to slice items argument after list is sorted, to capture
    largest items. Returns empty list if n == 0.
    """

    if n == 0:
        return []
    else:
        return sorted(items)[-n:]

    """
    ALTERNATE ANSWER:

    sorted_nums = sorted(items)[::-1]
    return sorted(sorted_nums[:n])

    """


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
