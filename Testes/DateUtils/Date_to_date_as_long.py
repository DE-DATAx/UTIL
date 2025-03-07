from Utils import DateUtils as DT
import datetime as dt

du = DT.DateUtils()

data = dt.datetime.now()

x = du.Date_to_DateAsLong(data)

print(x)