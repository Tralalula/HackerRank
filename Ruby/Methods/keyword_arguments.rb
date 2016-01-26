def convert_temp(temp, input_scale: 'celsius', output_scale: 'celsius')
  if input_scale == 'celsius' and output_scale=='fahrenheit'
    temp = temp * 1.8 + 32
  elsif input_scale == 'celsius' and output_scale=='kelvin'
    temp += 273
  elsif input_scale=='fahrenheit' and output_scale=='celsius'
    temp = (temp - 32) / 1.8
  elsif input_scale=='fahrenheit' and output_scale=='kelvin'
    temp = (temp + 459.67) * 5.0 / 9
  elsif input_scale=='kelvin' and output_scale=='celsius'
    temp -= 273.15
  elsif input_scale=='kelvin' and output_scale=='fahrenheit'
    temp = temp * 9.0 / 5 - 459.67
  end
  temp
end