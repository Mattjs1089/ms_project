//A Java program to calculate the monthly payment of a newly purchased vehicle. 
//MJS

//creat class CarLoan
public class CarLoan {
	public static void main(String[] args) {
    //initialize variables for purchase details
    int carLoan = 10000;
    int loanLength = 3;
    int interestRate = 2;
    int downPayment = 2500;
    //sets conditional for non-realistic instance
    if (loanLength <= 0 || interestRate <= 0){
      System.out.println("Error! You must take our a valid car loan");
      //Lets user know if car can be paid in full
    } else if (downPayment >= carLoan) {
      System.out.println("The car can be paid in full.");
      //if previous conditions not met, calculate car loan. 
    } else {
      //set variables for final purchase details
      int remainingBalance = carLoan - downPayment;
      int months = loanLength * 12;
      int monthlyBalance = remainingBalance / months;
      int interest = (monthlyBalance * interestRate) / 100;
      int monthlyPayment = monthlyBalance + interest;
      //print monthly payment of vehicle
      System.out.println(monthlyPayment);

    }

	

	}
}