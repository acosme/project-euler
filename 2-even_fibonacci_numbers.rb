#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def generic_function_refactored(n)
    sum = 0
    return 1 if n <= 2
    ultimos = [1,1]
    (n-2).times do 
        ultimos.reverse!
        ultimos[1] = ultimos[0] + ultimos[1]
        puts "#{ultimos[0]} - #{ultimos[1]}"
        sum += ultimos[0]
    end

    puts "result"
    puts sum
end

generic_function_refactored(4000000)
