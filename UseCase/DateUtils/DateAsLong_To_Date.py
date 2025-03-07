from Utils import DateUtils as DT
import datetime as dt

du = DT.DateUtils()

data = dt.datetime.now()
dataaslong = du.Date_to_DateAsLong(data)

x = du.DateAsLong_to_Date(dataaslong)

print(x)