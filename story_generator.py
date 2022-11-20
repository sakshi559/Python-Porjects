import random

When=['A few years ago','Yesterday' ,'Last night','Long time ago','On that day','On halloween']
who=['a ghost' ,' a tiger' ,'my friend','a Psychopath','a book worm', 'a nerd' , 'a gang']
name=['weird' ,'john','don\'t know','drunk','sick']
residence=['in street', 'in India', 'in park' ,'in river', 'in bridge']
went=['walking','school','stalking','following me','beating people']
wyd=['hanging','murdering','staring','running with knife','controlling','drinking']
happened=['was killed','got pranked','enjoy scaring us','found dead','tied us']

story=(random.choice(When)+", "+random.choice(name)+" ,"+random.choice(who)+" was "+random.choice(residence)+ ", " +random.choice(went)+" and " +random.choice(wyd)+", " +random.choice(happened))

print(story)