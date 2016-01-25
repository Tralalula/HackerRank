def sum_terms(n)
  (1..n).inject(0) { |product, n| product + n ** 2 + 1 }
end