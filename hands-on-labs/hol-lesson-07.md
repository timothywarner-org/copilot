# 🛠️ Hands-On Lab: Mastering GitHub Copilot for Code Reviews

![GitHub Copilot Badge](https://img.shields.io/badge/GitHub-Copilot-blue?style=flat-square&logo=github)

> **Module Reference**  
> This lab corresponds to **Lesson 7: Code Reviews with Copilot** from the course curriculum.

**Duration**: 15 minutes

## 🎯 Objectives

By the end of this lab, you will:
- Learn how to leverage Copilot during code reviews
- Practice identifying code improvements using AI assistance
- Master the art of AI-assisted code documentation

## Prerequisites

- GitHub Copilot installed and activated in VS Code
- Basic understanding of code review processes
- A local repository with a sample JavaScript project

## 🔨 Exercises

### Exercise 1: Setting Up for AI-Assisted Review (3 minutes)

1. Clone the sample repository:
   ```bash
   git clone https://github.com/example/sample-js-project.git
   cd sample-js-project
   ```

2. Open in VS Code and verify Copilot is active

### Exercise 2: Using Copilot for Code Analysis (5 minutes)

1. Open a key JavaScript file and add this prompt:
   ```javascript
   // Review the following code for potential improvements:
   function calculateTotal(items) {
     let total = 0;
     for(let i = 0; i < items.length; i++) {
       total = total + items[i].price;
     }
     return total;
   }
   ```

2. Try different review prompts:
   ```javascript
   // Suggest performance improvements for this function
   // Identify potential edge cases in this code
   // How can we make this more maintainable?
   ```

### Exercise 3: Refactoring with Copilot (7 minutes)

1. Practice refactoring suggestions:
   ```javascript
   // Refactor this function to use modern JavaScript features:
   function getFullName(user) {
     var firstName = user.firstName || '';
     var lastName = user.lastName || '';
     return firstName + ' ' + lastName;
   }
   ```

2. Document your changes:
   ```javascript
   // Generate JSDoc comments for the refactored function
   ```

## 🎉 Success Criteria

You've completed this lab when you:
- ✅ Successfully used Copilot to analyze existing code
- ✅ Generated and implemented improvement suggestions
- ✅ Created clear documentation for your changes

## 💡 Tips

- Use specific, detailed prompts for better suggestions
- Always validate Copilot's recommendations
- Combine Copilot's suggestions with your own expertise
- Document significant changes thoroughly

## 🤔 Reflection Questions

1. How did Copilot's suggestions compare to traditional code review practices?
2. Which types of prompts generated the most useful responses?
3. What are the limitations you discovered when using Copilot for code review?

---

Next: [Lesson 8: Advanced Copilot Techniques](./hol-lesson-08.md)