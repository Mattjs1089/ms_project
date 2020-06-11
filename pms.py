#A python program to mimic the selections of a real-world
#property management system(pms), found in hotels and residential buildings
import time
import csv
from csv import writer
import random

#print("ASCII ART")
print("\n:::::Python Property Management System:::::\n")
time.sleep(1)
print("Main Menu:")
print("----------------\n")
print("Property Code: PGH620\n")
print("1. Search by Name\n" "2. Search by Confirmation #\n" "3. Search by Room #\n" "4. View In-House Guests\n" "5. View Depatures\n" "6. Make a Reservation\n" "7. Cancel Reservation\n")
time.sleep(1)
menuSelect = input("Make a Selection: ")

if menuSelect == "1":
    nameEntry = input("Please enter Last name: ")
    with open ('hotelguests.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for column in csv_reader:
            if column[0] == nameEntry:
                print(column)
        else:
            if column[0] != nameEntry:
                print("No Guest Found")

elif menuSelect == "2":
    confEntry = input("Enter Confirmation Number: ")
    with open ('hotelguests.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for column in csv_reader:
            if column[0] == confEntry and confEntry.isdigit():
                print(row)
        else:
            print("No Confirmation Number Exists.")

elif menuSelect == "3":
    roomEntry = input("Enter Room Number: ")
    with open ('hotelguests.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for column in csv_reader:
            if column[0] == roomEntry and roomEntry.isdigit():
                print(row)
            else:
                if not column[0]:
                    print("No Guest Found")


elif menuSelect == "4":
    with open("hotelguests.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for lines in csv_reader:
            print(lines)

elif menuSelect == "5":
    with open("hotelguests.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for lines in csv_reader:
            print(lines[0])
            #currently shows last names all guests
            #needs to show departures ONLY for today's date

elif menuSelect == "6":
    lastName = input("Enter a Last Name: ")
    firstName = input("Enter a First Name: ")
    roomNumber = input("Assign Room Number: ")
    arrivalDate = input("Enter an Arrival Date: ")
    departureDate = input("Enter a Departure Date: ")
    confNum = random.randint(23000,30000)
    enterRate = input("Enter Rate Amt: $")
    enterCC = input("Enter a valid Credit Card Number: ")
    enterEXP = input("Enter Expiration Date as mm/yy: ")
    with open('hotelguests.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([lastName, firstName, roomNumber, arrivalDate, departureDate, confNum, enterRate, enterCC, enterEXP])
    print("Uploading Reservation...\n")
    time.sleep(3)
    print("Reservation Uploaded with Confirmation # " + str(confNum))

elif menuSelect == "7":
    print("CXL MENU")
    print("---------")
    print("1. Cancel by Last Name \n")
    print("2. Cancel by Confirmation #\n")
    cancelSelect = input("Select an option: ")

else:
    logoffAnsw = print("LOG OFF? Y/N?")
    if logoffAnsw == 'Y' or 'y':
        print("Logging Off...")
        time.sleep(3)
        print("Logged off at " + time)


    