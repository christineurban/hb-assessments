"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """


    """ Takes a string of words and returns the count of each word.

        Counts the number of times each word appears and assigns the
        word to a key and the number of time it appears to a value,
        returns a dictionary.
    """
    words = phrase.split()
    unique_words = {}

    for word in words:
        unique_words[word] = unique_words.get(word, 0)
        unique_words[word] += 1

    return unique_words


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    """Given melon, returns price of melon.

    If melon is not in melons dictionary, returns 'No price found'
    """

    melons = {"Watermelon": 2.95,
              "Cantaloupe": 2.50,
              "Musk": 3.25,
              "Christmas": 14.25,
             }

    if melon_name in melons:
        print melons[melon_name]
    else:
        print "\'No price found\'"


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    """Given a list of words, returns a list of tuples by word length.

    Returns a sorted list, and the nested lists are sorted as well.
    """

    alpha_words = sorted(words)  
    # words sorted here so they enter the value list sorted

    char_count_dict = {}

    for word in alpha_words:
        word_len = len(word)

        char_count_dict[word_len] = char_count_dict.get(word_len, [])
        # if word length not in dictionary as key,
        # adds it with a value of an empty list

        char_count_dict[word_len].append(word)
        # adds the word to the value list of the key of its length

    return sorted(char_count_dict.items())


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    """Translates a given phrase from English to Pirate.

    If word is not in the english_to_pirate dictionary, returns the same word
    to the sentence.
    """

    english_to_pirate = {"sir": "matey",
                         "hotel": "fleabag inn",
                         "student": "swabbie",
                         "man": "matey",
                         "professor": "foul blaggart",
                         "restaurant": "galley",
                         "your": "yer",
                         "excuse": "arr",
                         "students": "swabbies",
                         "are": "be",
                         "restroom": "head",
                         "my": "me",
                         "is": "be",
                        }

    words = phrase.split()  # splits the string into a list of words
    pirate_speak = ""

    for word in words:
        if word in english_to_pirate:
            pirate_speak += english_to_pirate[word] + " "
        else:
            pirate_speak += word + " "

    return pirate_speak.strip()  # removes the last space that was added


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    """Take list of words and follow chain rules to produce new list of words.
    """

    name_dict = {}
    game_results = [names[0]]
    used_words = []
    current_word = names[0]

    # ADDING KEYS
    for name in names:
        last_letter = name[-1]
        
        name_dict[last_letter] = name_dict.get(last_letter, [])
        # if last_letter key not in dictionary,
        # adds it with a value of an empty list


    # ADDING VALUES
    for name in names:
        first_letter = name[0]

        if first_letter in name_dict:
            name_dict[first_letter].append(name)
        # if first letter of name matches a last letter key in 
        # dictionary, add that name to the value list



    # ADDING TO GAME RESULTS
    while current_word[-1] in name_dict and current_word not in used_words:
    # while the last letter of the current word is in the dictionary and is
    # also not in used_words
        used_words.append(current_word)
        # add word to used words

        for word in name_dict[current_word[-1]]:
        # for each word in the value list
            if word not in used_words:
            # if the word hasn't been used yet
                game_results.append(word)
                # add word to game results
                current_word = word
                # change current word to word
                break
                # jump out of loop since word has been added


    return game_results

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
