//Java Program to mimic the actions of a Droid, and the current level of energy remaining after those actions take place.

//create class Droid
public class Droid{
  //initialize battery level and droid name
  int batteryLevel;
  String name;
  //set up return statement for droid name using toString Method
  public String toString() {
    return "Hello, I am the droid: " + name;
  }
  //setup instance for Droid with name parameter, as String
  public Droid(String droidName){
    name = droidName;
    batteryLevel = 100;
  }
  //create instance for performing tasks
  public void performTask(String task){
    //set up print statement for a more precise explination
    System.out.println(name + " is performing: " + task);
    //reduces battery level when task is performed. 
    batteryLevel = batteryLevel - 15;
  }
  //Sets up energyReport after tasks are completed
  public void energyReport(){
    System.out.println("Battery Level After Tasks: " + batteryLevel);
  }
  //creates instance for transferring energy to other drones, when more than one drone is created.
  public void energyTransfer(int energyToTrans) {
    int newEnergyLvl = batteryLevel + energyToTrans;
    batteryLevel = newEnergyLvl;

  }
  //In Main, call performTasks & energyReport using print statements.
  public static void main(String[] args) {
    Droid codey = new Droid("Codey");
    System.out.println(codey);
    codey.energyTransfer(10);
    System.out.println("Current Battery Level: " + codey.batteryLevel);
    
    codey.performTask("Job Searching");
    codey.performTask("Coding");
    codey.performTask("Taking over the world");
    codey.performTask("Human Extinction");
    codey.performTask("Making Lunch");
    codey.energyReport();
    //if battery level of codey is below 30, print line prompting to recharge Droid.
    if (codey.batteryLevel < 30) {
      System.out.println("Recharge Droid Soon");
    }
  }
}
