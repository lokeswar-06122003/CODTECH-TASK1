# CODTECH-TASK1

#Name:- P.Lokeswar

#Company:-CODTECH IT SOLUTIONS

#ID:-CT04DS7476

#Domain:- Python Programming

#Duration:-August to September 2024

#Mentor:-Neela Santhosh Kumar

#Overview of the project:-
This Python project is a **multi-number calculator** that can handle arithmetic operations (addition, subtraction, multiplication, and division) for a user-defined number of inputs.

Key Components:

1. Arithmetic Functions:
   - The project defines four core functions: `add`, `subtract`, `multiply`, and `divide`. Each function operates on a list of numbers and returns the result.
     - add(numbers): Returns the sum of all numbers in the list.
     - subtract(numbers): Starts with the first number and subtracts each subsequent number from it.
     - multiply(numbers): Multiplies all numbers together.
     - divide(numbers): Divides the first number by each subsequent number, checking for division by zero.
2. User Input:
   - The program interacts with the user through the console, prompting them to:
     - Select an arithmetic operation.
     - Specify how many numbers they want to use in the calculation.
     - Input the numbers themselves.

3. Choice and Error Handling:
   - Operation Choice: The user selects an operation by entering the corresponding number (1 for addition, 2 for subtraction, etc.).
   - Invalid Input: If the user selects an invalid option, a message is displayed, and the calculation is not performed.
   - Division by Zero: If the user tries to divide by zero, an error message is shown to prevent the operation from crashing.

4. Main Calculator Function:
   - The `calculator()` function is the main logic that:
     - Presents the user with the available operations.
     - Gathers the numbers to perform calculations on.
     - Calls the relevant arithmetic function based on the user's choice and prints the result.

5. Looping Through Input:
   - For each calculation, the user is asked to input multiple numbers, and these numbers are stored in a list. The chosen function is then applied to this list.
This design allows the calculator to handle any number of input values for each operation, making it versatile and scalable for multi-digit calculations.

![Screenshot 2024-09-09 191051](https://github.com/user-attachments/assets/dcbd1be9-0c36-4aa1-91d0-77ac887795ed)

