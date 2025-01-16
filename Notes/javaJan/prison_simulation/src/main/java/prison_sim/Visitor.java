package prison_sim;

public class Visitor implements LocationAssignment {
    private String visitorName;
    private String assignedLocation;

    public Visitor(String visitorName) {
        this.visitorName = visitorName;
        this.assignedLocation = "Unassigned"; // default value
    }

    @Override
    public void assignToLocation(String location) {
        this.assignedLocation = location;
    }

    @Override
    public String getAssignedLocation() {
        return assignedLocation;
    }

    public void displayInfo() {
        System.out.println("Visitor Name: " + visitorName + ", Assigned Room: " + assignedLocation);
    }
}



// The "Visitor" class represents individuals visiting the prison who are not part of the main "Person" hierarchy.
// By implementing the "LocationAssignment" interface, visitors can be associated with specific locations (e.g., rooms or areas) in the prison.
// This demonstrates how interfaces provide flexible behavior sharing across unrelated classes.
