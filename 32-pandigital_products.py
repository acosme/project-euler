'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.'''

#time: 2.5 hours

def elements_has_nine_digits(product, multiplicand, multiplier):
    return len(str(multiplicand) + str(product) + str(multiplier)) == 9

def elements_are_pandigital(product, multiplicand, multiplier):
    product = str(product)
    multiplicand = str(multiplicand)
    multiplier = str(multiplier)
    is_pandigital = True

    #print product
    for product_character in product:
        if (element_dont_included_in_others(product_character,product, multiplicand, multiplier)):
            continue
        else:
            is_pandigital = False

    if is_pandigital:
        for multiplicand_character in multiplicand:
            if (element_dont_included_in_others(multiplicand_character,multiplicand, product, multiplier)):
                continue
            else:
                is_pandigital = False

    if is_pandigital:
        for multiplier_character in multiplier:
            if (element_dont_included_in_others(multiplier_character,multiplier, multiplicand, product)):
                continue
            else:
                is_pandigital = False

    return is_pandigital

def element_dont_included_in_others(char,a, b, c):
    return ((not a.count(char) > 1) and (not char in b) and (not char in c))

def numbers_include_zero(product, multiplicand, multiplier):
    return ('0' in str(product) or '0' in str(multiplicand) or '0' in str(multiplier))

products_sum = 0
products_included = []

for multiplicand in range(0,9999):
    for multiplier in range(0,9999):
        product = multiplicand * multiplier
        if not product in products_included:
            if elements_has_nine_digits(product, multiplicand, multiplier) and not numbers_include_zero(product, multiplicand, multiplier):
                if elements_are_pandigital(product, multiplicand, multiplier):
                    print "summing %dx%d=%d\n" % (multiplicand, multiplier, product)
                    products_sum += product
                    products_included.append(product)
print products_sum
