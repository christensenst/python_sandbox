"""
Selection Sort:

First, find the smallest item in the array and exchange it with the first entry
Then, find the next smallest item and exchange it with the second entry.
Continue in this way until the entire array is sorted.  This is called selection
sort because you repeatedly select the smallest remaining item
"""

from test_data import ten_strings
from timer import total

def selection_sort(data):
    for x in range(len(data)):
        min = x
        for y in range(x + 1, len(data)):
            if data[y] < data[min]:
                min = y
        if x != min:
            exchange(data, x, min)


def exchange(data, x, min):
    temp = data[min]
    data[min] = data[x]
    data[x] = temp

if __name__ == '__main__':
    reps = 1000000
    results = total(reps, selection_sort, ten_strings)
    print "Selection sort took {} seconds for {} repetitions for a list of {} strings." \
        .format(str(results[0]), str(reps), str(len(ten_strings)))
    print "Compare to python's built-in sort method:"
    results = total(reps, sorted, ten_strings)
    print "Python's built-in 'sorted' method took {} seconds for {} repetitions for a list of {} strings." \
        .format(str(results[0]), str(reps), str(len(ten_strings)))