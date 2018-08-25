# Time tricky count

start_hour = 3
start_minute = 48
length = 172

# how many full hours in length
hours = length // 60 
# how many minutes in length not included in the full hours
minutes = length % 60 
# add up minutes
end_minute = start_minute + minutes 
# check maybe we have additional full hour in minutes
addit_hour = end_minute // 60 

# have or not additional hour, now we get end minute
end_minute = end_minute % 60  
# add up all full hours
end_hour = start_hour + hours + addit_hour 

#Our result:

print(str(end_hour) + ":" + str(end_minute))

# We can do the same by another way:
#hours = length // 60
#minutes = length - hours * 60
#end_hour = (start_hour + hours)
#end_minute = (start_minute + minutes)
#if(end_minute > 59):
#    end_minute -= 60
#    end_hour += 1

#end_hour = str(end_hour)
#end_minute = str(end_minute)

#print(end_hour + ":" + end_minute)
