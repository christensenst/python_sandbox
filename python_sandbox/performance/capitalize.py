""" Test speed for capitalize(), upper(), and string.capwords()

    Results:
    Testing str.upper():
    0:00:00.571233
    Testing str.capitalize():
    0:00:00.448530
    Testing string.capwords():
    0:00:02.089745
"""

from datetime import datetime
import string

SINGLE = 'gonnacapitalizethisthing'

if __name__ == '__main__':
    print "Testing str.upper():"
    start = datetime.now()
    for i in range(1000000):
        word = SINGLE
        word = word.upper()
    print datetime.now() - start
    print "Testing str.capitalize():"
    start = datetime.now()
    for i in range(1000000):
        word = SINGLE
        word = word.capitalize()
    print datetime.now() - start
    print "Testing string.capwords():"
    start = datetime.now()
    for i in range(1000000):
        word = SINGLE
        word = string.capwords(word)
    print datetime.now() - start
