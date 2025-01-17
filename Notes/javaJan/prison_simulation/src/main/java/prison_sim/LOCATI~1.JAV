package prison_sim;

public interface LocationAssignment {
    void assignToLocation(String location); // String in case of alphanumeric assignment
    String getAssignedLocation();
}

// The "LocationAssignment" interface defines a contract for any class that needs the capability to be assigned to a location within the prison system.
// It demonstrates flexibility and scalability by allowing unrelated classes (e.g., "Prisoner", "Visitor") to share common behavior without relying on inheritance.
