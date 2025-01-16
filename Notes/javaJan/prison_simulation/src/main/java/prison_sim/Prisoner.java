package prison_sim;

// Class representing a prisoner, inherits from Person class
public class Prisoner extends Person implements LocationAssignment {

    // prisoner specific attributes, use of enums
    private RiskLevel riskLevel;
    private CrimeType crime;
    private int sentenceLength;
    private String assignedLocation;

    // Constructor for prisoner
    public Prisoner(int id, String name, RiskLevel riskLevel, CrimeType crime, int sentenceLength) {
        super(id, name); // calls "Person" constructor
        this.riskLevel = riskLevel;
        this.crime = crime;
        this.sentenceLength = sentenceLength;
        this.assignedLocation = "Unassigned"; // default value
    }

    // Getters for the attributes/enums
    public RiskLevel getRiskLevel() {
        return riskLevel;
    }

    public CrimeType getCrime() {
        return crime;
    }

    public int getSentenceLenth() {
        return sentenceLength;
    }

    @Override
    public void assignToLocation(String location) {
        this.assignedLocation = location;
    }

    @Override 
    public String getAssignedLocation() {
        return assignedLocation;
    }

    // Override abstract method in "Person" base class to display prisoner details
    @Override
    public void displayInfo() {
        System.out.println("Prisoner ID: " + id + ", Name: " + name + ", Risk Level: " + riskLevel + ", Crime: " + crime + ", Length of Sentence: " + sentenceLength + " years" + ", Assigned Cell: " + assignedLocation);
    }

}

// The "Prisoner" class an imprisoned "Person" in the system
// It extends the "Person" class, adding attributes such as risk level, crime type, and sentence length.
// The class implements the "LocationAssignment" interface, allowing prisoners to be dynamically assigned to cells.
// This demonstrates inheritance, polymorphism, and interface implementation.
