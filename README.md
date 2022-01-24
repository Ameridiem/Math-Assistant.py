## Derivative Calculator

### Code Instructions
- Instructions on how to input code are in the menu file
- Enter any number to do something with the program. Menu will show what each number does (eg. start / enter equation, how to type in an equation without the program crashing, quit the program)
- The program will calculate the derivative of the function you typed in while showing the steps for you.

### Audience
- This program was built for AP Math students to have a resource for checking over their work that will show all of the appropriate steps.
- There aren't many programs out there that will do this, so it takes a long time to find mistakes.
- Showing the steps will help students look over their work and to not ponder over what their mistake was for hours.

### Timeline and Program Requirements
- Menu: Nov. 25th
- Function that simplifies common terms: Dec. 15th
- Function that simplifies powers: Jan. 3rd
- Defined function to clean up user-function: Jan. 12th
- Function to simplify brackets: Jan. 16th
- File for at least one derivative calc method: Jan. 20th
- Bug Fixes / Formatting: Jan. 21st
- Alpha / Beta Testing: Jan. 23rd
- Review: Jan. 23rd
### Program Expansion:
- Different deriavite calculating methods (power-rule / quotient rule, chain rule, etc.)
- Dealing with more complex equations
    - sin, cos, tan, arcsin, arccos, arctan
    - variables in the power
    - logarithmic / exponential equations
    - equations involving special constants such as pi or e

### Alpha Testing

#### List
- Every function in equation_symplifyer.py needs Alpha Testing
- Menu needs alpha testing to see if printing and function commands work properly
- Importing simplified function to the chain-rule file needs to be alpha tested to verify that the function is the correct format, data type, and not corrupted
- diff_eq function needs alpha testing to verify that the function is working properly and returning the correct answer.

### 
- January 17th, 2022: Code wouldn't execute properly with most formuals.
    - Using two stars for the power causes the system to not recognize coefficients and / or powers properly.
    - Used Regex Module to look for the two stars (\*\*) and replace with carots (^) and adjusted code accordingly.
- January 19th, 2022: Powers exactly 1 too much when there is a coefficient in front of the power.
    - Defined function was looking for parts\[0], even if parts had more than one item, the power would increase when it shoudln't.
    - Added if statement that looked for if there were more than one element in the list, if there was, the power would decrease by 1.
- January 23rd, 2022: Equation simplifyer doesn't work with coefficients outside of the brackets that are negative.
    - Negatives in front of coefficients created an extra item in the list that had a value of nothing
    - Removed all items in that list with a value of nothing.
### Beta Testing

#### Graham Mandryk
- January 23, 2022: Incorrect funtions such as #%! were being recognized instead of raising a ValueError
    - Added statement saying if the foiled-out function was equal to nothing to raise a ValueError

#### Jordan Mah
- January 23, 2022: Function 3x^20 - (3 + x^2)^3 raised a ValueError
    - ValueError only raised when it's in that order in the brackets.
    - Added parameter that tells the user to change the order of the function
    - With more time, it would be ideal to create a new function that could change the order of every part in brackets from highest power to lowest power so the program can work properly with every type of equation it was supposed to.

#### Marin Nelson:
- January 23, 2022: Program was not clear on how to type equations.
    - Program was originally designed to work with implicit and explicit equations, but coding became too complicated with explicit equations. Needed to update equation_instructions.txt.