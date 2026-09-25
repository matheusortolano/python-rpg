# ⚔️ Python RPG

Simple terminal-based RPG developed in Python as a practical study project focused on programming logic and Object-Oriented Programming.

The project was gradually refactored as new Python and OOP concepts were learned and applied.

---

## Features

- Character creation
- Choice between Warrior, Mage and Archer
- Battle system
- Character status visualization
- Escape attempt with random success chance
- Victory and defeat system
- Invalid input handling

---

## Concepts Practiced

The project was used to practice:

- variables;
- conditional structures;
- loops;
- functions;
- exception handling with `try` / `except`;
- Python's `random` module;
- classes and objects;
- inheritance;
- abstraction;
- encapsulation;
- polymorphism;
- method overriding;
- use of `super()`;
- properties and setters;
- project organization using modules.

---

## Character Structure

The game uses an object-oriented character hierarchy.

```text
Personagem
├── Guerreiro
├── Mago
├── Arqueiro
└── Inimigo
```

### `Personagem`

Base abstract class used to define common character behavior and attributes.

### `Guerreiro`

Represents the Warrior character class.

### `Mago`

Represents the Mage character class.

### `Arqueiro`

Represents the Archer character class.

### `Inimigo`

Represents enemy characters used during battles.

Each playable character class has its own attributes and implements its own attack behavior.

---

## Object-Oriented Programming

The project applies several OOP concepts.

### Inheritance

Playable characters inherit common behavior from the base character class.

This reduces duplicated code and allows shared attributes and methods to remain centralized.

### Abstraction

The `Personagem` class defines the general structure expected from the character types.

Specific classes are responsible for implementing their own behavior.

### Encapsulation

Character state and attributes are managed through the class structure instead of being handled directly throughout the application.

### Polymorphism

Different character types can implement the same operations in different ways.

For example, each class can provide its own attack implementation while using a common interface.

### Method Overriding

Child classes override methods inherited from the base class when specific behavior is required.

### `super()`

The project uses `super()` to reuse initialization or behavior from parent classes.

### Properties and Setters

Properties and setters are used to control access and updates to object attributes where appropriate.

---

## Battle System

The battle flow allows the player to interact with enemies through terminal commands.

Typical actions include:

- attacking;
- checking character status;
- attempting to escape;
- continuing the battle until victory or defeat.

Random behavior is used in some game mechanics, including escape attempts.

---

## Input Validation

The application includes handling for invalid user input.

`try` / `except` blocks and validation rules are used to prevent unexpected input from immediately interrupting the game.

---

## Project Organization

The code is separated into modules to practice better project structure and organization.

This approach helps separate responsibilities and makes the code easier to maintain as the project grows.

---

## Project Purpose

Python RPG was created as a study project to move beyond isolated exercises and apply multiple Python concepts in a single application.

The project helped reinforce:

- programming logic;
- Python syntax;
- functions;
- error handling;
- modularization;
- Object-Oriented Programming;
- code refactoring.

---

## Project Evolution

The project was not created as a finished game from the beginning.

It evolved progressively as new programming concepts were studied.

The code was refactored over time to introduce concepts such as:

```text
Functions
    ↓
Classes and Objects
    ↓
Inheritance
    ↓
Abstraction
    ↓
Encapsulation
    ↓
Polymorphism
    ↓
Properties and Setters
    ↓
Modular Project Structure
```

This evolution reflects the learning process behind the project.

---

## Tech Stack

- Python
- Python Standard Library
- Terminal / CLI

---

## Project Status

Study project completed and available for future improvements.

Possible future additions could include:

- more character classes;
- additional enemies;
- inventory system;
- items and equipment;
- experience and leveling;
- save system;
- more complex combat mechanics.