#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.



#time: 30 minutes

def is_palindrome?(number)
    number.to_s == number.to_s.reverse
end

palindromes = []

(100..999).each {|n1|
    (100..999).each {|n2|
        if is_palindrome?(n1 * n2)
            print "!"
            palindromes.push(n1 * n2) 
        else
            print "."
        end
    }
}

puts "\n"
puts palindromes.max


