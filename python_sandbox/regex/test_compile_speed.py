from datetime import datetime
import re

def keep_alphabet_char_and_single_spaces(element):
    result = re.sub('[^a-zA-Z ]', '', element)
    return re.sub(' +', ' ', result)

find_alphabet_char_and_spaces = re.compile('[^a-zA-Z ]')
find_multispaces = re.compile(' +')

def keep_alphabet_char_and_single_spaces_compiled(element):
    result = find_alphabet_char_and_spaces.sub('', element)
    return find_multispaces.sub(' ', result)

if __name__ == '__main__':
    x = 'One 1   Two 2      Three 3 Done'
    print "Testing regex without compiling"
    start_first = datetime.now()
    for i in range(1000000):
        result = keep_alphabet_char_and_single_spaces(x)
    print datetime.now() - start_first
    print "Testing regex with compiling"
    start_second = datetime.now()
    for i in range(1000000):
        result = keep_alphabet_char_and_single_spaces_compiled(x)
    print datetime.now() - start_second
    # using compiled regexes was consistently about 30% faster than the non-compiled regexes
