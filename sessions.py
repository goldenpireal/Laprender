from datetime import datetime
import time
 
def session_initiator():

    time_start = datetime.now().replace(microsecond=0)
    

    print("Loading up AI Agent. Please wait..")
    print()
    print("To end the session press 0")

    while True:
        try:
            end_choice = int(input())
            if end_choice == 0:
                print("Thank You for learning with us..")
                break
        except:
            print("Invalid Input")

    time_end = datetime.now().replace(microsecond=0)

    timedelta = time_end - time_start

    seconds = int(timedelta.total_seconds())
    minutes = seconds // 60

    duration_hour = minutes // 60
    duration_min = minutes - (duration_hour)*60
    duration_sec = seconds - (minutes)*60

    duration = [duration_hour, duration_min, duration_sec]

    print("Study session: ", time_start, "->", time_end)
    

    return duration



    


    
    





