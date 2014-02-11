'''Take the number 192 and multiply it by each of 1, 2, and 3:
192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?'''

#time: 1.5 hour

def number_is_pandigital(concated_pandigital):
    no_repeat = True
    for c in concated_pandigital:
        if concated_pandigital.count(c) > 1:
            no_repeat = False

    return ('0' not in concated_pandigital) and (len(concated_pandigital) == 9) and no_repeat

big_pandigital = 0

for multiplicand in range(0,9999):
    product = 0
    multiplier = 0
    procced = True
    concated_pandigital = ""
    print multiplicand

    while procced:
        multiplier += 1
        product = multiplicand * multiplier
        concated_pandigital += str(product)
        if len(concated_pandigital) >= 9:
            procced = False
            if number_is_pandigital(concated_pandigital):
                if int(concated_pandigital) > big_pandigital:
                    big_pandigital = int(concated_pandigital)
                    print big_pandigital

print "big_pandigital => %d" % big_pandigital
