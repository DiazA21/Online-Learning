package prison_sim;

import java.util.ArrayList;
import java.util.List;

public class Prison {
    private List<Person> people; // Gives a list of all people in the Prison

    public Prison() {
        this.people = new ArrayList<>();
    }

    public void addPerson(Person person) {
        people.add(person);
    }

    public void displayAllPeople() {
        for (Person person : people) {
            person.displayInfo(); 
        }
    }

}

// The "Prison" class manages a collection of "Person" objects, including prisoners and staff.
// It demonstrates composition by maintaining a list of "Person" instances and uses polymorphism to handle diverse objects dynamically.
// This class acts as a central hub for managing and displaying information about the prison population.
