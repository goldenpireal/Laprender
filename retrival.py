import sqlite3

def retrive_info():

    while True:
        print()
        print("Year(Press Enter for all years)")

        try:
            year = int(input())
        except ValueError:
            print("Invalid Input")
            continue

        if year < 1:
            print("Invalid input")

        else:
            break
    

    while True:
        print("Month(Press Enter for all months):")

        try:
            month = int(input())
        except ValueError:
            print("Invalid Input")
            continue

        if month < 1 or month > 12:
            print("Invalid Input")

        else:
            break


    while True:
        print("Date(Press Enter for all dates):")

        try:
            date = int(input())
        except ValueError:
            print("Invalid Input")
            continue

        def is_date_valid(month, date):

            if month < 8:
                if month % 2 != 0 and month != 2 :
                    if date > 31 or date < 1 :
                        print("Invalid Input")
                        return False
                    else:
                        return True
                    
                elif month % 2 == 0 and month != 8 and month != 2:
                    if date > 30 or date < 1:
                        print("Invalid Input") 
                        return False
                    else:
                        return True

                elif month == 2:
                    if date > 28 or date < 1:
                        print("Invalid Input")
                        return False
                    else:
                        return True

                else:
                    return True

            else:
                if month % 2 == 0 and month != 2 :
                    if date > 31 or date < 1 :
                        print("Invalid Input")
                        return False
                    else:
                        return True
                    
                elif month % 2 != 0 and month != 8 and month != 2:
                    if date > 30 or date < 1 :
                        print("Invalid Input") 
                        return False
                    else:
                        return True

                else:
                    return True

            

        if year % 4 != 0:
            temp1 = is_date_valid(month, date)
            if temp1 == True:
                break

        else:
            
            if month != 2:
                temp2 = is_date_valid(month, date)
                if temp2 == True:
                    break

            else:
                if date > 29 or date < 1 :
                    print("Invalid Input")
                else:
                    break
                
    return date, month, year


    

def retrive():

    dates = retrive_info()
    formated_date = str(dates[2])+"-"+str(dates[1])+"-"+str(dates[0])

    print("sessions on: ",formated_date)

    conn = sqlite3.connect("laprender.db")
    c = conn.cursor()
    result = c.execute("""SELECT * FROM sessions WHERE date=?""",
                       (formated_date,))
    print(result.fetchall())
    conn.close() 


