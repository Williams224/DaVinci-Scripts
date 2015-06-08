nb=raw_input('Enter Job Number')
number=int(nb)
for c in jobs(number).subjobs.select(status='completed'):
    i=c.id
    print 'getting subjob id:'
    print i
    if(c.outputfiles[0].lfn==''):
        print 'no output for job='
        print i
    else:
        c.outputfiles[0].get()
        
