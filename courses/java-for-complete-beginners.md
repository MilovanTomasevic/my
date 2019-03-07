---
layout: page
title: Java for Complete Beginners
description: >
  This free java tutorial for complete beginners will help you learn the java programming language from scratch. Start coding in no time with this course!
hide_description: true

---

     
## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## A Hello World Program

```java
public class Application {
 
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
 
}
```
Application.java
{:.figure}

## Using Variables

```java
public class Application {
 
    public static void main(String[] args) {
        int myNumber = 88;
        short myShort = 847;
        long myLong = 9797;
         
        double myDouble = 7.3243;
        float myFloat = 324.3f;
         
        char myChar = 'y';
        boolean myBoolean = false;
         
        byte myByte = 127;
         
         
        System.out.println(myNumber);
        System.out.println(myShort);
        System.out.println(myLong);
        System.out.println(myDouble);
        System.out.println(myFloat);
        System.out.println(myChar);
        System.out.println(myBoolean);
        System.out.println(myByte);
    }
 
}
```
Application.java
{:.figure}

## Strings - Working With Text

```java
public class Application {
    public static void main(String[] args) {
         
        int myInt = 7;
         
        String text = "Hello";
         
        String blank = " ";
         
        String name = "Bob";
         
        String greeting = text + blank + name;
         
        System.out.println(greeting);
         
        System.out.println("Hello" + " " + "Bob");
         
        System.out.println("My integer is: " + myInt);
         
        double myDouble = 7.8;
         
        System.out.println("My number is: " + myDouble + ".");
    }
}
```
Application.java
{:.figure}

## While Loops

```java
public class Application {
    public static void main(String[] args) {
         
        int value = 0;
     
        while(value < 10)
        {
            System.out.println("Hello " + value);
             
            value = value + 1;
        }
    }
}
```
Application.java
{:.figure}

## For Loops

```java
public class Application {
    public static void main(String[] args) {
         
        for(int i=0; i < 5; i++) {
            System.out.printf("The value of i is: %d\n", i);
        }
    }
}
```
Application.java
{:.figure}

## if

```java
public class Application {
	public static void main(String[] args) {
		
		// Some useful conditions:
		System.out.println(5 == 5);
		System.out.println(10 != 11);
		System.out.println(3 < 6);
		System.out.println(10 > 100);
		
		// Using loops with "break": 
		int loop = 0;
		
		while(true) {
			System.out.println("Looping: " + loop);
			
			if(loop == 3) {
				break;
			}
			
			loop++;
		
			System.out.println("Running");
		}
	}
}
```
Application.java
{:.figure}

## Getting User Input

```java
import java.util.Scanner;
 
public class Application {
    public static void main(String[] args) {
         
        // Create scanner object
        Scanner input = new Scanner(System.in);
         
        // Output the prompt
        System.out.println("Enter a floating point value: ");
         
        // Wait for the user to enter something.
        double value = input.nextDouble();
         
        // Tell them what they entered.
        System.out.println("You entered: " + value);
    }
}
```
Application.java
{:.figure}

## Do While

```java
import java.util.Scanner;
 
 
public class Application {
 
    public static void main(String[] args) {
 
         
        Scanner scanner = new Scanner(System.in);
         
        /*
        System.out.println("Enter a number: ");
        int value = scanner.nextInt();
         
        while(value != 5) {
            System.out.println("Enter a number: ");
            value = scanner.nextInt();
        }
        */
         
        int value = 0;
        do {
            System.out.println("Enter a number: ");
            value = scanner.nextInt();
        }
        while(value != 5);
         
        System.out.println("Got 5!");
    }
 
}
```
Application.java
{:.figure}

## Switch

```java
import java.util.Scanner;
 
public class Application {
 
    
	public static void main(String[] args) {
 
        Scanner input = new Scanner(System.in);
 
        System.out.println("Please enter a command: ");
        String text = input.nextLine();
 
        switch (text) {
        case "start":
            System.out.println("Machine started!");
            break;
 
        case "stop":
            System.out.println("Machine stopped.");
            break;
 
        default:
            System.out.println("Command not recognized");
        }
         
         
    }
 
}
```
Application.java
{:.figure}

## Arrays

```java
public class Application {
    public static void main(String[] args) {
         
        int value = 7;
         
        int[] values;
        values = new int[3];
         
        System.out.println(values[0]);
         
        values[0] = 10;
        values[1] = 20;
        values[2] = 30;
         
        System.out.println(values[0]);
        System.out.println(values[1]);
        System.out.println(values[2]);
         
        for(int i=0; i < values.length; i++) {
            System.out.println(values[i]);
        }
         
        int[] numbers = {5, 6, 7};
         
        for(int i=0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }
    }
     
}
```
Application.java
{:.figure}

## Arrays of Strings

```java
public class Application {
 
    public static void main(String[] args) {
         
        // Declare array of (references to) strings.
        String[] words = new String[3];
         
        // Set the array elements (point the references
        // at strings)
        words[0] = "Hello";
        words[1] = "to";
        words[2] = "you";
         
        // Access an array element and print it.
        System.out.println(words[2]);
         
        // Simultaneously declare and initialize an array of strings
        String[] fruits = {"apple", "banana", "pear", "kiwi"};
         
        // Iterate through an array
        for(String fruit: fruits) {
            System.out.println(fruit);
        }
         
        // "Default" value for an integer
        int value = 0;
         
        // Default value for a reference is "null"
        String text = null;
         
        System.out.println(text);
         
        // Declare an array of strings
        String[] texts = new String[2];
         
        // The references to strings in the array
        // are initialized to null.
        System.out.println(texts[0]);
         
        // ... But of course we can set them to actual strings.
        texts[0] = "one";
    }
 
}
```
Application.java
{:.figure}

## Multi-Dimensional Arrays

```java
public class Application {
 
    public static void main(String[] args) {
         
        // 1D array
        int[] values = {3, 5, 2343};
         
        // Only need 1 index to access values.
        System.out.println(values[2]);
         
        // 2D array (grid or table)
        int[][] grid = {
            {3, 5, 2343},
            {2, 4},
            {1, 2, 3, 4}
        };
         
        // Need 2 indices to access values
        System.out.println(grid[1][1]);
        System.out.println(grid[0][2]);
         
        // Can also create without initializing.
        String[][] texts = new String[2][3];
         
        texts[0][1] = "Hello there";
         
        System.out.println(texts[0][1]);
         
        // How to iterate through 2D arrays.
        // first iterate through rows, then for each row
        // go through the columns.
        for(int row=0; row < grid.length; row++) {
            for(int col=0; col < grid[row].length; col++) {
                System.out.print(grid[row][col] + "\t");
            }
             
            System.out.println();
        }
         
        // The last array index is optional.
        String[][] words = new String[2][];
         
        // Each sub-array is null.
        System.out.println(words[0]);
         
        // We can create the subarrays 'manually'.
        words[0] = new String[3];
         
        // Can set a values in the sub-array we
        // just created.
        words[0][1] = "hi there";
         
        System.out.println(words[0][1]);
    }
 
}
```
Application.java
{:.figure}

## Classes and Objects

```java
class Person {
     
    // Instance variables (data or "state")
    String name;
    int age;
     
     
    // Classes can contain
     
    // 1. Data
    // 2. Subroutines (methods)
}
 
 
public class Application {
 
    public static void main(String[] args) {
         
         
        // Create a Person object using the Person class
        Person person1 = new Person();  
        person1.name = "Joe Bloggs";
        person1.age = 37;
         
        // Create a second Person object
        Person person2 = new Person();
        person2.name = "Sarah Smith";
        person2.age = 20;
         
        System.out.println(person1.name);
         
    }
 
}
```
Application.java
{:.figure}

## Methods

```java
class Person {
 
    // Instance variables (data or "state")
    String name;
    int age;
 
    // Classes can contain
 
    // 1. Data
    // 2. Subroutines (methods)
     
    void speak() {
        for(int i=0; i<3; i++) {
            System.out.println("My name is: " + name + " and I am " + age + " years old ");
        }
    }
     
    void sayHello() {
        System.out.println("Hello there!");
    }
}
 
public class Application {
 
    public static void main(String[] args) {
 
        // Create a Person object using the Person class
        Person person1 = new Person();
        person1.name = "Joe Bloggs";
        person1.age = 37;
        person1.speak();
        person1.sayHello();
 
        // Create a second Person object
        Person person2 = new Person();
        person2.name = "Sarah Smith";
        person2.age = 20;
        person2.speak();
        person1.sayHello();
 
        System.out.println(person1.name);
 
    }
 
}
```
Application.java
{:.figure}

## Getters and Return Values

```java
class Person {
    String name;
    int age;
     
    void speak() {
        System.out.println("My name is: " + name);
    }
     
    int calculateYearsToRetirement() {
        int yearsLeft = 65 - age;
         
        return yearsLeft;
    }
     
    int getAge() {
        return age;
    }
     
    String getName() {
        return name;
    }
}
 
 
public class Application {
 
    public static void main(String[] args) {
        Person person1 = new Person();
         
        person1.name = "Joe";
        person1.age = 25;
         
        // person1.speak();
         
        int years = person1.calculateYearsToRetirement();
         
        System.out.println("Years till retirements " + years);
         
        int age = person1.getAge();
        String name = person1.getName();
         
        System.out.println("Name is: " + name);
        System.out.println("Age is: " + age);
    }
 
}
```
Application.java
{:.figure}

## Method Parameters

```java
class Frog {
    private String name;
    private int age;
     
    public void setName(String name) {
        this.name = name;
    }
     
    public void setAge(int age) {
        this.age = age;
    }
     
    public String getName() {
        return name;
    }
     
    public int getAge() {
        return age;
    }
     
    public void setInfo(String name, int age) {
        setName(name);
        setAge(age);
    }
}
 
public class Application {
 
    public static void main(String[] args) {
     
        Frog frog1 = new Frog();
         
        //frog1.name = "Bertie";
        //frog1.age = 1;
         
        frog1.setName("Bertie");
        frog1.setAge(1);
         
        System.out.println(frog1.getName());
    }
 
}
```
Application.java
{:.figure}

## Constructors

```java
class Machine {
    private String name;
    private int code;
     
    public Machine() {
        this("Arnie", 0);
         
        System.out.println("Constructor running!");
    }
     
    public Machine(String name) {
        this(name, 0);
         
        System.out.println("Second constructor running");
        // No longer need following line, since we're using the other constructor above.
        //this.name = name;
    }
     
    public Machine(String name, int code) {
         
        System.out.println("Third constructor running");
        this.name = name;
        this.code = code;
    }
}
 
public class Application {
    public static void main(String[] args) {
        Machine machine1 = new Machine();
 
        Machine machine2 = new Machine("Bertie");
         
        Machine machine3 = new Machine("Chalky", 7);
    }
 
}
```
Application.java
{:.figure}

## Static (and Final)

```java
class Thing {
    public final static int LUCKY_NUMBER = 7;
     
    public String name;
    public static String description;
     
    public static int count = 0;
     
    public int id;
     
    public Thing() {
         
        id = count;
         
        count++;
    }
     
    public void showName() {
        System.out.println("Object id: " + id + ", " + description + ": " + name);
    }
     
    public static void showInfo() {
        System.out.println(description);
        // Won't work: System.out.println(name);
    }
}
 
 
public class Application {
 
    public static void main(String[] args) {
         
        Thing.description = "I am a thing";
         
        Thing.showInfo();
         
        System.out.println("Before creating objects, count is: " + Thing.count);
         
        Thing thing1 = new Thing();
        Thing thing2 = new Thing();
         
        System.out.println("After creating objects, count is: " + Thing.count);
         
        thing1.name = "Bob";
        thing2.name = "Sue";
         
        thing1.showName();
        thing2.showName();
         
        System.out.println(Math.PI);
         
        System.out.println(Thing.LUCKY_NUMBER);
    }
 
}
```
Application.java
{:.figure}

## StringBuilder and String Formatting

```java
public class Application {
 
 
    public static void main(String[] args) {
         
        // Inefficient
        String info = "";
         
        info += "My name is Bob.";
        info += " ";
        info += "I am a builder.";
         
        System.out.println(info);
         
        // More efficient.
        StringBuilder sb = new StringBuilder("");
         
        sb.append("My name is Sue.");
        sb.append(" ");
        sb.append("I am a lion tamer.");
         
        System.out.println(sb.toString());
         
        // The same as above, but nicer ....
         
        StringBuilder s = new StringBuilder();
         
        s.append("My name is Roger.")
        .append(" ")
        .append("I am a skydiver.");
         
        System.out.println(s.toString());
         
        ///// Formatting //////////////////////////////////
         
        // Outputting newlines and tabs
        System.out.print("Here is some text.\tThat was a tab.\nThat was a newline.");
        System.out.println(" More text.");
         
        // Formatting integers
        // %-10d means: output an integer in a space ten characters wide,
        // padding with space and left-aligning (%10d would right-align)
        System.out.printf("Total cost %-10d; quantity is %d\n", 5, 120);
         
        // Demo-ing integer and string formatting control sequences
        for(int i=0; i<20; i++) {
            System.out.printf("%-2d: %s\n", i, "here is some text");
        }
         
        // Formatting floating point value
         
        // Two decimal place:
        System.out.printf("Total value: %.2f\n", 5.6874);
         
        // One decimal place, left-aligned in 6-character field:
        System.out.printf("Total value: %-6.1f\n", 343.23423);
         
        // You can also use the String.format() method if you want to retrieve
        // a formatted string.
        String formatted = String.format("This is a floating-point value: %.3f", 5.12345);
        System.out.println(formatted);
         
        // Use double %% for outputting a % sign.
        System.out.printf("Giving it %d%% is physically impossible.", 100);
    }
 
}
```
Application.java
{:.figure}

## The toString Method

```java
class Frog {
     
    private int id;
    private String name;
     
    public Frog(int id, String name) {
        this.id = id;
        this.name = name;
    }
     
    public String toString() {
         
        return String.format("%-4d: %s", id, name);
         
        /*
        StringBuilder sb = new StringBuilder();
        sb.append(id).append(": ").append(name);
         
        return sb.toString();
        */
    }
}
 
public class Application {
 
    public static void main(String[] args) {
        Frog frog1 = new Frog(7, "Freddy");
        Frog frog2 = new Frog(5, "Roger");
         
        System.out.println(frog1);
        System.out.println(frog2);
    }
}
```
Application.java
{:.figure}

## Inheritance

```java
public class Machine {
     
    protected String name = "Machine Type 1";
     
    public void start() {
        System.out.println("Machine started.");
    }
     
    public void stop() {
        System.out.println("Machine stopped.");
    }
}
```
Machine.java
{:.figure}

```java
public class Car extends Machine {
     
     
    @Override
    public void start() {
        System.out.println("Car started");
    }
 
    public void wipeWindShield() {
        System.out.println("Wiping windshield");
    }
     
    public void showInfo() {
        System.out.println("Car name: " + name);
    }
}
```
Car.java
{:.figure}

```java
public class Application {
 
    public static void main(String[] args) {
        Machine mach1 = new Machine();
         
        mach1.start();
        mach1.stop();
         
        Car car1 = new Car();
         
        car1.start();
        car1.wipeWindShield();
        car1.showInfo();
        car1.stop();
         
         
    }
 
}
```
Application.java
{:.figure}

## Packages

```java
package com.caveofprogramming.oceangame;

public class Aquarium {

}
```
com/caveofprogramming/oceangame/Aquarium.java
{:.figure}

```java
package ocean.plants;

public class Algae {

}
```
ocean/plants/Algae.java
{:.figure}

```java
package ocean.plants;

public class Seaweed {

}
```
ocean/plants/Seaweed.java
{:.figure}

```java
package ocean;

public class Fish {

}
```
ocean/Fish.java
{:.figure}

```java
import ocean.Fish;
import ocean.plants.Seaweed;
 
public class Application {
 
     
    public static void main(String[] args) {
        Fish fish = new Fish();
        Seaweed weed = new Seaweed();
    }
 
}
```
Application.java
{:.figure}

## Interfaces

```java
public interface Info {
    public void showInfo();
}
```
Info.java
{:.figure}

```java
public interface IStartable {
    public void start();
    public void stop();
}
```
IStartable.java
{:.figure}

```java
public class Machine implements IStartable {
     
    private int id = 7;
     
    public void start() {
        System.out.println("Machine started.");
    }
 
    public void showInfo() {
        System.out.println("Machine ID is: " + id);
    }
}
```
Machine.java
{:.figure}

```java
public class Person implements Info {
     
    private String name;
     
    public Person(String name) {
        this.name = name;
    }
 
    public void greet() {
        System.out.println("Hello there.");
    }
 
    @Override
    public void showInfo() {
        System.out.println("Person name is: " + name);
    }
}
```
Person.java
{:.figure}

```java
public class Application {
     
    public static void main(String[] args) {
         
        Machine mach1 = new Machine();
        mach1.start();
         
        Person person1 = new Person("Bob");
        person1.greet();
         
        Info info1 = new Machine();
        info1.showInfo();
         
        Info info2 = person1;
        info2.showInfo();
         
        System.out.println();
         
        outputInfo(mach1);
        outputInfo(person1);
    }
     
    private static void outputInfo(Info info) {
        info.showInfo();
    }
 
}
```
Application.java
{:.figure}

## Public, Private, Protected

```java
package world;
 
public class Field {
    private Plant plant = new Plant();
     
    public Field() {
         
        // size is protected; Field is in the same package as Plant.
        System.out.println(plant.size);
    }
}
```
world/Field.java
{:.figure}

```java
package world;
 
class Something {
     
}
 
public class Plant {
    // Bad practice
    public String name;
     
    // Accepatable practice --- it's final.
    public final static int ID = 8;
     
    private String type;
     
    protected String size;
     
    int height;
     
    public Plant() {
        this.name = "Freddy";
        this.type = "plant";
        this.size = "medium";
        this.height = 8;
    }
}
```
world/Plant.java
{:.figure}

```java
package world;
 
public class Oak extends Plant {
     
    public Oak() {
         
        // Won't work -- type is private
        // type = "tree";
         
        // This works --- size is protected, Oak is a subclass of plant.
        this.size = "large";
         
        // No access specifier; works because Oak and Plant in same package
        this.height = 10;
    }
 
}
```
world/Oak.java
{:.figure}

```java
import world.Plant;
 
 
public class Grass extends Plant {
    public Grass() {
         
        // Won't work --- Grass not in same package as plant, even though it's a subclass
        // System.out.println(this.height);
    }
}
```
Grass.java
{:.figure}

```java
import world.Plant;
 
/*
 * private --- only within same class
 * public --- from anywhere
 * protected -- same class, subclass, and same package
 * no modifier -- same package only
 */
 
public class Application {
 
    /**
     * @param args
     */
    public static void main(String[] args) {
        Plant plant = new Plant();
         
        System.out.println(plant.name);
         
        System.out.println(plant.ID);
         
        // Won't work --- type is private
        //System.out.println(plant.type);
         
        // size is protected; App is not in the same package as Plant.
        // Won't work
        // System.out.println(plant.size);
         
        // Won't work; App and Plant in different packages, height has package-level visibility.
        //System.out.println(plant.height);
 
    }
 
}
```
Application.java
{:.figure}

## Polymorphism

```java
public class Plant {
    public void grow() {
        System.out.println("Plant growing");
    }
}
```
Plant.java
{:.figure}

```java
public class Tree extends Plant {
 
    @Override
    public void grow() {
        System.out.println("Tree growing");
    }
     
    public void shedLeaves() {
        System.out.println("Leaves shedding.");
    }
     
}
```
Tree.java
{:.figure}

```java
public class Application {
 
    public static void main(String[] args) {
         
         
        Plant plant1 = new Plant();
         
        // Tree is a kind of Plant (it extends Plant)
        Tree tree = new Tree();
         
        // Polymorphism guarantees that we can use a child class
        // wherever a parent class is expected.
        Plant plant2 = tree;
         
        // plant2 references a Tree, so the Tree grow() method is called.
        plant2.grow();
         
        // The type of the reference decided what methods you can actually call;
        // we need a Tree-type reference to call tree-specific methods.
        tree.shedLeaves();
         
        // ... so this won't work.
        //plant2.shedLeaves();
         
        // Another example of polymorphism.
        doGrow(tree);
    }
     
    public static void doGrow(Plant plant) {
        plant.grow();
    }
 
}
```
Application.java
{:.figure}

## Encapsulation and the API Docs

```java
class Plant {
     
    // Usually only static final members are public
    public static final int ID = 7;
     
    // Instance variables should be declared private, 
    // or at least protected.
    private String name;
     
    // Only methods intended for use outside the class
    // should be public. These methods should be documented
    // carefully if you distribute your code.
    public String getData() {
        String data = "some stuff" + calculateGrowthForecast();
         
        return data;
    }
     
    // Methods only used the the class itself should
    // be private or protected.
    private int calculateGrowthForecast() {
        return 9;
    }
     
 
    public String getName() {
        return name;
    }
 
    public void setName(String name) {
        this.name = name;
    }
     
     
}
 
 
public class Application {
 
    public static void main(String[] args) {
         
    }
 
}
```
Application.java
{:.figure}

## Casting Numerical Values

```java
public class Application {
 
    /**
     * @param args
     */
    public static void main(String[] args) {
 
        byte byteValue = 20;
        short shortValue = 55;
        int intValue = 888;
        long longValue = 23355;
         
        float floatValue = 8834.8f;
        float floatValue2 = (float)99.3;
        double doubleValue = 32.4;
         
        System.out.println(Byte.MAX_VALUE);
         
        intValue = (int)longValue;
         
        System.out.println(intValue);
         
        doubleValue = intValue;
        System.out.println(doubleValue);
         
        intValue = (int)floatValue;
        System.out.println(intValue);
     
     
        // The following won't work as we expect it to!!
        // 128 is too big for a byte.
        byteValue = (byte)128;
        System.out.println(byteValue);
 
    }
 
}
```
Application.java
{:.figure}

## Upcasting and Downcasting

```java
class Machine {
    public void start() {
        System.out.println("Machine started.");
    }
}
 
class Camera extends Machine {
    public void start() {
        System.out.println("Camera started.");
    }
     
    public void snap() {
        System.out.println("Photo taken.");
    }
}
 
 
public class Application {
    public static void main(String[] args) {
 
        Machine machine1 = new Machine();
        Camera camera1 = new Camera();
         
        machine1.start();
        camera1.start();
        camera1.snap();
         
        // Upcasting 
        Machine machine2 = camera1;
        machine2.start();
        // error: machine2.snap();
 
        // Downcasting
        Machine machine3 = new Camera();
        Camera camera2 = (Camera)machine3;
        camera2.start();
        camera2.snap();
         
        // Doesn't work --- runtime error.
        Machine machine4 = new Machine();
        // Camera camera3 = (Camera)machine4;
        // camera3.start();
        // camera3.snap();
    }
 
}
```
Application.java
{:.figure}

## Using Generics

```java
import java.util.ArrayList;
import java.util.HashMap;
 
class Animal {
     
}
 
 
public class Application {
 
    public static void main(String[] args) {
         
        /////////////////// Before Java 5 ////////////////////////
        ArrayList list = new ArrayList();
         
        list.add("apple");
        list.add("banana");
        list.add("orange");
         
        String fruit = (String)list.get(1);
         
        System.out.println(fruit);
         
        /////////////// Modern style //////////////////////////////
         
        ArrayList<String> strings = new ArrayList<String>();
         
        strings.add("cat");
        strings.add("dog");
        strings.add("alligator");
         
        String animal = strings.get(1);
         
        System.out.println(animal);
         
         
        ///////////// There can be more than one type argument ////////////////////
         
        HashMap<Integer, String> map = new HashMap<Integer, String>();
         
         
        //////////// Java 7 style /////////////////////////////////
         
        ArrayList<Animal> someList = new ArrayList<>();
    }
 
}
```
Application.java
{:.figure}

## Generics and Wildcards

```java
import java.util.ArrayList;
 
class Machine {
 
    @Override
    public String toString() {
        return "I am a machine";
    }
     
    public void start() {
        System.out.println("Machine starting.");
    }
 
}
 
class Camera extends Machine {
    @Override
    public String toString() {
        return "I am a camera";
    }
     
    public void snap() {
        System.out.println("snap!");
    }
}
 
public class Application {
 
    public static void main(String[] args) {
 
        ArrayList<Machine> list1 = new ArrayList<Machine>();
 
        list1.add(new Machine());
        list1.add(new Machine());
 
        ArrayList<Camera> list2 = new ArrayList<Camera>();
 
        list2.add(new Camera());
        list2.add(new Camera());
 
        showList(list2);
        showList2(list1);
        showList3(list1);
    }
 
    public static void showList(ArrayList<? extends Machine> list) {
        for (Machine value : list) {
            System.out.println(value);
            value.start();
        }
 
    }
     
    public static void showList2(ArrayList<? super Camera> list) {
        for (Object value : list) {
            System.out.println(value);
        }
    }
     
    public static void showList3(ArrayList<?> list) {
        for (Object value : list) {
            System.out.println(value);
        }
    }
 
 
}
```
Application.java
{:.figure}

## Anonymous Classes

```java
class Machine {
    public void start() {
        System.out.println("Starting machine ...");
    }
}
 
interface Plant {
    public void grow();
}
 
public class Application {
 
    public static void main(String[] args) {
         
        // This is equivalent to creating a class that "extends"
        // Machine and overrides the start method.
        Machine machine1 = new Machine() {
            @Override public void start() {
                System.out.println("Camera snapping ....");
            }
        };
         
        machine1.start();
         
        // This is equivalent to creating a class that "implements"
        // the Plant interface
        Plant plant1 = new Plant() {
            @Override
            public void grow() {
                System.out.println("Plant growing");
                 
            }
        };
         
        plant1.grow();
    }
}
```
Application.java
{:.figure}

## Reading Files using Scanner

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
 
 
public class Application {
 
    public static void main(String[] args) throws FileNotFoundException {
        //String fileName = "C:/Users/John/Desktop/example.txt";
        String fileName = "example.txt";
         
        File textFile = new File(fileName);
         
        Scanner in = new Scanner(textFile);
         
        int value = in.nextInt();
        System.out.println("Read value: " + value);
         
        in.nextLine();
         
        int count = 2;
        while(in.hasNextLine()) {
            String line = in.nextLine();
             
            System.out.println(count + ": " + line);
            count++;
        }
         
        in.close();
    }
 
}
```
Application.java
{:.figure}

## Handling exceptions

```java
package demo1;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
 
 
 
public class Application {
 
    public static void main(String[] args) throws FileNotFoundException {
         
        File file = new File("test.txt");
         
        FileReader fr = new FileReader(file);
    }
 
}
```
demo1/Application.java
{:.figure}

```java
package demo2;
 
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
 
public class Application {
 
    public static void main(String[] args) {
        File file = new File("test.txt");
 
        try {
            FileReader fr = new FileReader(file);
             
            // This will not be executed if an exception is thrown.
            System.out.println("Continuing ....");
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + file.toString());
        }
 
        System.out.println("Finished.");
    }
 
}
```
demo2/Application.java
{:.figure}

```java
package demo3;
 
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
 
public class Application {
 
    public static void main(String[] args) {
        try {
            openFile();
        } catch (FileNotFoundException e) {
            // PS. This message is too vague : )
            System.out.println("Could not open file");
        }
    }
 
    public static void openFile() throws FileNotFoundException {
        File file = new File("test.txt");
 
        FileReader fr = new FileReader(file);
 
    }
 
}
```
demo3/Application.java
{:.figure}

## Multiple Exceptions

```java
import java.io.FileNotFoundException;
import java.io.IOException;
import java.text.ParseException;
 
 
public class Test {
    public void run() throws IOException, ParseException {
         
         
        //throw new IOException();
         
        throw new ParseException("Error in command list.", 2);
         
         
    }
     
    public void input() throws IOException, FileNotFoundException {
         
    }
}
```
Test.java
{:.figure}

```java
import java.io.FileNotFoundException;
import java.io.IOException;
import java.text.ParseException;
 
public class Application {
 
    public static void main(String[] args)  {
        Test test = new Test();
         
        // Multiple catch blocks
        try {
            test.run();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ParseException e) {
            System.out.println("Couldn't parse command file.");
        }
         
        // Try multi-catch (Java 7+ only)
        try {
            test.run();
        } catch (IOException | ParseException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
 
        // Using polymorphism to catch the parent of all exceptions
        try {
            test.run();
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } 
         
        // Important to catch exceptions in the right order!
        // IOException cannot come first, because it's the parent
        // of FileNotFoundException, so would catch both exceptions
        // in this case.
        try {
            test.input();
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
         
     
    }
 
}
```
Application.java
{:.figure}

## Runtime vs. checked Exceptions

```java
public class Application {
 
    public static void main(String[] args) {
         
        // Null pointer exception ....
        String text = null;
         
        System.out.println(text.length());
         
        // Arithmetic exception ... (divide by zero)
        int value = 7/0;
 
        // You can actually handle RuntimeExceptions if you want to;
        // for example, here we handle an ArrayIndexOutOfBoundsException
        String[] texts = { "one", "two", "three" };
 
        try {
            System.out.println(texts[3]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println(e.toString());
        }
    }
}
```
Application.java
{:.figure}

## Abstract Classes

```java
public abstract class Machine {
    private int id;
 
    public int getId() {
        return id;
    }
 
    public void setId(int id) {
        this.id = id;
    }
     
    public abstract void start();
    public abstract void doStuff();
    public abstract void shutdown();
     
    public void run() {
        start();
        doStuff();
        shutdown();
    }
}
```
Machine.java
{:.figure}

```java
public class Camera extends Machine {
 
    @Override
    public void start() {
        System.out.println("Starting camera.");
    }
 
    @Override
    public void doStuff() {
        System.out.println("Taking a photo");
         
    }
 
    @Override
    public void shutdown() {
        System.out.println("Shutting down the camera.");
         
    }
 
}
```
Camera.java
{:.figure}

```java
public class Car extends Machine {
 
    @Override
    public void start() {
        System.out.println("Starting ignition...");
         
    }
 
    @Override
    public void doStuff() {
        System.out.println("Driving...");
    }
 
    @Override
    public void shutdown() {
        System.out.println("Switch off ignition.");
           
    }
 
}
```
Car.java
{:.figure}

```java
public class Application {
 
    public static void main(String[] args) {
        Camera cam1 = new Camera();
        cam1.setId(5);
         
        Car car1 = new Car();
        car1.setId(4);
         
        car1.run();
         
        //Machine machine1 = new Machine();
    }
 
}
```
Application.java
{:.figure}

## Reading Files With File Reader

```java
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
 
 
public class Application {
 
    public static void main(String[] args) {
 
        File file = new File("test.txt");
         
        BufferedReader br = null;
         
        try {
            FileReader fr = new FileReader(file);
            br = new BufferedReader(fr);
             
            String line;
             
            while( (line = br.readLine()) != null ) {
                System.out.println(line);
            }
             
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + file.toString());
        } catch (IOException e) {
            System.out.println("Unable to read file: " + file.toString());
        }
        finally {
            try {
                br.close();
            } catch (IOException e) {
                System.out.println("Unable to close file: " + file.toString());
            }
            catch(NullPointerException ex) {
                // File was probably never opened!
            }
        }
         
         
 
    }
 
}
```
Application.java
{:.figure}

## Try With Resources

```java
class Temp implements AutoCloseable {
 
    @Override
    public void close() throws Exception {
        System.out.println("Closing!");
        throw new Exception("oh no!");
    }
     
}
 
 
public class App {
 
    public static void main(String[] args) {
         
        try(Temp temp = new Temp()) {
             
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
         
         
    }
 
}
```
Application.java
{:.figure}

```java
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
 
public class Application2 {
 
    public static void main(String[] args) {
        File file = new File("test.txt");
 
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
 
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (FileNotFoundException e) {
            System.out.println("Can't find file " + file.toString());
        } catch (IOException e) {
            System.out.println("Unable to read file " + file.toString());
        }
 
    }
 
}
```
Application2.java
{:.figure}

## Creating and Writing Text Files

```java
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
 
 
public class Application {
 
     
    public static void main(String[] args) {
        File file = new File("test.txt");
          
        try (BufferedWriter br = new BufferedWriter(new FileWriter(file))) {
           br.write("This is line one");
           br.newLine();
           br.write("This is line two");
           br.newLine();
           br.write("Last line.");
        } catch (IOException e) {
            System.out.println("Unable to read file " + file.toString());
        }
  
 
    }
 
}
```
Application.java
{:.figure}

```sh
This is line one
This is line two
Last line.
```
test.txt
{:.figure}

## The `equals()` Method

```java
class Person {
    private int id;
    private String name;
 
    public Person(int id, String name) {
        this.id = id;
        this.name = name;
    }
 
    @Override
    public String toString() {
        return "Person [id=" + id + ", name=" + name + "]";
    }
 
    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + id;
        result = prime * result + ((name == null) ? 0 : name.hashCode());
        return result;
    }
 
    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Person other = (Person) obj;
        if (id != other.id)
            return false;
        if (name == null) {
            if (other.name != null)
                return false;
        } else if (!name.equals(other.name))
            return false;
        return true;
    }
 
     
}
 
public class Application {
 
    public static void main(String[] args) {
         
        System.out.println(new Object());
 
        Person person1 = new Person(5, "Bob");
        Person person2 = new Person(5, "Bob");
         
 
        System.out.println(person1.equals(person2));
         
        Double value1 = 7.2;
        Double value2 = 7.2;
         
        System.out.println(value1.equals(value2));
         
        Integer number1 = 6;
        Integer number2 = 6;
         
        System.out.println(number1.equals(number2));
         
        String text1 = "Hello";
        String text2 = "Hellodfadf".substring(0, 5);
         
        System.out.println(text2);
         
        System.out.println(text1.equals(text2));
    }
 
}
```
Application.java
{:.figure}

## Inner Classes

```java
public class Robot {
 
    private int id;
     
    // Non-static nested classes have access to the enclosing
    // class's instance data. E.g. implement Iterable
    // http://www.caveofprogramming.com/java/using-iterable-java-collections-framework-video-tutorial-part-11/
    // Use them to group functionality.
    private class Brain {
        public void think() {
            System.out.println("Robot " + id + " is thinking.");
        }
    }
 
    // static inner classes do not have access to instance data.
    // They are really just like "normal" classes, except that they are grouped
    // within an outer class. Use them for grouping classes together.
    public static class Battery {
        public void charge() {
            System.out.println("Battery charging...");
        }
    }
 
    public Robot(int id) {
        this.id = id;
    }
 
    public void start() {
        System.out.println("Starting robot " + id);
         
        // Use Brain. We don't have an instance of brain
        // until we create one. Instances of brain are 
        // always associated with instances of Robot (the
        // enclosing class).
        Brain brain = new Brain();
        brain.think();
         
        final String name = "Robert";
         
        // Sometimes it's useful to create local classes
        // within methods. You can use them only within the method.
        class Temp {
            public void doSomething() {
                System.out.println("ID is: " + id);
                System.out.println("My name is " + name);
            }
        }
         
        Temp temp = new Temp();
        temp.doSomething();
    }
}
```
Robot.java
{:.figure}

```java
public class Application {
 
     
    public static void main(String[] args) {
     
        Robot robot = new Robot(7);
        robot.start();
         
        // The syntax below will only work if Brain is
        // declared public. It is quite unusual to do this.
        // Robot.Brain brain = robot.new Brain();
        // brain.think();
         
        // This is very typical Java syntax, using
        // a static inner class.
        Robot.Battery battery = new Robot.Battery();
        battery.charge();
    }
 
}
```
Application.java
{:.figure}

## Enum Types - Basic and Advanced Usage

```java
public enum Animal {
    CAT("Fergus"), DOG("Fido"), MOUSE("Jerry");
     
    private String name;
     
    Animal(String name) {
        this.name = name;
    }
 
    public String getName() {
        return name;
    }
     
    public String toString() {
        return "This animal is called: " + name;
    }
}
```
Animal.java
{:.figure}

```java
public class Application {
     
    public static void main(String[] args) {
         
        Animal animal = Animal.DOG;
         
        switch(animal) {
        case CAT:
            System.out.println("Cat");
            break;
        case DOG:
            System.out.println("Dog");
            break;
        case MOUSE:
            break;
        default:
            break;
 
        }
         
        System.out.println(Animal.DOG);
        System.out.println("Enum name as a string: " + Animal.DOG.name());
         
        System.out.println(Animal.DOG.getClass());
         
        System.out.println(Animal.DOG instanceof Enum);
         
        System.out.println(Animal.MOUSE.getName());
         
        Animal animal2 = Animal.valueOf("CAT");
         
        System.out.println(animal2);
    }
 
}
```
Application.java
{:.figure}

## Recursion - A useful trick up your sleeve

```java
public class App {
 
     
    public static void main(String[] args) {
         
        // E.g. 4! = 4*3*2*1 (factorial 4)
         
        System.out.println(factorial(5));
    }
     
    private static int factorial(int value) {
        //System.out.println(value);
         
        if(value == 1) {
            return 1;
        }
         
        return factorial(value - 1) * value;
    }
 
}
```
Application.java
{:.figure}

## Serialization - Saving Objects to Files

```java
import java.io.Serializable;
 
public class Person implements Serializable {
     
    private static final long serialVersionUID = 4801633306273802062L;
     
    private int id;
    private String name;
     
    public Person(int id, String name) {
        this.id = id;
        this.name = name;
    }
 
    @Override
    public String toString() {
        return "Person [id=" + id + ", name=" + name + "]";
    }
}
 
// www.caveofprogramming.com
```
Person.java
{:.figure}

```java
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
 
 
 
public class WriteObjects {
 
    public static void main(String[] args) {
        System.out.println("Writing objects...");
 
        Person mike = new Person(543, "Mike");
        Person sue = new Person(123, "Sue");
         
        System.out.println(mike);
        System.out.println(sue);
         
        try(FileOutputStream fs = new FileOutputStream("people.bin")) {
             
            ObjectOutputStream os = new ObjectOutputStream(fs);
             
            os.writeObject(mike);
            os.writeObject(sue);
             
            os.close();
             
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
     
    }
 
}
```
WriteObjects.java
{:.figure}

```java
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
 
 
 
public class ReadObjects {
 
     
    public static void main(String[] args) {
        System.out.println("Reading objects...");
 
        try(FileInputStream fi = new FileInputStream("people.bin")) {
             
            ObjectInputStream os = new ObjectInputStream(fi);
             
            Person person1 = (Person)os.readObject();
            Person person2 = (Person)os.readObject();
             
            os.close();
             
            System.out.println(person1);
            System.out.println(person2);
             
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
         
    }
 
}
```
ReadObjects.java
{:.figure}

## Serializing Arrays

```java
import java.io.Serializable;
 
public class Person implements Serializable {
     
    private static final long serialVersionUID = 4801633306273802062L;
     
    private int id;
    private String name;
     
    public Person(int id, String name) {
        this.id = id;
        this.name = name;
    }
 
    @Override
    public String toString() {
        return "Person [id=" + id + ", name=" + name + "]";
    }
}
 
// www.caveofprogramming.com
```
Person.java
{:.figure}

```java
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
 
public class WriteObjects {
 
    public static void main(String[] args) {
        System.out.println("Writing objects...");
         
        Person[] people = {new Person(1, "Sue"), new Person(99, "Mike"), new Person(7, "Bob")};
         
        ArrayList<Person> peopleList = new ArrayList<Person>(Arrays.asList(people));
 
        try (FileOutputStream fs = new FileOutputStream("test.ser"); ObjectOutputStream os = new ObjectOutputStream(fs)) {
 
            // Write entire array
            os.writeObject(people);
             
            // Write arraylist
            os.writeObject(peopleList);
             
            // Write objects one by one
            os.writeInt(peopleList.size());
             
            for(Person person: peopleList) {
                os.writeObject(person);
            }
             
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
 
    }
 
}
```
WriteObjects.java
{:.figure}

```java
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
 
public class ReadObjects {
 
    public static void main(String[] args) {
        System.out.println("Reading objects...");
         
        try (FileInputStream fi = new FileInputStream("test.ser"); ObjectInputStream os = new ObjectInputStream(fi)) {
 
            // Read entire array
            Person[] people = (Person[])os.readObject();
             
            // Read entire arraylist
            @SuppressWarnings("unchecked")
            ArrayList<Person> peopleList = (ArrayList<Person>)os.readObject();
             
            for(Person person: people) {
                System.out.println(person);
            }
             
            for(Person person: peopleList) {
                System.out.println(person);
            }
             
            // Read objects one by one.
            int num = os.readInt();
             
            for(int i=0; i<num; i++) {
                Person person = (Person)os.readObject();
                System.out.println(person);
            }
             
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
 
    }
 
}
```
ReadObjects.java
{:.figure}

## ArrayList - Arrays the Easy Way

```java
import java.util.ArrayList;
import java.util.List;
 
public class Application {
 
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<Integer>();
 
        // Adding
        numbers.add(10);
        numbers.add(100);
        numbers.add(40);
 
        // Retrieving
        System.out.println(numbers.get(0));
 
        System.out.println("nIteration #1: ");
        // Indexed for loop iteration
        for (int i = 0; i < numbers.size(); i++) {
            System.out.println(numbers.get(i));
        }
 
        // Removing items (careful!)
        numbers.remove(numbers.size() - 1);
 
        // This is VERY slow
        numbers.remove(0);
 
        System.out.println("nIteration #2: ");
        for (Integer value : numbers) {
            System.out.println(value);
        }
 
        // List interface ...
        List<String> values = new ArrayList<String>();
    }
}
```
Application.java
{:.figure}

## Linked Lists

```java
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
 
 
public class Application {
 
 
    public static void main(String[] args) {
        /*
         * ArrayLists manage arrays internally.
         * [0][1][2][3][4][5] ....
         */
        List<Integer> arrayList = new ArrayList<Integer>();
         
        /*
         * LinkedLists consists of elements where each element
         * has a reference to the previous and next element
         * [0]->[1]->[2] ....
         *    <-   <-
         */
        List<Integer> linkedList = new LinkedList<Integer>();
         
        doTimings("ArrayList", arrayList);
        doTimings("LinkedList" , linkedList);
    }
     
    private static void doTimings(String type, List<Integer> list) {
         
        for(int i=0; i<1E5; i++) {
            list.add(i);
        }
         
        long start = System.currentTimeMillis();
         
        /*
        // Add items at end of list
        for(int i=0; i<1E5; i++) {
            list.add(i);
        }
        */
         
        // Add items elsewhere in list
        for(int i=0; i<1E5; i++) {
            list.add(0, i);
        }
         
        long end = System.currentTimeMillis();
         
        System.out.println("Time taken: " + (end - start) + " ms for " + type);
    }
     
 
 
}
```
Application.java
{:.figure}

## HashMaps - Retrieving Objects via a Key

```java
import java.util.HashMap;
import java.util.Map;
 
public class Application {
 
 
    public static void main(String[] args) {
 
        HashMap<Integer, String> map = new HashMap<Integer, String>();
         
        map.put(5, "Five");
        map.put(8, "Eight");
        map.put(6, "Six");
        map.put(4, "Four");
        map.put(2, "Two");
         
        String text = map.get(6);
         
        System.out.println(text);
         
        for(Map.Entry<Integer, String> entry: map.entrySet()) {
            int key = entry.getKey();
            String value = entry.getValue();
             
            System.out.println(key + ": " + value);
        }
         
    }
 
}
```
Application.java
{:.figure}

## Sorted Maps

```java
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.TreeMap;
 
public class Application {
 
    public static void main(String[] args) {
        Map<Integer, String> hashMap = new HashMap<Integer, String>();
        Map<Integer, String> linkedHashMap = new LinkedHashMap<Integer, String>();
        Map<Integer, String> treeMap = new TreeMap<Integer, String>();
         
        testMap(treeMap);
    }
     
    public static void testMap(Map<Integer, String> map) {
        map.put(9, "fox");
        map.put(4, "cat");
        map.put(8, "dog");
        map.put(1, "giraffe");
        map.put(0, "swan");
        map.put(15, "bear");
        map.put(6, "snake");
         
        for(Integer key: map.keySet()) {
            String value = map.get(key);
             
            System.out.println(key + ": " + value);
        }
    }
     
}
```
Application.java
{:.figure}

## Sets

```java
import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;
 
public class Application {
 
    public static void main(String[] args) {
 
        // HashSet does not retain order.
        // Set<String> set1 = new HashSet<String>();
 
        // LinkedHashSet remembers the order you added items in
        // Set<String> set1 = new LinkedHashSet<String>();
 
        // TreeSet sorts in natural order
        Set<String> set1 = new TreeSet<String>();
 
        if (set1.isEmpty()) {
            System.out.println("Set is empty at start");
        }
 
        set1.add("dog");
        set1.add("cat");
        set1.add("mouse");
        set1.add("snake");
        set1.add("bear");
 
        if (set1.isEmpty()) {
            System.out.println("Set is empty after adding (no!)");
        }
 
        // Adding duplicate items does nothing.
        set1.add("mouse");
 
        System.out.println(set1);
 
        // ///////// Iteration ////////////////
 
        for (String element : set1) {
            System.out.println(element);
        }
 
        // ////////// Does set contains a given item? //////////
        if (set1.contains("aardvark")) {
            System.out.println("Contains aardvark");
        }
 
        if (set1.contains("cat")) {
            System.out.println("Contains cat");
        }
 
        /// set2 contains some common elements with set1, and some new
 
        Set<String> set2 = new TreeSet<String>();
 
        set2.add("dog");
        set2.add("cat");
        set2.add("giraffe");
        set2.add("monkey");
        set2.add("ant");
         
        ////////////// Intersection ///////////////////
         
        Set<String> intersection = new HashSet<String>(set1);
         
        intersection.retainAll(set2);
         
        System.out.println(intersection);
         
        ////////////// Difference /////////////////////////
         
        Set<String> difference = new HashSet<String>(set2);
         
        difference.removeAll(set1);
        System.out.println(difference);
    }
 
}
```
Application.java
{:.figure}

## Using Custom Objects in Sets and as Keys in Maps

```java
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.Set;
 
class Person {
    private int id;
    private String name;
     
    public Person(int id, String name) {
        this.id = id;
        this.name = name;
    }
     
    public String toString() {
        return "{ID is: " + id + "; name is: " + name + "}";
    }
 
    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + id;
        result = prime * result + ((name == null) ? 0 : name.hashCode());
        return result;
    }
 
    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        final Person other = (Person) obj;
        if (id != other.id)
            return false;
        if (name == null) {
            if (other.name != null)
                return false;
        } else if (!name.equals(other.name))
            return false;
        return true;
    }
     
     
}
 
 
public class Application {
 
    public static void main(String[] args) {
         
        Person p1 = new Person(0, "Bob");
        Person p2 = new Person(1, "Sue");
        Person p3 = new Person(2, "Mike");
        Person p4 = new Person(1, "Sue");
         
        Map<Person, Integer> map = new LinkedHashMap<Person, Integer>();
         
        map.put(p1, 1);
        map.put(p2, 2);
        map.put(p3, 3);
        map.put(p4, 1);
         
        for(Person key: map.keySet()) {
            System.out.println(key + ": " + map.get(key));
        }
         
        Set<Person> set = new LinkedHashSet<Person>();
         
        set.add(p1);
        set.add(p2);
        set.add(p3);
        set.add(p4);
         
        System.out.println(set);
    }
 
}
```
Application.java
{:.figure}

## Sorting Lists

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
 
class Person {
    private int id;
    private String name;
     
    public Person(int id, String name) {
        this.id = id;
        this.name = name;
    }
 
    public int getId() {
        return id;
    }
 
    public void setId(int id) {
        this.id = id;
    }
 
    public String getName() {
        return name;
    }
 
    public void setName(String name) {
        this.name = name;
    }
     
    public String toString() {
        return id + ": " + name;
    }
}
 
class StringLengthComparator implements Comparator<String> {
 
    @Override
    public int compare(String s1, String s2) {
 
        int len1 = s1.length();
        int len2 = s2.length();
         
        if(len1 > len2) {
            return 1;
        }
        else if(len1 < len2) {
            return -1;
        }
         
        return 0;
    }
}
 
class ReverseAlphabeticalComparator implements Comparator<String> {
 
    @Override
    public int compare(String s1, String s2) {
        return -s1.compareTo(s2);
    }
}
 
public class Application {
 
     
    public static void main(String[] args) {
         
        ////////////////////// Sorting Strings ////////////////////////////////
        List<String> animals = new ArrayList<String>();
         
        animals.add("tiger");
        animals.add("lion");
        animals.add("cat");
        animals.add("snake");
        animals.add("mongoose");
        animals.add("elephant");
         
        // Collections.sort(animals, new StringLengthComparator());
        Collections.sort(animals, new ReverseAlphabeticalComparator());
         
        for(String animal: animals) {
            System.out.println(animal);
        }
     
        ////////////////////// Sorting Numbers ////////////////////////////////
        List<Integer> numbers = new ArrayList<Integer>();
         
        numbers.add(3);
        numbers.add(36);
        numbers.add(73);
        numbers.add(40);
        numbers.add(1);
         
        Collections.sort(numbers, new Comparator<Integer>() {
            public int compare(Integer num1, Integer num2) {
                return -num1.compareTo(num2);
            }
        });
         
        for(Integer number: numbers) {
            System.out.println(number);
        }
         
        ////////////////////// Sorting arbitary objects ////////////////////////////////
         
        List<Person> people = new ArrayList<Person>();
         
        people.add(new Person(1, "Joe"));
        people.add(new Person(3, "Bob"));
        people.add(new Person(4, "Clare"));
        people.add(new Person(2, "Sue"));
         
        // Sort in order of ID
        Collections.sort(people, new Comparator<Person>() {
            public int compare(Person p1, Person p2) {
 
                if(p1.getId() > p2.getId()) {
                    return 1;
                }
                else if(p1.getId() < p2.getId()) {
                    return -1;
                }
                 
                return 0;
            }
        });
         
        for(Person person: people) {
            System.out.println(person);
        }
         
        System.out.println("n");
        // Sort in order of name
        Collections.sort(people, new Comparator<Person>() {
            public int compare(Person p1, Person p2) {
                return p1.getName().compareTo(p2.getName());
            }
        });
         
        for(Person person: people) {
            System.out.println(person);
        }
         
    }
 
}
```
Application.java
{:.figure}

## Natural Ordering

```java
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.SortedSet;
import java.util.TreeSet;
 
class Person implements Comparable<Person> {
    private String name;
     
    public Person(String name) {
        this.name = name;
    }
     
    public String toString() {
        return name;
    }
 
    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((name == null) ? 0 : name.hashCode());
        return result;
    }
 
    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        final Person other = (Person) obj;
        if (name == null) {
            if (other.name != null)
                return false;
        } else if (!name.equals(other.name))
            return false;
        return true;
    }
 
    @Override
    public int compareTo(Person person) {
        int len1 = name.length();
        int len2 = person.name.length();
         
        if(len1 > len2) {
            return 1;
        }
        else if(len1 < len2) {
            return -1;
        }
        else {
            return name.compareTo(person.name);
        }
    }
}
 
public class Application {
 
    public static void main(String[] args) {
        List<Person> list = new ArrayList<Person>();
        SortedSet<Person> set = new TreeSet<Person>();
         
        addElements(list);
        addElements(set);
         
        Collections.sort(list);
         
        showElements(list);
        System.out.println();
        showElements(set);
    }
     
    private static void addElements(Collection<Person> col) {
        col.add(new Person("Joe"));
        col.add(new Person("Sue"));
        col.add(new Person("Juliet"));
        col.add(new Person("Clare"));
        col.add(new Person("Mike"));
    }
     
    private static void showElements(Collection<Person> col) {
        for(Person element: col) {
            System.out.println(element);
        }
    }
 
}

```
Application.java
{:.figure}

## Queues

```java
import java.util.NoSuchElementException;
import java.util.Queue;
import java.util.concurrent.ArrayBlockingQueue;
 
 
 
 
public class Application {
 
    public static void main(String[] args) {
        //  (head) <- oooooooooooooooooooooooo <- (tail) FIFO (first in, first out)
         
        Queue<Integer> q1 = new ArrayBlockingQueue<Integer>(3);
         
        // Throws NoSuchElement exception --- no items in queue yet
        // System.out.println("Head of queue is: " + q1.element());
         
        q1.add(10);
        q1.add(20);
        q1.add(30);
         
        System.out.println("Head of queue is: " + q1.element());
         
        try {
            q1.add(40);
        } catch (IllegalStateException e) {
            System.out.println("Tried to add too many items to the queue.");
        }
         
        for(Integer value: q1) {
            System.out.println("Queue value: " + value);
        }
         
        System.out.println("Removed from queue: " + q1.remove());
        System.out.println("Removed from queue: " + q1.remove());
        System.out.println("Removed from queue: " + q1.remove());
         
        try {
            System.out.println("Removed from queue: " + q1.remove());
        } catch (NoSuchElementException e) {
            System.out.println("Tried to remove too many items from queue");
        }
         
        ////////////////////////////////////////////////////////////////////
         
        Queue<Integer> q2 = new ArrayBlockingQueue<Integer>(2);
         
        System.out.println("Queue 2 peek: " + q2.peek());
         
        q2.offer(10);
        q2.offer(20);
         
        System.out.println("Queue 2 peek: " + q2.peek());
         
        if(q2.offer(30) == false) {
            System.out.println("Offer failed to add third item.");
        }
         
        for(Integer value: q2) {
            System.out.println("Queue 2 value: " + value);
        }
         
        System.out.println("Queue 2 poll: " + q2.poll());
        System.out.println("Queue 2 poll: " + q2.poll());
        System.out.println("Queue 2 poll: " + q2.poll());
    }
 
}
```
Application.java
{:.figure}

## Using Iterators

```java
import java.util.Iterator;
import java.util.LinkedList;
 
public class Application {
 
    public static void main(String[] args) {
 
        LinkedList<String> animals = new LinkedList<String>();
 
        animals.add("fox");
        animals.add("cat");
        animals.add("dog");
        animals.add("rabbit");
         
        // "Old" way of iterating through lists (except that generics
        // didn't exist pre Java 5). This way is still an integral part
        // of Java; it allows you to remove items from the list
        // and also supports the "for each" syntax behind the scenes.
 
        Iterator<String> it = animals.iterator();
 
        while (it.hasNext()) {
            String value = it.next();
            System.out.println(value);
             
            if(value.equals("cat")) {
                it.remove();
            }
        }
 
        System.out.println();
         
        /*
         * If you want to add items to a list while iterating through
         * it, get a ListIterator using the .listIterator() method.
         * ListIterator also has a previous() method, allowing you to
         * "rewind" the iterator so that you can add items before
         * the current item.
         */
 
        // / Modern iteration, Java 5 and later; "for each" loop
 
        for (String animal : animals) {
            System.out.println(animal);
             
            // The following won't work; you need an iterator.
            // Throws ConcurrentModificationException
            // animals.remove(2);
        }
    }
 
}
```
Application.java
{:.figure}

## Implementing Iterable

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.Iterator;
import java.util.LinkedList;
 
 
public class UrlLibrary implements Iterable<String> {
    private LinkedList<String> urls = new LinkedList<String>();
 
    private class UrlIterator implements Iterator<String> {
         
        private int index = 0;
 
        @Override
        public boolean hasNext() {
            return index < urls.size();
        }
 
        @Override
        public String next() {
             
            StringBuilder sb = new StringBuilder();
             
            try {
                URL url = new URL(urls.get(index));
                 
                BufferedReader br = new BufferedReader(new InputStreamReader(url.openStream()));
                 
                String line = null;
                 
                while( (line = br.readLine()) != null) {
                    sb.append(line);
                    sb.append("n");
                }
                 
                br.close();
                 
            } catch (Exception e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
             
            index++;
             
            return sb.toString();
        }
 
        @Override
        public void remove() {
            urls.remove(index);
        }
         
    }
     
    public UrlLibrary() {
        urls.add("http://www.caveofprogramming.com");
        urls.add("http://www.facebook.com/caveofprogramming");
        urls.add("http://news.bbc.co.uk");
    }
 
    @Override
    public Iterator<String> iterator() {
        return new UrlIterator();
    }
 
    /*
    @Override
    public Iterator<String> iterator() {
        return urls.iterator();
    }
    */
     
     
}
```
UrlIterator.java
{:.figure}

## Deciding Which Collections to use

```java
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;
 
 
 
 
public class Application {
 
    public static void main(String[] args) {
         
        /* 
         * Consider:
         * 1. what you need the collection to do
         * 2. are you using the fastest collection for your purposes
         * (think about insertion/deletion, retrieval and traversal
         */
         
        //////////////// LISTS ///////////////////////////////////
         
        // Store lists of objects
        // Duplicates are allowed
        // Objects remain in order
        // Elements are indexed via an integer
        // cf. shopping list
        // Checking for particular item in list is slow
        // Looking an item up by index is fast
        // Iterating through lists is relatively fast
        // Note: you can sort lists if you want to.
         
        // If you only add or remove items at end of list, use ArrayList.
        List<String> list1 = new ArrayList<String>();
         
        // Removing or adding items elsewhere in the list?
        List<String> list2 = new LinkedList<String>();
         
        ////////////////SETS ///////////////////////////////////
         
        // Only store unique values
        // Great for removing duplicates
        // Not indexed, unlike lists
        // Very fast to check if a particular object exists
        // If you want to use your own objects, you must implement hashCode() and equals().
         
        // Order is unimportant and OK if it changes?
        // HashSet is not ordered.
        Set<String> set1 = new HashSet<String>();
         
        // Sorted in natural order? Use TreeSet - must implement Comparable for custom types
        // (1,2,3 ..., a,b,c.... etc)
        Set<String> set2 = new TreeSet<String>();
         
        // Elements remain in order they were added
        Set<String> set3 = new LinkedHashSet<String>();
         
        ////////////////MAPS ///////////////////////////////////
         
        // Key value pairs.
        // Like lookup tables
        // Retrieving a value by key is fast
        // Iterating over map values is very slow
        // Maps not really optimised for iteration
        // If you want to use your own objects as keys, you must implement hashCode() and equals().
         
        // Keys not in any particular order, and order liable to change.
        Map<String, String> map1 = new HashMap<String, String>();
         
        // Keys sorted in natural order - must implement Comparable for custom types
        Map<String, String> map2 = new TreeMap<String, String>();
         
        // Keys remain in order added 
        Map<String, String> map3 = new LinkedHashMap<String, String>();
         
        // There are also the SortedSet and SortedMap interfaces.
    }
 
}
```
Application.java
{:.figure}

## Complex Data Structures

```java
import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.Set;
 
public class Application {
 
    public static String[] vehicles = { "ambulance", "helicopter", "lifeboat" };
 
    public static String[][] drivers = { 
        { "Fred", "Sue", "Pete" },
            { "Sue", "Richard", "Bob", "Fred" }, 
            { "Pete", "Mary", "Bob" }, };
 
    public static void main(String[] args) {
 
        Map<String, Set<String>> personnel = new HashMap<String, Set<String>>();
 
        for (int i = 0; i < vehicles.length; i++) {
            String vehicle = vehicles[i];
            String[] driversList = drivers[i];
 
            Set<String> driverSet = new LinkedHashSet<String>();
 
            for (String driver : driversList) {
                driverSet.add(driver);
            }
 
            personnel.put(vehicle, driverSet);
        }
 
        { // Brackets just to scope driversList variable so can use again later
            // Example usage
            Set<String> driversList = personnel.get("helicopter");
 
            for (String driver : driversList) {
                System.out.println(driver);
            }
        }
 
        // Iterate through whole thing
        for (String vehicle : personnel.keySet()) {
            System.out.print(vehicle);
            System.out.print(": ");
            Set<String> driversList = personnel.get(vehicle);
 
            for (String driver : driversList) {
                System.out.print(driver);
                System.out.print(" ");
            }
             
            System.out.println();
        }
    }
 
}
```
Application.java
{:.figure}

