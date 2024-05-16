# Software Engineering Fundamentals with Python

## Course Description
This course introduces fundamental concepts of computer programming. We explore various topics including data structures, algorithms, and object-oriented programming using Python. Each lecture builds upon the previous ones, culminating in a comprehensive understanding of basic programming principles suitable for further study in computer science.

## Part I: Python Fundamentals

### - [ ] Lecture 1: Introduction
- Overview of the course
- Setting up the programming environment
- Introduction to Python

### - [ ] Lecture 2: Strings, Input/Output, Branching
- Working with strings
- Reading from and writing to files
- Conditional statements

### - [ ] Lecture 3: Iteration
- While loops and for loops
- Iterating through data structures

### - [ ] Lecture 4: Loops over Strings, Guess-and-Check, Binary
- Advanced loop constructs
- Problem-solving using the guess-and-check method
- Binary numbers and operations

### - [ ] Lecture 5: Floats and Approximation Methods
- Representation of floating-point numbers
- Techniques for numerical approximation

### - [ ] Lecture 6: Bisection Search
- Implementing bisection search algorithm
- Applications of bisection search

### - [x] Lecture 7: Decomposition, Abstraction, Functions
- Principles of decomposition and abstraction
- Defining and using functions

### - [x] Lecture 8: Functions as Objects
- Functions as first-class objects
- Higher-order functions

### - [x] Lecture 9: Lambda Functions, Tuples, and Lists
- Using lambda expressions
- Introduction to tuples and lists

### - [ ] Lecture 10: Lists, Mutability
- Detailed exploration of lists
- Mutability and side effects

### - [ ] Lecture 11: Aliasing, Cloning
- Concepts of aliasing and cloning lists
- Avoiding common pitfalls with mutability

### - [ ] Lecture 12: List Comprehension, Functions as Objects, Testing, Debugging
- Advanced list operations
- Techniques for testing and debugging

### - [ ] Lecture 13: Exceptions, Assertions
- Handling errors and exceptions
- Using assertions to ensure correct behavior

### - [ ] Lecture 14: Dictionaries
- Introduction to dictionaries
- Applications of dictionaries in data handling

### - [ ] Lecture 15: Recursion
- Understanding recursion
- Recursive programming examples

### - [ ] Lecture 16: Recursion on Non-Numerics
- Applying recursion to various data types
- Complex recursive algorithms

### - [x] Lecture 17: Python Classes
- Introduction to classes and objects
- Defining and using classes in Python

### - [x] Lecture 18: More Python Class Methods
- Advanced methods in classes
- Special class operations

### - [x] Lecture 19: Inheritance
- Understanding inheritance
- Building extensible and maintainable code

### - [ ] Lecture 20: Fitness Tracker Object-Oriented Programming Example
- Case study: Building a fitness tracker
- Object-oriented design and implementation

### - [ ] Lecture 21: Timing Programs, Counting Operations
- Techniques for measuring program performance
- Analyzing computational complexity

### - [ ] Lecture 22: Big Oh and Theta
- Theoretical foundations of algorithm analysis
- Big O and Theta notations

#### - [ ] Lecture 23: Complexity Classes Examples
- Exploring different complexity classes
- Examples and case studies

### - [ ] Lecture 24: Sorting Algorithms
- Overview of common sorting algorithms
- Implementing and comparing sorting techniques

### - [ ] Lecture 25: Plotting
- Visualizing data using Python
- Graphs and plots for data analysis

### - [ ] Lecture 26: List Access, Hashing, Simulations, and Wrap-Up
- Advanced data access techniques
- Introduction to hashing
- Using simulations to solve complex problems
- Course wrap-up and review

## Part II: SOLID Principle

### Lecture 27: Single Responsibility Principle
- Understanding the Single Responsibility Principle (SRP)
- Importance of having one reason for a class to change
- Case studies and refactoring examples that illustrate SRP

### Lecture 28: Open/Closed Principle
- Exploring the Open/Closed Principle (OCP)
- Techniques for making software entities extendable without modifying them
- Practical examples of applying OCP in software design

### Lecture 29: Liskov Substitution Principle
- Introduction to Liskov Substitution Principle (LSP)
- Discussion on substitutability of objects in a program
- Examples of LSP violations and how to correct them

### Lecture 30: Interface Segregation Principle
- Defining Interface Segregation Principle (ISP)
- The importance of creating fine-grained interfaces
- Implementing ISP to avoid unnecessary dependencies in code

### Lecture 31: Dependency Inversion Principle
- Exploring Dependency Inversion Principle (DIP)
- Techniques for decoupling software modules
- Examples of inversion of control and dependency injection

## Part III: Final Project - Chess Game Development Using SOLID Principles

### Project Overview
This final project series dives deep into the application of SOLID principles in a practical object-oriented programming project: building a Chess game. We will provide not only the foundational aspects of the SOLID principles but also how to apply them in a complex software development project.

### Lecture 32: Introduction and Setup
- Introduction to the Chess game project.
- Overview of SOLID principles.
- Setting up the development environment.
- High-level architecture planning for the Chess game.

### Lecture 33: Single Responsibility Principle (SRP)
- Designing the `ChessPiece` class to handle specific piece behaviors.
- Creating separate classes for managing the game board (`GameBoard`) and game state (`GameState`).

### Lecture 34: Open/Closed Principle (OCP)
- Demonstrating how to extend the game functionality with new types of chess pieces without altering existing code.
- Supporting different rule sets through subclassing and polymorphism.

### Lecture 35: Liskov Substitution Principle (LSP)
- Ensuring that subclasses of `ChessPiece` can be replaced with their parent class without affecting game integrity.
- Practical examples of applying LSP with chess pieces and game rules.

### Lecture 36: Interface Segregation Principle (ISP)
- Defining narrow interfaces for different types of piece movements and game interactions.
- How to separate concerns effectively using interfaces to simplify dependencies.

### Lecture 37: Dependency Inversion Principle (DIP)
- Decoupling high-level game logic from low-level implementation details.
- Implementing dependency injection for game configuration and dynamic behavior management.

### Lecture 38: Implementing Basic Game Logic and User Interface
- Coding session for implementing the core game mechanics such as piece movement and turn management.
- Developing a basic user interface, whether textual or graphical.

### Lecture 39: Advanced Features and Game Rules
- Integrating special moves like castling, en passant, and pawn promotion.
- Adding features like game history tracking, undo functionality, and save/load game states.

### Lecture 40: Testing, Debugging, and Refinement
- Effective testing strategies for object-oriented projects.
- Debugging techniques focusing on common issues in complex system designs.
- Refining the codebase based on test outcomes and feedback.

### Lecture 41: Project Review and Extensions
- Comprehensive review of how each SOLID principle was implemented throughout the project.
- Discussion on potential improvements and extensions such as adding AI opponents or online multiplayer features.
- Collecting and incorporating feedback to enhance the project.

## How to Use These Materials
Each folder in this repository corresponds to one lecture. Inside, you'll find lecture notes, supplementary materials, and code examples. Clone this repository to get started:

```bash
git clone [URL-of-this-repository]
