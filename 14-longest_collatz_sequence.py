'''The following iterative sequence is defined for the set of positive integers:
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.'''

def is_odd(num):
    return num & 0x1

i = 1000000
big_chain_size = 0
big_num = 0

while i != 1:
    print str(i)
    num = i;
    chain_size = 0
    while num != 1:
        '''print ' ~ ' + str(num)'''
        if is_odd(num):
            num = num*3 + 1
        else:
            num = num/2
        chain_size += 1
    if big_chain_size < chain_size:
        big_chain_size = chain_size
        big_num = i
    i -= 1
    print '\n'

print big_num




