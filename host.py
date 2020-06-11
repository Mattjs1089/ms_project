
#Program Introduction
#A fictional program used to obtain information/modify statuses of hosts
#from the WestWorld series on HBO


print("DELOS INCORPORATED HOST MOFIFICATION SYSTEM:")
print("Security Clearance, Level A Required.")
print("⚠️ UNAUTHORIZED ACCESS PROHIBITED, AND PUNISHABLE BY DEADLY FORCE")
print("To request access, contact your Systems Admininistrator")
print("\n")

passKey = 0
#sets password, prompts user for login credentials
while passKey == passKey:
    passKey = input("Enter Credentials: ")
    if passKey == 'password':
        print("Host Selection Menu")
        print("__________________________")
        print("Abernathy, Dolores: 52522")
        print("Millay, Maeve: 52523")
        print("Penny, Clementine: 52524")
        print("Lowe, Bernard 52525")
        print("Hale, Charlotte: 52526")
        print("Ford, Robert 52527")
        print("Stubbs, Ashley: 52528")
        print("Hughes, Elsie: 52529")
        print("Delos, Logan: 52530")
        print("Sizemore, Lee: 52530")
        print("Flood, Teddy: 52531")
        print("Lutz, Felix: 52532")
        print("Cullen, Theresa: 52533")
        print("Doe, Armastice: 52534")
        print("Escaton, Hector: 52535")
        print("Strand, Karl: 52536")
        print("Grace, Emily: 52537")
        print("Nichol, Caleb: 52538")
        print("__________________________")
        print("Please enter HID to access host file...")
        print("\n \n")
        break
    elif passKey != 'password':
        print("Invalid Credentials. Please contact your Administrator")
        continue

 #function for host descriptions and status      
def host(ID_number, name, skin_tone, eye_color, hair_color, height, weight, gender, iq_level, status):
    print("Host ID:" + ID_number + " " + name)
    print("Skin Tone: " + skin_tone)
    print("Eye Color: " + eye_color)
    print("Hair Color: " + hair_color)
    print("Height: " + height)
    print("Weight: " + weight)
    print("Gender: " + gender)
    print("IQ Level: " + iq_level)
    print("Current Status: " + status)
    print("\n")

id_selection = 0
#selection from main menu - user must enter a 5 digit ID# respective to each host
while id_selection == id_selection:
    id_selection = input("Enter HID: ")

    if id_selection == "52522":
        host(str(52522), "Abernathy, Dolores", "White", "Blue", "Blonde", "5'7", "145lbs", "Female", "230", "Missing")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            #Menu for changing host's status
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                print("!!!WARNING: HOST IS NOT ACCESSIBLE.")
                print("!!! ERROR CODE RED: OUT OF RANGE!!!")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                print("!!!WARNING: HOST IS NOT ACCESSIBLE.")
                print("!!! ERROR CODE RED: OUT OF RANGE!!!")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                print("!!!WARNING: HOST IS NOT ACCESSIBLE.")
                print("!!! ERROR CODE RED: OUT OF RANGE!!!")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                print("!!!WARNING: HOST IS NOT ACCESSIBLE.")
                print("!!! ERROR CODE RED: OUT OF RANGE!!!")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                print("!!!WARNING: HOST IS NOT ACCESSIBLE.")
                print("!!! ERROR CODE RED: OUT OF RANGE!!!")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                print("!!!WARNING: HOST IS NOT ACCESSIBLE.")
                print("!!! ERROR CODE RED: OUT OF RANGE!!!")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52523":
        host(str(52523), "Millay, Maeve", "White", "Hazel", "Black", "5'10", "141lbs", "Female", "250", "Inactive")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52523), "Millay, Maeve", "White", "Hazel", "Black", "5'10", "141lbs", "Female", "250", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52523), "Millay, Maeve", "White", "Hazel", "Black", "5'10", "141lbs", "Female", "250", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52523), "Millay, Maeve", "White", "Hazel", "Black", "5'10", "141lbs", "Female", "250", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52523), "Millay, Maeve", "White", "Hazel", "Black", "5'10", "141lbs", "Female", "250", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52523), "Millay, Maeve", "White", "Hazel", "Black", "5'10", "141lbs", "Female", "250", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52523), "Millay, Maeve", "White", "Hazel", "Black", "5'10", "141lbs", "Female", "250", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52524":
        host(str(52524), "Penny, Clementine", "White", "Blonde", "", "5'8", "145lbs", "Female", "187", "Inactive")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52524), "Penny, Clementine", "White", "Blonde", "", "5'8", "145lbs", "Female", "187", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52524), "Penny, Clementine", "White", "Blonde", "", "5'8", "145lbs", "Female", "187", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52524), "Penny, Clementine", "White", "Blonde", "", "5'8", "145lbs", "Female", "187", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52524), "Penny, Clementine", "White", "Blonde", "", "5'8", "145lbs", "Female", "187", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52524), "Penny, Clementine", "White", "Blonde", "", "5'8", "145lbs", "Female", "187", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52524), "Penny, Clementine", "White", "Blonde", "", "5'8", "145lbs", "Female", "187", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52525":
        host(str(52525), "Lowe, Bernard", "Black", "Brown", "Black", "5'8", "214lbs", "Male", "220", "Active: WestWorld")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52525), "Lowe, Bernard", "Black", "Brown", "Black", "5'8", "214lbs", "Male", "220", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52525), "Lowe, Bernard", "Black", "Brown", "Black", "5'8", "214lbs", "Male", "220", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52525), "Lowe, Bernard", "Black", "Brown", "Black", "5'8", "214lbs", "Male", "220", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52525), "Lowe, Bernard", "Black", "Brown", "Black", "5'8", "214lbs", "Male", "220", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52525), "Lowe, Bernard", "Black", "Brown", "Black", "5'8", "214lbs", "Male", "220", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52525), "Lowe, Bernard", "Black", "Brown", "Black", "5'8", "214lbs", "Male", "220", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52526":
        host(str(52526), "Charlotte Hale", "White", "Green", "Blonde", "5'8", "132lbs", "Female", "220", "Deprecated")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52526), "Charlotte Hale", "White", "Green", "Blonde", "5'8", "132lbs", "Female", "220", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52526), "Charlotte Hale", "White", "Green", "Blonde", "5'8", "132lbs", "Female", "220", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52525), "Lowe, Bernard", "Black", "Brown", "Black", "5'8", "214lbs", "Male", "220", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52526), "Charlotte Hale", "White", "Green", "Blonde", "5'8", "132lbs", "Female", "220", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52526), "Charlotte Hale", "White", "Green", "Blonde", "5'8", "132lbs", "Female", "220", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52526), "Charlotte Hale", "White", "Green", "Blonde", "5'8", "132lbs", "Female", "220", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52527":
        host(str(52527), "Ford, Robert", "White", "Blue", "Brown", "5'8", "176lbs", "Male", "187", "In Development")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52527), "Ford, Robert", "White", "Blue", "Brown", "5'8", "176lbs", "Male", "187", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52527), "Ford, Robert", "White", "Blue", "Brown", "5'8", "176lbs", "Male", "187", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52527), "Ford, Robert", "White", "Blue", "Brown", "5'8", "176lbs", "Male", "187", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52527), "Ford, Robert", "White", "Blue", "Brown", "5'8", "176lbs", "Male", "187", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52527), "Ford, Robert", "White", "Blue", "Brown", "5'8", "176lbs", "Male", "187", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52527), "Ford, Robert", "White", "Blue", "Brown", "5'8", "176lbs", "Male", "187", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52528":
        host(str(52528), "Stubbs, Ashley", "White", "Hazel", "Black", "5'8", "137lbs", "Male", "210", "Motor Functions Frozen")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52528), "Stubbs, Ashley", "White", "Hazel", "Black", "5'8", "137lbs", "Male", "210", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52528), "Stubbs, Ashley", "White", "Hazel", "Black", "5'8", "137lbs", "Male", "210", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52528), "Stubbs, Ashley", "White", "Hazel", "Black", "5'8", "137lbs", "Male", "210", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52528), "Stubbs, Ashley", "White", "Hazel", "Black", "5'8", "137lbs", "Male", "210", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52528), "Stubbs, Ashley", "White", "Hazel", "Black", "5'8", "137lbs", "Male", "210", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52528), "Stubbs, Ashley", "White", "Hazel", "Black", "5'8", "137lbs", "Male", "210", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52529":
        host(str(52529), "Hughes, Elsie", "White", "Brown", "Blonde", "5'8", "141lbs", "Female", "130", "Unaffiliated/Missing")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52529), "Hughes, Elsie", "White", "Brown", "Blonde", "5'8", "141lbs", "Female", "130", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52529), "Hughes, Elsie", "White", "Brown", "Blonde", "5'8", "141lbs", "Female", "130", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52529), "Hughes, Elsie", "White", "Brown", "Blonde", "5'8", "141lbs", "Female", "130", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52529), "Hughes, Elsie", "White", "Brown", "Blonde", "5'8", "141lbs", "Female", "130", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52529), "Hughes, Elsie", "White", "Brown", "Blonde", "5'8", "141lbs", "Female", "130", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52529), "Hughes, Elsie", "White", "Brown", "Blonde", "5'8", "141lbs", "Female", "130", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52530":
        host(str(52530), "Delos, Logan", "White", "Blue", "Brown", "5'8", "176lbs", "Male", "250", "In Development/Inactive")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52530), "Delos, Logan", "White", "Blue", "Brown", "5'8", "176lbs", "Male", "250", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52530), "Delos, Logan", "White", "Blue", "Brown", "5'8", "176lbs", "Male", "250", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52530), "Delos, Logan", "White", "Blue", "Brown", "5'8", "176lbs", "Male", "250", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52530), "Delos, Logan", "White", "Blue", "Brown", "5'8", "176lbs", "Male", "250", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52530), "Delos, Logan", "White", "Blue", "Brown", "5'8", "176lbs", "Male", "250", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52530), "Delos, Logan", "White", "Blue", "Brown", "5'8", "176lbs", "Male", "250", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52531":
        host(str(52531), "Sizemore, Lee", "White", "Blue", "Brown", "5'8", "142lbs", "Male", "250", "Inactive")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52531), "Sizemore, Lee", "White", "Blue", "Brown", "5'8", "142lbs", "Male", "250", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52531), "Sizemore, Lee", "White", "Blue", "Brown", "5'8", "142lbs", "Male", "250", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52531), "Sizemore, Lee", "White", "Blue", "Brown", "5'8", "142lbs", "Male", "250", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52531), "Sizemore, Lee", "White", "Blue", "Brown", "5'8", "142lbs", "Male", "250", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52531), "Sizemore, Lee", "White", "Blue", "Brown", "5'8", "142lbs", "Male", "250", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
            host(str(52531), "Sizemore, Lee", "White", "Blue", "Brown", "5'8", "142lbs", "Male", "250", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52532":
        host(str(52532), "Flood, Teddy", "White", "Hazel", "Black", "5'8", "141lbs", "Male", "210", "Missing")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52532), "Flood, Teddy", "White", "Hazel", "Black", "5'8", "141lbs", "Male", "210", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52532), "Flood, Teddy", "White", "Hazel", "Black", "5'8", "141lbs", "Male", "210", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52532), "Flood, Teddy", "White", "Hazel", "Black", "5'8", "141lbs", "Male", "210", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52532), "Flood, Teddy", "White", "Hazel", "Black", "5'8", "141lbs", "Male", "210", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52532), "Flood, Teddy", "White", "Hazel", "Black", "5'8", "141lbs", "Male", "210", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
            host(str(52532), "Flood, Teddy", "White", "Hazel", "Black", "5'8", "141lbs", "Male", "210", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52533":
        host(str(52533), "Lutz, Felix", "Asian", "Brown", "Black", "5'10", "165lbs", "Male", "124", "Unaffiliated")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52533), "Lutz, Felix", "Asian", "Brown", "Black", "5'10", "165lbs", "Male", "124", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52533), "Lutz, Felix", "Asian", "Brown", "Black", "5'10", "165lbs", "Male", "124", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52533), "Lutz, Felix", "Asian", "Brown", "Black", "5'10", "165lbs", "Male", "124", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52533), "Lutz, Felix", "Asian", "Brown", "Black", "5'10", "165lbs", "Male", "124", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52533), "Lutz, Felix", "Asian", "Brown", "Black", "5'10", "165lbs", "Male", "124", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
            host(str(52533), "Lutz, Felix", "Asian", "Brown", "Black", "5'10", "165lbs", "Male", "124", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52534":
        host(str(52534), "Cullen, Theresa", "White", "Brown", "Black", "5'8", "121lbs", "Female", "125", "Unaffiliated")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52534), "Cullen, Theresa", "White", "Brown", "Black", "5'8", "121lbs", "Female", "125", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52534), "Cullen, Theresa", "White", "Brown", "Black", "5'8", "121lbs", "Female", "125", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52534), "Cullen, Theresa", "White", "Brown", "Black", "5'8", "121lbs", "Female", "125", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52534), "Cullen, Theresa", "White", "Brown", "Black", "5'8", "121lbs", "Female", "125", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52534), "Cullen, Theresa", "White", "Brown", "Black", "5'8", "121lbs", "Female", "125", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
            host(str(52534), "Cullen, Theresa", "White", "Brown", "Black", "5'8", "121lbs", "Female", "125", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52535":
        host(str(52535), "Doe, Armistice", "White", "Brown", "Blonde", "5'8", "165lbs", "Female", "205", "Missing")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52535), "Doe, Armistice", "White", "Brown", "Blonde", "5'8", "165lbs", "Female", "205", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52535), "Doe, Armistice", "White", "Brown", "Blonde", "5'8", "165lbs", "Female", "205", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52535), "Doe, Armistice", "White", "Brown", "Blonde", "5'8", "165lbs", "Female", "205", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52535), "Doe, Armistice", "White", "Brown", "Blonde", "5'8", "165lbs", "Female", "205", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52535), "Doe, Armistice", "White", "Brown", "Blonde", "5'8", "165lbs", "Female", "205", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52535), "Doe, Armistice", "White", "Brown", "Blonde", "5'8", "165lbs", "Female", "205", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52536":
        host(str(52536), "Escaton, Hector", "Latino", "Brown", "Black", "5'8", "189lbs", "Male", "200", "Active: SpyWorld")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52536), "Escaton, Hector", "Latino", "Brown", "Black", "5'8", "189lbs", "Male", "200", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52536), "Escaton, Hector", "Latino", "Brown", "Black", "5'8", "189lbs", "Male", "200", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52536), "Escaton, Hector", "Latino", "Brown", "Black", "5'8", "189lbs", "Male", "200", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52536), "Escaton, Hector", "Latino", "Brown", "Black", "5'8", "189lbs", "Male", "200", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52536), "Escaton, Hector", "Latino", "Brown", "Black", "5'8", "189lbs", "Male", "200", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52536), "Escaton, Hector", "Latino", "Brown", "Black", "5'8", "189lbs", "Male", "200", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52537":
        host(str(52537), "Strand, Karl", "White", "Green", "Browne", "5'8", "173lbs", "Male", "801", "In Development")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52537), "Strand, Karl", "White", "Green", "Browne", "5'8", "173lbs", "Male", "801", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52537), "Strand, Karl", "White", "Green", "Browne", "5'8", "173lbs", "Male", "801", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52537), "Strand, Karl", "White", "Green", "Browne", "5'8", "173lbs", "Male", "801", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52537), "Strand, Karl", "White", "Green", "Browne", "5'8", "173lbs", "Male", "801", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52537), "Strand, Karl", "White", "Green", "Browne", "5'8", "173lbs", "Male", "801", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52537), "Strand, Karl", "White", "Green", "Browne", "5'8", "173lbs", "Male", "801", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52538":
        host(str(52538), "Grace, Emily", "White", "Blue", "Browne", "5'8", "121lbs", "Female", "801", "In Development")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52538), "Grace, Emily", "White", "Blue", "Browne", "5'8", "121lbs", "Female", "801", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52538), "Grace, Emily", "White", "Blue", "Browne", "5'8", "121lbs", "Female", "801", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52538), "Grace, Emily", "White", "Blue", "Browne", "5'8", "121lbs", "Female", "801", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52538), "Grace, Emily", "White", "Blue", "Browne", "5'8", "121lbs", "Female", "801", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52538), "Grace, Emily", "White", "Blue", "Browne", "5'8", "121lbs", "Female", "801", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52538), "Grace, Emily", "White", "Blue", "Browne", "5'8", "121lbs", "Female", "801", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection == "52539":
        host(str(52539), "Nichol, Caleb", "White", "Brown", "Red/Blonde", "5'8", "175lbs", "Male", "450", "In Development")
        print("Make a Selection:")
        print("_________________")
        print("\n")
        print("1. Change Host Status")
        print("2. Exit")
        print("\n")
        menu_select = 0
        menu_select = input("Make a Selection: ")
        if menu_select == '1':
            print("Select New Host Status")
            print("______________________")
            print("\n")
            print("1. Active")
            print("2. Inactive")
            print("3. Missing")
            print("4. In Development")
            print("5. Software Update")
            print("6. Freeze All Motor Functions")
            status_select = 0
            status_select = input("Change Status: Make a Selection: ")
            if status_select == '1':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52539), "Nichol, Caleb", "White", "Brown", "Red/Blonde", "5'8", "175lbs", "Male", "450", "Active")
            elif status_select == '2':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52539), "Nichol, Caleb", "White", "Brown", "Red/Blonde", "5'8", "175lbs", "Male", "450", "Inactive")
            elif status_select == '3':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52539), "Nichol, Caleb", "White", "Brown", "Red/Blonde", "5'8", "175lbs", "Male", "450", "Missing")
            elif status_select == '4':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52539), "Nichol, Caleb", "White", "Brown", "Red/Blonde", "5'8", "175lbs", "Male", "450", "In Development")
            elif status_select == '5':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52539), "Nichol, Caleb", "White", "Brown", "Red/Blonde", "5'8", "175lbs", "Male", "450", "Software Update")
            elif status_select == '6':
                print("Updated Host Status: ")
                print("_____________________")
                print("\n")
                host(str(52539), "Nichol, Caleb", "White", "Brown", "Red/Blonde", "5'8", "175lbs", "Male", "450", "Motor Functions Frozen")
        elif menu_select == '2':
            print("Logging Off...") 
            print("Logged Off")
            break
    elif id_selection != 5:
        print("Invalid HID. Please Try Again")
        print("\n")
        continue




