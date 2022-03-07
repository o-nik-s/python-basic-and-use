from datetime import datetime, timedelta
print((datetime.strptime(input().strip(), "%Y %m %d") + timedelta(int(input().strip()))).strftime("%Y %-m %-d"))