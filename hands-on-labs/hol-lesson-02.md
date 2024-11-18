# 🛠️ Hands-On Lab: Writing Effective Prompts for GitHub Copilot

![GitHub Copilot Badge](https://img.shields.io/badge/GitHub-Copilot-blue?style=flat-square&logo=github)

> **Module Reference**  
> This lab corresponds to **Lesson 2: Writing Prompts for Copilot** from the course curriculum.

**Duration**: 15 minutes

## 🎯 Objectives

By the end of this lab, you will:
- Learn the anatomy of an effective Copilot prompt
- Practice writing prompts that generate accurate code
- Understand how to iterate and refine prompts for better results

## Prerequisites

- GitHub Copilot installed and activated in VS Code
- Basic programming knowledge in any language

## 🔨 Exercises

### Exercise 1: The Prompt Pyramid (5 minutes)

Let's see how different levels of detail in prompts affect Copilot's output.

1. Create a new file called `user_validation.py` (or `.js`/`.java` if you prefer)

2. Try these prompts in order, and observe how Copilot's suggestions improve:

   **Basic Prompt:**
   ```python
   # validate email
   ```

   **Better Prompt:**
   ```python
   # function to validate email format
   ```

   **Best Prompt:**
   ```python
   # function validateEmail that checks:
   # - contains @ and at least one dot
   # - no spaces allowed
   # - minimum length of 5 characters
   # returns true if valid, false otherwise
   ```

💡 **Discussion**: Notice how each prompt provides more context and requirements, leading to more accurate suggestions.

### Exercise 2: Prompt Patterns (5 minutes)

Practice these effective prompt patterns:

1. Create a new file called `data_transformer.py`

2. Try writing a prompt using each pattern:

   **Input/Output Pattern:**
   ```python
   # input: array of numbers [1,2,3,4,5]
   # output: sum of squares [1,4,9,16,25]
   # function name: squareNumbers
   ```

   **Example-Based Pattern:**
   ```python
   # function convertTime that changes 24h to 12h format
   # example: 14:30 -> 2:30 PM
   # example: 08:15 -> 8:15 AM
   # example: 00:30 -> 12:30 AM
   ```

### Exercise 3: Refining Prompts (5 minutes)

Sometimes your first prompt won't give you exactly what you want. Let's practice refining:

1. Start with this prompt:
   ```python
   # generate password
   ```

2. Refine it gradually:
   ```python
   # generate secure password
   ```
   
   ```python
   # generate secure password with:
   # - minimum 12 characters
   # - at least 1 uppercase, 1 lowercase
   # - at least 1 number and 1 special character
   ```

## 🎉 Success Criteria

You've completed this lab when you:
- ✅ Successfully generated code using all three levels of prompts in Exercise 1
- ✅ Created functions using both prompt patterns in Exercise 2
- ✅ Practiced prompt refinement in Exercise 3

## 💡 Tips

- Be specific about function names, parameters, and return values
- Include examples when the behavior isn't obvious
- Use clear formatting in your prompts (bullet points, new lines)
- If you don't like Copilot's first suggestion, try refining your prompt

## 🤔 Reflection Questions

1. Which prompt pattern worked best for you?
2. How did the level of detail in your prompts affect Copilot's output?
3. What differences did you notice between your initial and refined prompts?

---

Next: [Lesson 3: Advanced Copilot Features](./hol-lesson-03.md)

