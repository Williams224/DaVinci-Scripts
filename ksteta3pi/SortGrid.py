import datetime as dt
import time

finishtime=dt.datetime(2015,7,27,6,00)

while dt.datetime.now()<finishtime:
    MopUpFails(266)
    MopUpFails(259)
    MopUpFails(269)
    MopUpFails(280)
    MopUpFails(281)
    MopUpFails(282)
    MopUpFails(283)
    MopUpFails(284)
    MopUpFails(285)
    for i in range(286,330):
        MopUpFails(i)
    for i in range(259,330):
        GetOutput(i)

