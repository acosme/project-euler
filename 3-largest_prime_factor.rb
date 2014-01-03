#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#time: 40 minutes

num = 600851475143
factors = {}
while num != 1
    (2..num).each {|i|
        if num % i == 0
            print "!"
            factors.merge!({num => i})
            num = num / i
            break
        else
            print "."
        end
    }
end

puts "\n"
puts factors
