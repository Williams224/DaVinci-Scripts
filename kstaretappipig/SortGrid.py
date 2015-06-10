import datetime as dt

finishtime=dt.datetime(2015,6,11,05,00)

while dt.datetime.now()<finishtime:
    MopUpFails(161)
    MopUpFails(162)
    MopUpFails(163)
    GetOutput(161)
    GetOutput(162)
    GetOutput(163)
    MopUpFails(165)
    MopUpFails(167)
    GetOutput(165)
    GetOutput(167)
              
