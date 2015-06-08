i=0
for subs in jobs(26).subjobs.select(status != 'completed'):
    i+=1
print i
    
