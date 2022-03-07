import datetime

date,delta = datetime.date(*[int(i) for i in input().split()]), datetime.timedelta(int(input()))

print((date+delta).year,(date+delta).month,(date+delta).day)
