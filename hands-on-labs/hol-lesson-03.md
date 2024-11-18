# Hands-on Lab: Lesson 3 - Generating Code with GitHub Copilot

## Objectives
In this lab, you will:
- Learn how to use GitHub Copilot in VS Code
- Generate a basic application using Copilot suggestions
- Explore Copilot Chat features
- Practice common Copilot commands and interactions

## Prerequisites
- Visual Studio Code installed
- GitHub Copilot extension installed and authenticated
- GitHub Copilot Chat extension installed

## Exercise 1: Setting Up Your Project

1. Open Visual Studio Code
2. Create a new folder for your project
3. Open the Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
4. Type "Copilot" to see available Copilot commands

## Exercise 2: Using Copilot Chat

1. Open Copilot Chat in VS Code using one of these methods:
   - Click the Copilot Chat icon in the sidebar
   - Use the keyboard shortcut (Ctrl+Shift+I / Cmd+Shift+I)
   - Open Command Palette and type "Copilot Chat"

2. Try these example prompts in Copilot Chat:
   ```
   /help - View available commands
   /explain - Get explanations about code
   /tests - Generate unit tests
   /fix - Fix issues in your code
   ```

## Exercise 3: Generating a Basic Application

1. Create a new file called `app.js`

2. Type this comment at the top of your file:
   ```javascript
   // Create a simple Express.js web server that serves a "Hello, World!" message
   ```

3. Watch as Copilot suggests the complete application code. Press Tab to accept suggestions.

4. Try adding these comments to generate more code:
   ```javascript
   // Add a route for /about that returns JSON with app information
   
   // Create a middleware that logs all incoming requests
   
   // Add error handling middleware
   ```

## Exercise 4: Refining Code with Copilot

1. Use inline suggestions:
   - Start typing a function name
   - Wait for Copilot's suggestion
   - Press Tab to accept or use arrow keys to navigate suggestions

2. Use Copilot Chat to improve your code:
   ```
   "How can I make this code more efficient?"
   "What security considerations should I add?"
   "Can you suggest some error handling improvements?"
   ```

## Exercise 5: Challenge

Using Copilot, create:
1. A basic REST API endpoint
2. Input validation
3. Connection to a database (MongoDB or SQLite)
4. Basic CRUD operations

## Tips for Success
- Be specific in your comments and prompts
- Use natural language to describe what you want
- Experiment with different ways of asking
- Review and understand the generated code
- Don't accept suggestions blindly - verify the code meets your needs

## Next Steps
- Explore more Copilot features
- Practice generating different types of applications
- Try more complex scenarios
- Experiment with different programming languages

## Additional Resources
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot documentation](https://docs.github.com/en/copilot/getting-started-with-github-copilot/getting-started-with-github-copilot-in-visual-studio-code)
