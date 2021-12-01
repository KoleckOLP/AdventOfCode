data = File.readlines("../input.txt")

data_conv = []

data.each { |l| data_conv.append(l.to_i) }

result = 0
b = 0

data_conv.each do |a|
    if b == 0
        b = a
        next
    end

    if a > b
        result += 1
    end
    puts("#{a} > #{b}, #{result}")
    b = a
end

puts(result)
