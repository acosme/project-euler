#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

# 3 hours

def not_10001_prime(prime_count)
    prime_count != 10001
end

def is_prime?(i)
    return false if i <= 1
    return true if i == 2
    (2...i).each {|n| 
        if i % n == 0 
            return false 
            #print "~"
        end
    }
    #print " ><>"
    true
end

count = 0
prime_count = 0
while not_10001_prime(prime_count) do
   count += 1
   if is_prime?(count)
       puts prime_count
       prime_count += 1
   end
end

puts count




