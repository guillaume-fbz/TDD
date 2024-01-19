# TDD

## Chapter 1 : Unit Test and Coverage

## Ex1 : Verlan
Implement a function named "verlan" that takes a string as input and returns a new string
with the following modifications:
- Remove leading and trailing whitespaces.
- Reverse the order of characters in the string.
- Convert all characters to lowercase.

For example:\
input: verlan("  Hello World  ")\
output: "dlrow olleh"

## Ex2 : Calculator
Perform basic arithmetic operations based on the given operation.

Implement a function named "calculate" that takes parameters:
  - a: The first operand (number)
  - b: The second operand (number)
  - operation: The arithmetic operation to perform ('+', '-', '*', '/')

Returns:\
 The result of the specified arithmetic operation.\
 If the operation is not one of '+', '-', '*', '/', returns None.\
 If attempting to divide by zero, returns None.

For example:\
  input: calculate(10, 2, '/')\
  output: 5

## Ex3 : Student
Add unit tests on student.py class and then generate a test coverage report using pytest-cov.


## Chapter 2 : TDD

## Ex1 : FizzBuzz Kata
FizzBuzz is a programming challenge. Write a program that prints one line for each number from 1 to 100.\

If the number is a multiple of 3, print "Fizz" instead.\
If the number is a multiple of 5, print "Buzz" instead.\
If the number is a multiple of both 3 and 5, print "FizzBuzz".\
Otherwise, simply print the number itself.\

Source:  https://codingdojo.org/kata/FizzBuzz/

## Ex2 : Mars Rover Kata
You simulate the movement of a rover on Mars given a set of commands.\

Here are the basic rules:\
The Mars Rover is located at a given position on a rectangular grid.\
You can control the rover by sending it a sequence of commands: 'L' (turn left), 'R' (turn right), 'M' (move one step forward).\
The grid is represented as a set of coordinates (x, y).\
The rover has a direction it is facing: North, East, South, or West.\

Source: https://codingdojo.org/kata/mars-rover/

## Chapter 3 : Advanced testing

## Ex1 : TBD Mocking

## Ex2 : TBD FastAPI route
