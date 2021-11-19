data = File.readlines("../input.txt")

data_strip = []

data.each { |l| data_strip.append(l.strip) }

data_split = []

data_strip.each { |l|
    data_split.append(l.chars.each_slice(7).map(&:join))
}

row = []

data_split.each do |l|
    i = 0
    range = []

    while i < 128 do
        range.append(i)
        i += 1
    end

    l[0].chars.each do |c|  # this should be looping 7 chars
        foption, boption = range.each_slice( (range.size/2.0).round ).to_a
        if c == "F"
            range = foption
        else
            range = boption
        end
    end
    row.append(range)
end

column = []

data_split.each do |l|
    i = 0
    range = []

    while i < 8 do
        range.append(i)
        i += 1
    end

    l[1].chars.each do |c|  # this should be looping 3 chars
        loption, roption = range.each_slice( (range.size/2.0).round ).to_a
        if c == "L"
            range = loption
        else
            range = roption
        end
    end
    column.append(range)
end

final = []

888.times do |i|
    final.append(row[i][0].to_i * 8 + column[i][0].to_i)
end

puts(final.max)
