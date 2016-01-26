def prime?(x)
  return false if x <= 1
  Math.sqrt(x).to_i.downto(2).each { |i| return false if x % i == 0 }
  true
end