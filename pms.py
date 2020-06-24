#A python program to mimic the functionality of a real-world
#property management system(PMS), found in hotels and residential buildings
import time
import datetime
import csv
from csv import writer
import random


#Display main menu to the user
print("\n:::::Python Property Management System:::::\n")
time.sleep(1)
print("Main Menu:")
print("----------------\n")
print("Property Code: PGH620\n")
print("1. Search by Name\n" "2. Search by Confirmation #\n" "3. Search by Room #\n" "4. View In-House Guests\n" "5. View Departures\n" "6. Make a Reservation\n" "7. Cancel Reservation\n" "8. Log-off/Switch User\n")
time.sleep(1) #mimics loading of the system
menuSelect = input("Make a Selection: ")

if menuSelect == "1": #DONE
    nameEntry = input("Please enter Last name: ")
    #opens csv file containing guest records
    with open ('hotelguests.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        #searches for name entry, displays line
        for row in csv_reader:
            if row[0] == nameEntry:
                print(row)
                #ADD ELIF FOR "GUEST NOT FOUND"
        

elif menuSelect == "2": #DONE
    confEntry = input("Enter Confirmation Number: ")
    with open ('hotelguests.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for column in csv_reader:
            if column[5] == confEntry and confEntry.isdigit():
                print(column)
                #ADD ELIF FOR "GUEST NOT FOUND"

elif menuSelect == "3": #DONE
    roomEntry = input("Enter Room Number: ")
    with open ('hotelguests.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for column in csv_reader:
            if column[2] == roomEntry and roomEntry.isdigit():
                print(column)
                #ADD ELIF FOR "GUEST NOT FOUND"


elif menuSelect == "4": #DONE
    with open("hotelguests.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for lines in csv_reader:
            print(lines)

elif menuSelect == "5": #DONE
    depDate = input("Enter Departure Date: ")
    with open ('hotelguests.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for column in csv_reader:
            if column[4] == depDate:
                print(column)
                #ADD ELIF FOR NO DEPARTURES FOUND

elif menuSelect == "6": #DONE
    lastName = input("Enter a Last Name: ")
    firstName = input("Enter a First Name: ")
    roomNumber = input("Assign Room Number: ")
    arrivalDate = input("Enter an Arrival Date: ")
    departureDate = input("Enter a Departure Date: ")
    confNum = random.randint(150000,160000)
    enterRate = input("Enter Rate Amt: $")
    enterCC = input("Enter a valid Credit Card Number: ")
    enterEXP = input("Enter Expiration Date as mm/yy: ")
    with open('hotelguests.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([lastName, firstName, roomNumber, arrivalDate, departureDate, confNum, enterRate, enterCC, enterEXP])
    print("Uploading Reservation...\n")
    time.sleep(3)
    print("Reservation Uploaded with Confirmation # " + str(confNum))

elif menuSelect == "7": #DONE
    print("CXL MENU")
    print("---------")
    print("1. Cancel by Last Name \n")
    print("2. Cancel by Confirmation #\n")
    cancelSelect = input("Select an option: ")
    lines = list()
    if cancelSelect == "1":
        lastName = input("Enter last name: ")
        with open('hotelguests.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == lastName:
                        lines.remove(row)
        with open('hotelguests.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
            time.sleep(2)
            print("Reservation removed from PMS.")

    else: 
        confNumber = input("Enter confirmation number: ")
        if cancelSelect == "2":
            with open('hotelguests.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    lines.append(row)
                    for field in row:
                        if field == confNumber:
                            lines.remove(row)

        with open('hotelguests.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
            time.sleep(2)
            print("Reservation removed from PMS.")

elif menuSelect == 8:
    logoffAnsw = input("LOG OFF? Y/N?")
    if logoffAnsw == 'Y' or 'y':
        print("Logging Off...")
        time.sleep(3)
        print("Logged off at " + time)
    elif logoffAnsw == 'N' or 'n':
        print("Not finished")

