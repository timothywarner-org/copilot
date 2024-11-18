# Hands-on Lab: Lesson 4 - Refactoring and Debugging with GitHub Copilot

## Overview
In this hands-on lab, you'll learn how to leverage GitHub Copilot to refactor code and debug issues efficiently. You'll work with real-world examples and learn techniques that can be applied to any programming language.

**Duration**: 15-20 minutes

## Prerequisites
- Visual Studio Code installed
- GitHub Copilot extension installed and authenticated
- GitHub Copilot Chat extension installed
- Basic programming knowledge in any language

## Exercise 1: Understanding Code with Copilot

1. Create a new file called `calculator.js` with this inefficient code:
   ```javascript
   function add(a, b) {
     return a + b;
   }
   
   function subtract(a, b) {
     return a - b;
   }
   
   function multiply(a, b) {
     let result = 0;
     for(let i = 0; i < b; i++) {
       result = add(result, a);
     }
     return result;
   }
   
   function divide(a, b) {
     if(b === 0) {
       return "Error: Division by zero";
     }
     let count = 0;
     let current = a;
     while(current >= b) {
       current = subtract(current, b);
       count = add(count, 1);
     }
     return count;
   }
   ```

2. Open Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)

3. Ask Copilot to analyze the code:
   ```
   /explain What are the inefficiencies in this code?
   ```

## Exercise 2: Refactoring for Efficiency

1. Select the `multiply` function and use inline chat (Ctrl+I / Cmd+I):
   ```
   Make this function more efficient
   ```

2. Select the `divide` function and ask:
   ```
   Optimize this function and add error handling
   ```

3. Review Copilot's suggestions and accept the improvements by clicking "Accept" or pressing Tab.

## Exercise 3: Adding Error Handling and Tests

1. Ask Copilot to add input validation:
   ```
   Add type checking and input validation to all functions
   ```

2. Generate unit tests by typing this comment:
   ```javascript
   // Write comprehensive jest tests for all calculator functions
   ```

## Exercise 4: Debugging with Copilot

1. Add this buggy function to your code:
   ```javascript
   function calculateCompoundInterest(principal, rate, years) {
     const amount = principal * (1 + rate) ^ years;
     return amount - principal;
   }
   ```

2. Ask Copilot to help find the bug:
   ```
   /explain Why isn't this compound interest calculation correct?
   ```

3. Let Copilot suggest the fix:
   ```
   Fix the compound interest calculation
   ```

## Exercise 5: Code Structure Improvement

1. Ask Copilot to organize the code better:
   ```
   Suggest a better structure for this calculator module using classes
   ```

2. Request documentation:
   ```
   Add JSDoc documentation to all functions
   ```

## Challenge Exercise

1. Add this complex function:
   ```javascript
   function processTransactions(transactions) {
     let total = 0;
     for(let i = 0; i < transactions.length; i++) {
       if(transactions[i].type === 'credit') {
         total = total + transactions[i].amount;
       } else if(transactions[i].type === 'debit') {
         total = total - transactions[i].amount;
       }
       if(transactions[i].fee) {
         total = total - transactions[i].fee;
       }
     }
     return total;
   }
   ```

2. Ask Copilot to:
   - Refactor using modern JavaScript features
   - Add error handling
   - Improve performance
   - Add type safety
   - Generate tests

## Tips for Success
- Always review Copilot's suggestions before accepting them
- Use specific prompts for better results
- Combine Copilot Chat with inline suggestions for best results
- Test the refactored code to ensure it maintains the original functionality

## Next Steps
- Experiment with refactoring your own code
- Try these techniques with different programming languages
- Explore more complex refactoring scenarios
- Practice debugging real-world issues

## Additional Resources
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [Refactoring best practices](https://docs.github.com/en/copilot/using-github-copilot/example-use-cases/refactoring-code-with-github-copilot)
