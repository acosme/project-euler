#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#2 hours

def special_pythagorean_triplet?(a,b,c)
    puts a + b + c
    return a + b + c == 1000
end

def a_square_plus_b_square_equal_c_square?(a,b,c)
    (a*a)+(b*b) == c*c
end

min_a_value = 3
max_a_value = 450

max_b_value = max_a_value + 1

max_c_value = max_b_value + 1

for a in min_a_value..max_a_value
    for b in (a+1)..max_b_value
        for c in (b+1)..max_c_value
            if a_square_plus_b_square_equal_c_square?(a,b,c)
                if special_pythagorean_triplet?(a,b,c)
                    puts "FOUND!!!!"
                    puts "#{a}-#{b}-#{c}"
                    system("sleep 3600")
                    puts "so it's #{a*b*c} !!!"
                end
            end
        end
    end
end

#a <= 332, b <= 333, c <= 334


