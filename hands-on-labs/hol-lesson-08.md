# 🛠️ Hands-On Lab: Advanced Copilot Techniques

![GitHub Copilot Badge](https://img.shields.io/badge/GitHub-Copilot-blue?style=flat-square&logo=github)

> **Module Reference**  
> This lab corresponds to **Lesson 8: Advanced Copilot Techniques** from the course curriculum.

**Duration**: 15 minutes

## 🎯 Objectives

By the end of this lab, you will:
- Master Copilot's slash commands
- Use Copilot Chat effectively in the editor
- Learn to work with Copilot's context awareness

## Prerequisites

- GitHub Copilot and Copilot Chat installed in VS Code
- Basic familiarity with Copilot's core features

## 🔨 Exercises

### Exercise 1: Mastering Slash Commands (5 minutes)

1. Open VS Code and create a new file called `advanced_features.py`

2. Try these slash commands in the Copilot Chat panel:
   ```
   /explain - Get detailed code explanations
   /tests - Generate unit tests
   /fix - Get help fixing code issues
   /docs - Generate documentation
   ```

3. Practice with this code:
   ```python
   def process_data(items):
       return [x for x in items if isinstance(x, (int, float)) and x > 0]
   ```

   Try:
   ```
   /explain process_data
   /tests process_data
   /docs process_data
   ```

### Exercise 2: Context-Aware Coding (5 minutes)

1. Create a new file with dependencies:
   ```python
   import pandas as pd
   import numpy as np
   ```

2. Use Copilot Chat to understand context:
   ```
   /explain what libraries are available in this file?
   ```

3. Ask for context-aware suggestions:
   ```python
   # Create a function that:
   # - reads a CSV file
   # - filters rows where 'age' > 25
   # - calculates mean salary by department
   # using the imported libraries
   ```

### Exercise 3: Working with Copilot Agents (5 minutes)

1. Try different agent personas:
   ```
   @workspace - For workspace-specific questions
   @terminal - For terminal commands
   @vscode - For VS Code-specific features
   ```

2. Practice agent interactions:
   ```
   @workspace What files contain TODO comments?
   @terminal How do I find large files in this directory?
   @vscode What extensions are recommended for this project?
   ```

## 🎉 Success Criteria

You've completed this lab when you:
- ✅ Successfully used at least 3 different slash commands
- ✅ Created context-aware code with Copilot
- ✅ Interacted with different Copilot agents

## 💡 Tips

- Use natural language in your interactions with Copilot Chat
- Combine slash commands for better results
- Pay attention to Copilot's context understanding
- Use agents for specialized tasks

## 🤔 Reflection Questions

1. How do slash commands enhance your coding workflow?
2. When are different agents most useful?
3. How does context awareness improve Copilot's suggestions?

---

Next: [Lesson 9: Testing with Copilot](./hol-lesson-09.md) 