"""
Examples of using collections.Counter
Counter objects support convenient and rapid tallies
"""

from collections import Counter

def most_common_word(phrase):
    data = phrase.split()
    
    # produces: Counter({'and': 3, 'like': 3, 'to': 3, 'run': 2, 'on': 1, 'code': 1, 'I': 1,
    #                   'guitar': 1, 'jam': 1, 'the': 1, 'really': 1})
    tally = Counter(data)
    
    # if there is a tie, choose the first one alphabetically 
    # can't use most_common() for key because order is random 
    max_count = tally.most_common(1)[0][1]
    max_words = [k for k,v in tally.items() if v == max_count]
    return max_words[0]

if __name__ == '__main__':
    crazy_phrase = "I like to code and like to run and code code and really like to jam on the guitar while code code"
    popular_word = most_common_word(crazy_phrase)
    print popular_word