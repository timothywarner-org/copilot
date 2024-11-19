# 🛠️ Hands-On Lab: Copilot for Testing

![GitHub Copilot Badge](https://img.shields.io/badge/GitHub-Copilot-blue?style=flat-square&logo=github)

> **Module Reference**  
> This lab corresponds to **Lesson 9: Testing with Copilot** from the course curriculum.

**Duration**: 15 minutes

## 🎯 Objectives

By the end of this lab, you will:
- Generate unit tests using Copilot's /tests command
- Create integration tests with Copilot assistance
- Learn to write test cases for edge cases
- Generate test documentation

## Prerequisites

- GitHub Copilot and Copilot Chat installed
- Basic understanding of testing frameworks (Jest/Mocha/Pytest)
- Node.js or Python installed locally

## 🔨 Exercises

### Exercise 1: Unit Testing with /tests (5 minutes)

1. Create a file called `calculator.js`:
   ```javascript
   class Calculator {
     add(a, b) {
       return a + b;
     }
     
     divide(a, b) {
       if (b === 0) throw new Error('Division by zero');
       return a / b;
     }
   }
   ```

2. Use Copilot's /tests command:
   ```javascript
   // @test Generate comprehensive unit tests for the Calculator class
   // Include edge cases and error scenarios
   ```

3. Try specific test generation:
   ```javascript
   // @test Generate tests for divide() method
   // Cases: normal division, division by zero, floating points
   ```

### Exercise 2: Integration Testing (5 minutes)

1. Create a simple API endpoint:
   ```javascript
   // user-service.js
   class UserService {
     async getUserProfile(id) {
       // Simulated API call
       return { id, name: 'Test User', email: 'test@example.com' };
     }
   }
   ```

2. Ask Copilot to generate integration tests:
   ```javascript
   // @test Generate integration tests for UserService
   // Test API responses, error handling, and data validation
   ```

### Exercise 3: Test Coverage Analysis (5 minutes)

1. Use Copilot to analyze test coverage:
   ```
   /explain What scenarios should be tested for complete coverage?
   ```

2. Generate missing test cases:
   ```javascript
   // @test Generate additional test cases to achieve:
   // - Edge cases
   // - Error scenarios
   // - Boundary conditions
   ```

## 🎉 Success Criteria

You've completed this lab when you:
- ✅ Generated and ran unit tests using /tests
- ✅ Created integration tests for a service
- ✅ Achieved good test coverage with Copilot's help

## 💡 Tips

- Use /tests for quick test generation
- Specify edge cases in your prompts
- Ask Copilot to explain the tests it generates
- Use /fix when tests need improvement

## 🤔 Reflection Questions

1. How does Copilot's test generation compare to manual test writing?
2. What types of tests are easier/harder for Copilot to generate?
3. How can you improve the quality of generated tests?

---

Next: [Lesson 10: Documentation with Copilot](./hol-lesson-10.md) 