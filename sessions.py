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
    date = time_end.date()

    timedelta = time_end - time_start

    duration = int(timedelta.total_seconds())


    print("Study session: ", time_start, "->", time_end)
    

    return duration, date



    


    
    





