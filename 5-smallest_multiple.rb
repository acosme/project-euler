#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


not_a_number_divisible_by_all = true
num = 

while not_a_number_divisible_by_all do
    num += 2
    print num
    (3..20).each do |i|
        if num % i == 0
            print "  ."
            if i == 20
                not_a_number_divisible_by_all = false
            end
        else
            break
        end
    end
    puts "\n"
end

puts num
