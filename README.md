## FINAL DOCUMENT SUBMISSION : TASK 2 - GENERATE AND PRINT SIMPLE NUMBER PATTERNS

## PROJECT TITLE: Number Pattern Generation Using Loops

## OBJECTIVE:
To develop a Python program that prints a structured number pattern using loops and control
statements.

## DESCRIPTION:
In this task, a Full Number Pyramid pattern is generated. The program uses nested loops to printspaces, ascending numbers, and descending numbers to form a centered pyramid shape.
This demonstrates the use of loop control structures, which are essential for pattern generation.

## WELL-COMMENTED PYTHON CODE:
rows = 5

for i in range(1, rows + 1):
    # Print spaces
    for space in range(rows - i):
        print(" ", end="")

    # Print ascending numbers
    for num in range(1, i + 1):
        print(num, end="")

    # Print descending numbers
    for num in range(i - 1, 0, -1):
        print(num, end="")

    print()

  
## OUTPUT EXPLANATION:
 The program prints the following pattern:
     1
   121
  12321
 1234321
123454321
 • The first loop adds spaces so that the pyramid is centered.
 • The second loop prints ascending numbers (1 to row number).
 • The third loop prints descending numbers (row-1 to 1).
 
 ## CONCLUSION:
 This program successfully demonstrates how nested loops can be used to generate structured number
 patterns.
 It fulfills the task requirements by applying control statements and loop concepts effectively.
