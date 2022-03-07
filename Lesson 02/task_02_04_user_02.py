import datetime

d = datetime.datetime.strptime(input(), "%Y %m %d").date() + datetime.timedelta(int(input()))
print('{0.year} {0.month} {0.day}'.format(d))
