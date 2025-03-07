from Utils import DateUtils as DT
import datetime as dt
from datetime import timedelta

du = DT.DateUtils()

time = (dt.datetime.now().time()).strftime("%H:%M:%S")

x = timedelta(du.Time_to_TimeAsLong(time))

y = du.TimeAsLong_to_Time(x)

print(y)