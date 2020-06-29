//A C++ program to mimic the functionality of a real-world
//property management system(PMS), commonly found in hotels and residential buildings

#include <iostream>



//Display main menu to the user

int main() {
    std::cout << ":::::+Plus Property Management System:::::\n";

    std::cout <<"\nMain Menu:";
    std::cout <<"------------------\n";
    std::cout <<"Property Code: JGH620\n";
    std::cout <<" 1. Search by Name\n 2. Search by Confirmation\n 3. Search by Room\n 4. View In-House Guests\n 5. View Departures\n 6. Make a Reservation\n 7. Cancel a Reservation\n 8. Log-off/Switch User\n";

    int menuSelect = 0;
    std::cout << "Make a Selection: ";
    std::cin >> menuSelect;

    if (menuSelect == 1) {
        char lastName;
        std::cout << "Enter Last Name: ";
        std::cin >> lastName;
    } else if (menuSelect == 2) {
        int confEntry;
        std::cout << "Enter Confirmation Number: ";
        std::cin >> confEntry;
    } else if (menuSelect == 3) {
        int roomNum;
        std::cout << "Enter Room Number: ";
        std::cin >> roomNum;
    } else if (menuSelect == 4) {
        std::cout << "Loading In-House Guests...";
    } else if (menuSelect == 5) {
        int departDate;
        std::cout << "Enter Departure Date(mmddyy): ";
        std::cin >> departDate;
    } else if (menuSelect == 6) {
        std::cout << "Loading Reservation System...";
    } else if (menuSelect == 7) {
        std::cout << "1. Cancel by Last Name\n";
        std::cout << "2. Cancel by Confirmation Number\n";
        int cxlMenuSelect = 0;
        std::cout << "Make a Selection: ";
        std::cin >> cxlMenuSelect;
        if (cxlMenuSelect == 1) {
            char cxlLastName;
            std::cout << "Enter a Last Name: ";
            std::cin >> cxlLastName;
        } else {
            int cxlConf;
            std::cout << "Enter Confirmation Number: ";
            std::cin >> cxlConf;
        }

    } else if (menuSelect == 8) {
        char userAnswer;
        std::cout << "LOG OFF? Y/N?: ";
        std::cin >> userAnswer;
        if (userAnswer == 'Y' || userAnswer == 'y') {
            std::cout << "User Logged Off\n";
        }
        
        
        
    }
}



