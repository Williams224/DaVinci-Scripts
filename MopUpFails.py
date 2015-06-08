nb = raw_input('Enter job number: ')
jnumber=int(nb)

for fails in jobs(jnumber).subjobs.select(status='failed'):
    if fails.info.submit_counter==1:
        fails.resubmit()
    elif fails.info.submit_counter==2:
        fails.backend.settings['CPUTime']=fails.backend.settings['CPUTime']*2
        fails.resubmit()
    elif fails.info.submit_counter==3:
        fails.backend.settings['BannedSites']=[fails.backend.actualCE]
        fails.resubmit()
    elif fails.info.submit_counter>3:
        print 'WARNING SUBMIT COUNTER > 3'
        
        
