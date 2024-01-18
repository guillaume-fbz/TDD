# TDD

## Unit Test and Coverage

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
