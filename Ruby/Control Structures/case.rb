def identify_class(obj)
  # write your case control structure here
  case
    when obj.class.to_s == 'Hacker' then
      puts 'It\'s a Hacker!'
    when obj.class.to_s == 'Submission' then
      puts 'It\'s a Submission!'
    when obj.class.to_s == 'TestCase' then
      puts 'It\'s a TestCase!'
    when obj.class.to_s == 'Contest' then
      puts 'It\'s a Contest!'
    else
      puts 'It\'s an unknown model'
  end
end