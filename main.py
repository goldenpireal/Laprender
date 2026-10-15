import sessions
import time
import database

while True:
    print("1.Start a study session")
    print("0.Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print()
        print("Invalid Input")
        print()
        continue
    
    if choice == 1:

        duration_and_date = sessions.session_initiator()
        database.save_session(duration=duration_and_date[0], date=duration_and_date[1])

        seconds = duration_and_date[0]
        minutes = seconds // 60
        
        duration_hour = minutes // 60
        duration_min = minutes - (duration_hour)*60
        duration_sec = seconds - (minutes)*60
    
        duration = [duration_hour, duration_min, duration_sec]
    
        
        
        print()
        time.sleep(0.5)
        print("Your total study duration: ")
        print(duration[0],"h",duration[1],"m",duration[2],"s")
        print()
        print()
        time.sleep(1)
    elif choice == 0:
        print("Goodbye.. see yya later")
        break

    else:
        print()
        print("Invalid Input")
        print()

    
