# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.

# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.

# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.

import datetime
dt_date = datetime.date(*list(map(int, input().strip().split())))
# dt_date = datetime.date(*list(map(int, "2016 12 20".strip().split())))
# print(dt_date)
dt_timedelta = datetime.timedelta(int(input()))
# dt_timedelta = datetime.timedelta(int(14))
# print(dt_timedelta)
print(*list(map(int, str(dt_date+dt_timedelta).split("-"))))
new_data = dt_date + dt_timedelta
print(new_data.year, new_data.month, new_data.day)
