def full_name(first_name, *middle_name, last_name)
  name = "#{first_name} "
  middle_name.each { |m_name| name += "#{m_name} " }
  name += last_name
  name
end