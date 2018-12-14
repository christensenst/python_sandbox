from __future__ import print_function
LARGEST_VALUE = 1000


def main():
    sequence_length = 0
    for d in range(LARGEST_VALUE, 1, -1):
        if sequence_length >= d:
            return d + 1
        found_remainers = [0 for a in range(d)]
        value = 1
        position = 0
        while found_remainers[value] == 0 and value != 0:
            found_remainers[value] = position
            value *= 10
            value %= d
            position += 1
        if position - found_remainers[value] > sequence_length:
            sequence_length = position - found_remainers[value]


if __name__ == '__main__':
    result = main()
    print(result)
