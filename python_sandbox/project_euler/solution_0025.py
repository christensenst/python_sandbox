"""

"""

def fibonacci(a, b):
    count = 0
    while True:
        a, b = b, a + b
        count += 1
        if len(str(a)) >= 1000:
            return a, count
    


if __name__ == '__main__':
    a, b = 0, 1
    answer, term = fibonacci(a, b)
    print len(str(answer))
    print answer
    print term