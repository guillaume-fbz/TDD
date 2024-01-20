# TDD

## Chapter 1 : Unit Test and Coverage

## Ex1 : Verlan
Implement a function named "verlan" that takes a string as input and returns a new string
with the following modifications:
- Remove leading and trailing whitespaces.
- Reverse the order of characters in the string.
- Convert all characters to lowercase.

For example:

     input: verlan("  Hello World  ")
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

For example:

     input: calculate(10, 2, '/')
     output: 5


## Ex3 : Student
Add unit tests on student.py class and then generate a test coverage report using pytest-cov.


## Chapter 2 : TDD

## Ex1 : FizzBuzz Kata
FizzBuzz is a programming challenge. Write a program that prints one line for each number from 1 to 100.\

If the number is a multiple of 3, print "Fizz" instead.\
If the number is a multiple of 5, print "Buzz" instead.\
If the number is a multiple of both 3 and 5, print "FizzBuzz".\
Otherwise, simply print the number itself.

Source:  https://codingdojo.org/kata/FizzBuzz/

## Ex2 : Mars Rover Kata
You simulate the movement of a rover on Mars given a set of commands.

Here are the basic rules:\
The Mars Rover is located at a given position on a rectangular grid.\
You can control the rover by sending it a sequence of commands: 'L' (turn left), 'R' (turn right), 'M' (move one step forward).\
The grid is represented as a set of coordinates (x, y).\
The rover has a direction it is facing: North, East, South, or West.

Source: https://codingdojo.org/kata/mars-rover/

## Ex3 : Roman Numerals Kata
The Romans were a clever bunch. They conquered most of Europe and ruled it for hundreds of years. They invented concrete and straight roads and even bikinis [1].\
One thing they never discovered though was the number zero. This made writing and dating extensive histories of their exploits slightly more challenging, but the system of numbers they came up with is still in use today. \
For example the BBC uses Roman numerals to date their programmes.

The Romans wrote numbers using letters : I, V, X, L, C, D, M. (notice these letters have lots of straight lines and are hence easy to hack into stone tablets)

The Kata says you should write a function to convert from normal numbers to Roman Numerals:

     1 --> I
     10 --> X
     7 --> VII

Source: https://codingdojo.org/kata/RomanNumerals/

## Chapter 3 : Advanced testing

## Ex1 : WeatherNow API

Create an API using FastAPI framework that uses an external weather library to fetch and display the current temperature for a given city. (use weather_service.py file in this repository)

Example :

     input HTTP GET 200 : http://localhost:8080/weather/Valenciennes
     output: HTTP 200 { 'town': 'Valenciennes', 'temperature': 5, 'feeling': 'Cold' }

Rules:

Temperature feeling:\
Cold: Below 10 degrees Celsius\
Moderate: 10 to 20 degrees Celsius\
Warm: 20 to 30 degrees Celsius\
Hot: Above 30 degrees Celsius

In this world, we consider that only three cities exists : Valenciennes, Lille and Paris.

Errors management:

Implement error handling to manage unknown city.

     input: HTTP GET : http://localhost:8080/weather/PalletTown
     output: HTTP 404 NOT_FOUND

Implement error handling to manage exceptions that may occur during the temperature retrieval process.

     input HTTP GET : http://localhost:8080/weather/Valenciennes
     output: HTTP 503 SERVICE_UNAVAILABLE
     
