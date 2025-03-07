from Utils import DateUtils as DT
import datetime as dt

du = DT.DateUtils()

time = (dt.datetime.now().time()).strftime("%H:%M:%S")

x = du.Time_to_TimeAsLong(time)

print(x)