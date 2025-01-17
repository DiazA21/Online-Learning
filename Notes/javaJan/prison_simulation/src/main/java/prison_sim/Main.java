package prison_sim;

public class Main {
    public static void main(String[] args) {
        Prison prison = new Prison();

        Prisoner prisoner1 = new Prisoner(1, "Andrew Diaz", RiskLevel.MEDIUM, CrimeType.THEFT, 15);
        Prisoner prisoner2 = new Prisoner(2, "John Doe", RiskLevel.MEDIUM, CrimeType.FRAUD, 20);
        Prisoner prisoner3 = new Prisoner(3, "Jack Frost", RiskLevel.HIGH, CrimeType.ARSON, 25);

        prisoner1.assignToLocation("B101");
        prisoner2.assignToLocation("B201");
        prisoner3.assignToLocation("C05");

        prison.addPerson(prisoner1);
        prison.addPerson(prisoner2);
        prison.addPerson(prisoner3);

        Staff staff1 = new Staff(101, "Lisa Ramirez", Role.ADMIN, 2);
        Staff staff2 = new Staff(102, "Charles Darwin", Role.WARDEN, 5);
       
        prison.addPerson(staff1);
        prison.addPerson(staff2);

        Visitor visitor1 = new Visitor("Jane Doe");
        visitor1.assignToLocation("Visitor Room 1");

        System.out.println("Prison Population: ");
        prison.displayAllPeople();

    }
}

// The "Main" class serves as the entry point for the program, demonstrating the interaction of all components.
// It showcases object-oriented principles such as inheritance, polymorphism, abstraction, and interface usage.
// The program dynamically creates and manages "Prisoner", "Staff", and "Visitor" instances, highlighting their relationships within the prison system.

