import datetime as dt

for j in jobs(207).subjobs.select(status="submitted"):
    j.force_status('failed')
    j.resubmit()

for j in jobs(208).subjobs.select(status="submitted"):
    j.force_status('failed')
    j.resubmit()

for j in jobs(211).subjobs.select(status="submitted"):
    j.force_status('failed')
    j.resubmit()
    
    

    

finishtime=dt.datetime(2015,7,19,05,00)

while dt.datetime.now()<finishtime:
    MopUpFails(207)
    MopUpFails(208)
    MopUpFails(211)
    MopUpFails(214)
    MopUpFails(215)
    MopUpFails(216)
    MopUpFails(217)
    MopUpFails(218)
    MopUpFails(219)
    MopUpFails(220)
    MopUpFails(221)
    MopUpFails(222)
    MopUpFails(223)
    MopUpFails(224)
    MopUpFails(225)
    MopUpFails(226)
    MopUpFails(227)
    MopUpFails(228)
    MopUpFails(229)
    MopUpFails(230)
    MopUpFails(231)
    MopUpFails(232)
    MopUpFails(233)
    MopUpFails(234)
    MopUpFails(235)
    MopUpFails(236)
    MopUpFails(237)
    GetOutput(207)
    GetOutput(208)
    GetOutput(211)
    GetOutput(214)
    GetOutput(215)
    GetOutput(216)
    GetOutput(217)
    GetOutput(218)
    GetOutput(219)
    GetOutput(220)
    GetOutput(221)
    GetOutput(222)
    GetOutput(223)
    GetOutput(224)
    GetOutput(225)
    GetOutput(226)
    GetOutput(227)
    GetOutput(228)
    GetOutput(229)
    GetOutput(230)
    GetOutput(231)
    GetOutput(232)
    GetOutput(233)
    GetOutput(234)
    GetOutput(235)
    GetOutput(236)
    GetOutput(237)
        
        
            
            



