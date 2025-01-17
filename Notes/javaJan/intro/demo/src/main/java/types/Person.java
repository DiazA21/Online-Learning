package types;

public class Person {
// Fields (state of the object - discussed later)

    String name;
    int age;
    // Methods (behavior of the object)

    public void introduce() {
        System.out.println("Hi, my name is " + name + " and I am " + age + " years old.");
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }



    
}
