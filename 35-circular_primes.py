'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?'''

import itertools

def is_prime(i):
    #print type(i)
    if i <= 1: return False
    if i == 2: return True
    for n in range(2,i):
        if i % n == 0: return False
    return True

def rotations_are_primes(num):
    anagrams = ["".join(perm) for perm in itertools.permutations(str(num))]
    for anagram in anagrams:
        if not is_prime(int(anagram)):
            return False
    return True

prime_list = []
count_circulars = 0

for i in range(1,1000000):
    if is_prime(i):
        if rotations_are_primes(i):
            print "\n" + str(i)
            count_circulars += 0

print count_circulars
