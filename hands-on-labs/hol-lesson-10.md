# 🛠️ Hands-On Lab: Copilot for Documentation

![GitHub Copilot Badge](https://img.shields.io/badge/GitHub-Copilot-blue?style=flat-square&logo=github)

> **Module Reference**  
> This lab corresponds to **Lesson 10: Documentation with Copilot** from the course curriculum.

**Duration**: 15 minutes

## 🎯 Objectives

By the end of this lab, you will:
- Use Copilot's /docs command for automated documentation
- Generate JSDoc and docstring comments
- Create README files and API documentation
- Learn documentation best practices with AI assistance

## Prerequisites

- GitHub Copilot and Copilot Chat installed
- Basic understanding of documentation formats (JSDoc, docstrings)
- A code project to document

## 🔨 Exercises

### Exercise 1: Code-Level Documentation (5 minutes)

1. Create a file with a complex function:
   ```javascript
   function processUserData(userData, options = {}) {
     const { normalize = true, validate = true } = options;
     const processed = userData.map(user => ({
       ...user,
       name: normalize ? user.name.trim().toLowerCase() : user.name,
       email: validate ? validateEmail(user.email) : user.email
     }));
     return processed.filter(user => user.email !== false);
   }
   ```

2. Use the /docs command:
   ```javascript
   // @docs Generate comprehensive JSDoc for processUserData
   ```

3. Try documenting edge cases:
   ```javascript
   // @docs Include error scenarios and parameter constraints
   ```

### Exercise 2: README Generation (5 minutes)

1. Use Copilot to create a project README:
   ```markdown
   # Project Documentation
   
   <!-- @copilot generate project overview -->
   
   ## Installation
   <!-- @copilot describe setup steps -->
   
   ## Usage
   <!-- @copilot provide usage examples -->
   ```

2. Generate API documentation:
   ```javascript
   // @docs Create API documentation for the following endpoints:
   app.get('/api/users', getUsers);
   app.post('/api/users', createUser);
   app.put('/api/users/:id', updateUser);
   ```

### Exercise 3: Documentation Maintenance (5 minutes)

1. Use Copilot to update existing docs:
   ```javascript
   // @docs Update this documentation to reflect new features:
   /**
    * @deprecated Use processUserData instead
    */
   function oldProcessUser(data) {
     // ...
   }
   ```

2. Generate changelog entries:
   ```markdown
   # Changelog
   
   <!-- @copilot summarize changes from git history -->
   ```

## 🎉 Success Criteria

You've completed this lab when you:
- ✅ Generated comprehensive function documentation
- ✅ Created a complete README file
- ✅ Updated existing documentation
- ✅ Generated API documentation

## 💡 Tips

- Use /docs for quick documentation generation
- Include examples in your documentation prompts
- Ask Copilot to explain complex parts of the documentation
- Use markdown formatting for better readability

## 🤔 Reflection Questions

1. How does AI-assisted documentation compare to manual writing?
2. What types of documentation are best suited for Copilot?
3. How can you ensure generated documentation stays accurate?

---

Next: [Lesson 11: Copilot Best Practices](./hol-lesson-11.md) 