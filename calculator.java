//A simple Java program with basic calculator functions
//Matthew J Schaefer
//June 2020

//create class Calculator
public class Calculator{
    //create constructor Calculator
    public Calculator(){
  
    }
    //create method for addition
    public int add(int a, int b){
      return a + b;
  
    }
    //create method for subtraction
    public int subtract(int a, int b){
      return a - b;
    }
    //create method for multiplication
    public int multiple(int a, int b){
      return a * b;
    }
    //create method for division
    public int divide(int a, int b){
      return a / b;
    }
    //create method for modulo/remainder
    public int modulo(int a, int b){
      return a % b;
    }   //In main function, print calculation results
        public static void main(String[] args){
        Calculator myCalculator = new Calculator();
        System.out.println(myCalculator.add(5, 7));
        System.out.println(myCalculator.subtract(45, 11));
  
  
    }
  
  }
  