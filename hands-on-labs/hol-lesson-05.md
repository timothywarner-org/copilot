# Hands-on Lab: Lesson 5 - Building a Web Application with GitHub Copilot

## Overview
In this hands-on lab, you'll use GitHub Copilot to build a Node.js web application from scratch. You'll learn how Copilot can accelerate your development workflow by suggesting code, helping with implementation details, and assisting with common web development tasks.

**Duration**: 15-20 minutes

## Prerequisites
- Visual Studio Code installed
- GitHub Copilot extension installed and authenticated
- Node.js installed on your system
- Basic knowledge of JavaScript/Node.js

## Exercise 1: Project Setup with Copilot

1. Create a new directory for your project and open it in VS Code

2. Initialize a new Node.js project by typing this comment:
   ```javascript
   // Initialize a new Node.js project with Express and required dependencies
   ```

3. Let Copilot help create your `package.json`. Type:
   ```javascript
   // Create a package.json with Express, body-parser, and cors dependencies
   ```

4. Create a new file called `server.js` and type:
   ```javascript
   // Create an Express server with basic middleware and error handling
   ```

## Exercise 2: Building Core Components

1. Create a basic Express server structure:
   ```javascript
   // Create an Express server that listens on port 3000
   ```

2. Add middleware setup by commenting:
   ```javascript
   // Add middleware for parsing JSON, CORS, and logging requests
   ```

3. Create a tasks route file `routes/tasks.js`:
   ```javascript
   // Create Express router for handling task CRUD operations
   ```

## Exercise 3: Implementing Task Management

1. Create a task model in `models/task.js`:
   ```javascript
   // Create a Task class with id, title, description, and status properties
   ```

2. Implement task operations in your route file:
   ```javascript
   // Implement GET all tasks endpoint
   // Implement POST new task endpoint
   // Implement PUT update task endpoint
   // Implement DELETE task endpoint
   ```

## Exercise 4: Error Handling and Validation

1. Add error handling middleware:
   ```javascript
   // Create error handling middleware for Express
   ```

2. Implement input validation:
   ```javascript
   // Add validation for task creation and updates
   ```

## Exercise 5: Testing Your Application

1. Create test cases using Copilot:
   ```javascript
   // Create test cases for task CRUD operations
   ```

2. Test your endpoints using these curl commands (Copilot will help generate them):
   ```bash
   // Generate curl commands to test the API endpoints
   ```

## Challenge Exercises

1. Add user authentication:
   ```javascript
   // Implement JWT authentication for the API
   ```

2. Add data persistence:
   ```javascript
   // Add MongoDB connection and schema for tasks
   ```

## Tips for Success
- Use natural language comments to guide Copilot
- Review and understand the generated code
- Use Copilot Chat for explanations of complex parts
- Combine inline suggestions with chat for best results

## Common Copilot Prompts for Web Development
- "Create an endpoint that..."
- "Add error handling for..."
- "Implement input validation for..."
- "Create a middleware that..."
- "Add documentation for this API endpoint..."

## Next Steps
- Add more features to your application
- Implement a frontend using React or Vue.js
- Add database integration
- Deploy your application
- Add automated tests

## Additional Resources
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [Express.js documentation](https://expressjs.com/)
- [Node.js best practices](https://nodejs.org/en/docs/guides)
