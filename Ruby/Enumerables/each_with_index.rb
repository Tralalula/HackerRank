def skip_animals(animals, skip)
  result = []
  animals[skip..-1].each_with_index { |element, index| result << "#{index + skip}:#{element}" }
  result
end