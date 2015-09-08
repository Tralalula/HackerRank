__author__ = 'Tobias'

def time_conversion(time_to_convert, period):
    hour_colon = time_to_convert.find(":")
    hour = time_to_convert[:hour_colon]

    if period == "PM":
        hour = int(hour) + 12
        if hour == 24:
            hour = "12"
    elif hour == "12":
        hour = "00"

    return str(hour) + time_to_convert[hour_colon:]

time = raw_input()
time_len = len(time)

get_period = time[time_len - 2:time_len]
time = time[:time_len - 2]
print time_conversion(time, get_period)