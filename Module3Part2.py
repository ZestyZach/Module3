#ask user for the time in hours 1-24
current_time = int(input("Enter current time in hours (0-23)\n"))
if (current_time <= 23) and (current_time >= 0): 
    #if a valid time is entered ask user for how long to set the alarm for
    timer_time = int(input("How long should the timer be?\n")) 
    # (current_time + timer_time) % 24 gives us the hour the timer shoudl go off
    future_time = (current_time + timer_time) % 24
    #output what time the alarm will go off
    print("The alarm will go off at {}".format(future_time))
else:
    # only 0 through 23 are valid inputs
    print("Please use a number between 0 and 23.")
input("Press Enter to exit.")
