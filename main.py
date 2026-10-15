import sessions
import time
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
        duration = sessions.session_initiator()
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

    
