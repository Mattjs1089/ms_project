//Java program that will print the largest city within the given continent, according to value provided in the continent variable. 

public class Continents {
	public static void main(String[] args) {
    //set variable and value
    int continent = 6;
    //commence switch statement, case 1-7
    switch (continent) {
      case 1:
        System.out.println("North America: Mexico City, Mexico");
        break;
      case 2:
        System.out.println("South America: Sao Paulo, Brazil");
        break;
      case 3:
        System.out.println("Europe: Moscow, Russia");
        break;
      case 4:
        System.out.println("Africa: Lagos, Nigeria");
        break;
      case 5:
        System.out.println("Asia: Shanghai, China");
        break;
      case 6:
        System.out.println("Australia: Sydney, Australia");
        break;
      case 7:
        System.out.println("Antartica: McMurdo Station, US");
        break;
      default:
      //if 1-7 not provided, print Undefined. 
        System.out.println("Undefined continent!");
        break;

    }

	}
}