data = File.readlines("../input.txt")

data_conv = []

data.each { |l| data_conv.append(l.to_i) }

result = 0
new_data = []
i = 0

data_conv.each_index do |i|
    if i+2 < data_conv.length
        new_data.append(data_conv[i] + data_conv[i+1] + data_conv[i+2])
    end
end

puts(new_data.inspect)

y = 0

new_data.each do |x|
    if y == 0
        y = x
        next
    end

    if x > y
        result += 1
    end
    puts("#{x} > #{y}, #{result}")
    y = x
end

puts(result)
