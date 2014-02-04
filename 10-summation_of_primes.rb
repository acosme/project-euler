#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.


def is_prime?(i)
    return false if i <= 1
    return true if i == 2
    (2...i).each {|n|
        if i % n == 0
            return false
        end
    }
    true
end

count = 0
sum_primes = 0
while count < 2000000 do
   count += 1
   if is_prime?(count)
       puts "summing #{count}"
       sum_primes += count
   end
end

puts sum_primes

