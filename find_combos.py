def find_combos(chars, k):
    """Given a set of characters (chars) and an integer (k), return a list of 
    all possible strings of length k that can be formed, sorted alphabetically.

    >>> find_combos(set(['a','b','c']), 2)
    ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']

    >>> find_combos(set(['a','b','c']), 3)
    ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']

    >>> find_combos(set(['a','b']), 2)
    ['aa', 'ab', 'ba', 'bb']

    >>> find_combos(set(['a','b']), 3)
    ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']

    >>> find_combos(set(['a']), 1)
    ['a']

    >>> find_combos(set(['a']), 2)
    ['aa']
    """

    char_strings = list(chars)

    i = 1

    while i < k:
        new_strings = []
        for char in chars:
            for char_string in char_strings:
                new_strings.append(char_string + char)

        char_strings = new_strings[:]
        i += 1

    char_strings.sort()

    return char_strings



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS! ***\n")




