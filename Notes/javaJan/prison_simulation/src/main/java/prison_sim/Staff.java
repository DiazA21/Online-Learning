package prison_sim;

public class Staff extends Person {

    // staff specific attributes / enum
    private Role role;
    private int accessLevel;


    // constructor for staff
    public Staff(int id, String name, Role role, int accessLevel) {
        super(id,name); // calls "Person" constructor
        this.role = role;
        this.accessLevel = accessLevel;
    }

    // Getters for Staff class
    public Role getRole() {
        return role;
    }

    public int getAccessLevel() {
        return accessLevel;
    }

    // Override abstract method in "Person" base class to display staff details
    @Override
    public void displayInfo() {
        System.out.println("Staff ID: " + id + ", Name: " + name + ", Job Role: " + role + ", Access Level: " + accessLevel);
    }

}

// The "Staff" class represents employees working in the prison system.
// It extends the "Person" class, adding attributes such as role and access level.
// This class demonstrates inheritance and polymorphism by providing customised implementations of shared behavior.
