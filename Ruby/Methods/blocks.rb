def factorial
  yield
end

n = gets.to_i
factorial do
  puts (2..n).to_a.inject { |product, n| product * n }
end