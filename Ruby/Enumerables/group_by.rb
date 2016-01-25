def group_by_marks(marks, n)
  result = {}
  grouped_marks = marks.group_by { |key, value| value > n }
  unless grouped_marks[false].nil?
    result['Failed'] = grouped_marks[false]
  end
  unless grouped_marks[true].nil?
    result['Passed'] = grouped_marks[true]
  end
  result
end