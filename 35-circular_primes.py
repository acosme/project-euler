'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?'''

import itertools

def is_prime(i):
    if i <= 1: return False
    if i == 2: return True
    for n in range(2,i):
        if i % n == 0:
            return False
    return True

def rotations_are_primes(num):

    if not all_numbers_between_permitted(num): return False

    rotations = []
    rotation = str(num)
    for i in range(1,len(str(num)) + 1):
        rotation = rotation[1:] + rotation[0]
        if not int(rotation) in rotations: rotations.insert(0,int(rotation))
        if not is_prime(int(rotation)):
            return False

    circular_primes.extend(rotations)
    return True




def all_numbers_between_permitted(num):
    if not len(str(num)) >= 2: return True
    for char in str(num):
        if not int(char) in [1,3,7,9]: return False
    return True

circular_primes = []
count_circular = 0

for i in range(0,1000000):
#for i in range(0,10000):
#for i in range(0,100):
    if is_prime(i):
        print i
        if not i in circular_primes and rotations_are_primes(i):
            count_circular += 1
            print "\n->"
            print circular_primes

print circular_primes
print "total => %d" % len(circular_primes)
print "count first circulars => %d" % count_circular
