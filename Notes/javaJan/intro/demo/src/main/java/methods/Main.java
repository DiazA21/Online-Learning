package methods;

public class Main {

    public static void main(String[] args) {
      

    }

}

/* method - function - perform a task or return a value - like in python
must be in body of a class
signiture - 

 */
 /* Main a = new Main();

System.out.println(a.add(5,5));        

}
public static int add(int a, int b){
    return a + b;
}
 */

 /* 
// method overloading - achieved by changing number, type or order of parameters
 * Main c = new Main();
        c.greet("Andrew"); // calls first method
        c.greet(); // calls second method

    }

        public void greet(String name) {
            System.out.println("Hello " + name);
        }

        public void greet() {
            greet("Andrew");
        }
 */

 /* Scanner -
    We must make an object of the scanner class
    import for utils.scanners
    
    next() - reads a single word
    nextline() - reads a whole line (strings)
    nextint() - reads an integer
    nextDouble() - reads a decimal number

    public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your name:");
        String name = scanner.nextLine();

        
        System.out.println("Hello " + name);

        
import java.util.Scanner;

Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your age");
        int age = scanner.nextInt();

        System.out.println("Enter your height");
        double height = scanner.nextDouble();

        scanner.nextLine();

        System.out.println("Enter your name");
        String name = scanner.nextLine();

        System.out.println("Hello " + name + " age is " + age + " height is" + height);
        scanner.close();
   
 */

 /* formatting

  * // %d numbers
        // %s strings
        // %f float
        // %b boolean

        System.out.printf("integer: %d%nString: %s%nfloat: %f%n", 10, "hello-world", 3.11455);
    
     // formatted string

        String name = "Andrew";
        int age = 10;
        double x = 25.24;

        String formattedString = String.format("Hello %s, your age is %d, also %.1f", name, age, x);
        System.out.println(formattedString);

    
  */

