# Chatbot with Chat history stored in Database

This project is a simple chatbot application built using Python, integrating a database for chat history storage and a language model service to generate responses. The chatbot can handle user messages, manage chat history, and terminate conversations upon receiving a `/stop` command.

## Features
- **Conversation Handling**: The bot processes user inputs and generates responses using a language model service.
- **Database Integration**: Stores chat data (user messages and bot responses) and maintains chat history.
- **Session Management**: Supports starting and terminating chat sessions, including proper logging of start and end times.
- **Message Truncation**: Limits conversation history to the last few messages if the conversation exceeds a large number of entries.

## Components
- **`Chatbot` Class**: Core logic for handling user messages and managing the chat lifecycle.
- **`Database` (Mocked in tests)**: Handles chat data storage (methods for inserting and retrieving data).
- **`LLM Service` (Mocked in tests)**: Generates responses to user input based on conversation history.

## Installation
1. Clone the repository:
2. Install the necessary dependencies
   ```bash
   pip3 install requirements.txt
   ```
4. Run the bot or test it using `doctest`:
    ```bash
    python3 -m doctest -v chatbot.py
    ```

## Usage
1. **Create Database**: Create a databse named `ChatDB` in Mysql
2. **Create .env**:
```
  # Together API key
  TOGETHER_API_KEY="YOUR_API_KEY"
  
  # Groq API key
  GROQ_API_KEY = "YOUR_API_KEY"
  
  # MySQL connectionDB (if you're running locally)
  DB_USER = "<DB_USER_NAME>"
  DB_PASSWORD = "<DB_USER_NAME>"
  DB_HOST = "127.0.0.1"
  DB_NAME = "ChatDB"
  PORT = "3306"
 ```
7. **Handling Messages**: run below command to start the chat in console, you can login to your Database to check the chat history
```python
python3 main.py
```
10. **Ending the Chat**: When the user sends `/stop`, the chat will terminate and log the end of the conversation with the message 'conversation-terminated'

## Testing
The code includes basic `doctests` to verify the chatbot's functionality using mock services for the database and language model:
- Run the tests:
    ```bash
    python3 -m doctest -v chatbot.py
    ```
