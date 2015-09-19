from datetime import datetime

def library_fine(actual_date, expected_date):
    if actual_date <= expected_date:
        return 0
    elif actual_date.month == expected_date.month and actual_date.year == expected_date.year:
        return 15 *  abs((expected_date - actual_date).days)
    elif actual_date.year == expected_date.year:
        return 500 * abs(expected_date.month - actual_date.month)
    return 10000

actual_return_date = datetime.strptime(raw_input(), "%d %m %Y")
expected_return_date = datetime.strptime(raw_input(), "%d %m %Y")

fine = library_fine(actual_return_date, expected_return_date)
print fine