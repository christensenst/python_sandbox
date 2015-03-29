"""calculate a monthly payment based on principle, rate, and number of months
"""

import sys

def calculate_payment(principle, rate, months):
    return (principle * (rate/12)/(1 - pow(1 + rate/12,-months)))

if __name__ == '__main__':
    principle = int(sys.argv[1])
    rate = float(sys.argv[2])/100
    try:
        months = int(sys.argv[3])
    except IndexError:
        months = 48
    print calculate_payment(principle, rate, months)