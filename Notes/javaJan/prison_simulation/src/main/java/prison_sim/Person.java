package prison_sim;

// base class "Person", provides foundation for entities that are "people" in this sim and allows for future additions such as "Visitor"
public abstract class Person { 
    protected int id; // Shared attribute for a person's ID
    protected String name; // Shared attribute for a person's name

    // constructor to initialise name and id
    public Person(int id, String name) {
        this.id = id; // Assign the given id to the instance variable
        this.name = name; // Assign the given name to the instance variable
    }

    // Getter for id
    public int getID() {
        return id;
    }

    // Getter for name
    public String getName() {
        return name;
    }

    // Abstract method to enforce subclasses to implement their own display logic
    public abstract void displayInfo();

}

// The "Person" abstract class serves as the foundation for all person-related entities in the prison system.
// It encapsulates shared attributes (id, name) and requires subclasses to implement their own "displayInfo" method.
// This design ensures code reuse and consistency with the use of inheritance and abstraction.
