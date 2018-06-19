# Title Capitalization
#
# Many writers are often confused by the different methods of capitalizing titles. There are
# several forms of capitalization rules, but one of the most popular is called "title case" or "up
# style."
#
# Implement a function that will take a title in the form of a string and return the string
# with the correct capitalization for a title according to these rules.
# - Always capitalize the first word in a title.
# - Always capitalize the last word in a title.
# - Lowercase the following words, unless they are the first or last word of the title:
# "a", "the", "to", "at", "in", "with", "and", "but", "or."
# - Uppercase any words not in the list above.
# - A word is defined as a series of non-space characters.
#
# Example 1: "i love solving problems and it is fun"
# Would return "I Love Solving Problems and It Is Fun"
# Example 2: "wHy DoeS A biRd Fly?"
# Would return "Why Does a Bird Fly?"

import sys
lower_list = ['a', 'the', 'to', 'at', 'in', 'with', 'and', 'but', 'or']
title = sys.argv[1]

def capitalize_title(title):
    words = title.split(' ')
    new_title = []
    for i, word in enumerate(words):
        if (i == 0) or (i == len(words) - 1): new_title.append(word.capitalize())
        elif word in lower_list: new_title.append(word.lower())
        else: new_title.append(word.upper())
    return ' '.join(new_title)


capitalized_title = capitalize_title(title)
print 'Original title: {} | Capitalized title: {}'.format(title, capitalized_title)
