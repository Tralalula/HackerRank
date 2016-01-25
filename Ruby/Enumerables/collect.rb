def rot13(secret_messages)
  secret_messages.map do |element|
    element.tr('a-z', 'n-za-m')
  end
end