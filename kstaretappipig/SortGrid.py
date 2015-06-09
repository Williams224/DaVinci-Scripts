import datetime as dt

finishtime=dt.datetime(2015,6,10,05,00)

while dt.datetime.now()<finishtime:
    MopUpFails(161)
    MopUpFails(162)
    MopUpFails(163)
    GetOutput(161)
    GetOutput(162)
    GetOutput(163)
    MopUpFails(158)
    MopUpFails(159)
    GetOutput(158)
    GetOutput(159)
