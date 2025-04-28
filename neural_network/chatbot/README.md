

# Chatbot with LLM Integration and Database Storage

This chatbot application integrates LLM (Large Language Model) API services, **Together** and **Groq**(you can use any one of them), to generate AI-driven responses. It stores conversation history in a MySQL database and manages chat sessions with triggers that update the status of conversations automatically.

## Features
- Supports LLM response generation using **Together** and **Groq** APIs.
- Stores chat sessions and message exchanges in MySQL database tables.
- Automatically updates chat session status using database triggers.
- Manages conversation history with user-assistant interaction.

## Requirements

Before running the application, ensure the following dependencies are installed:

- Python 3.13+
- MySQL Server
- The following Python libraries:
  ```bash
  pip3 install -r requirements.txt
  ```

## Setup Instructions

### Step 1: Set Up Environment Variables

Create a `.env` file in the root directory of your project and add the following entries for your database credentials and API keys:

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

# API service to you(or use "Together")
API_SERVICE = "Groq"
```

### Step 2: Create MySQL Tables and Trigger

The `create_tables()` function in the script automatically creates the necessary tables and a trigger for updating chat session statuses. To ensure the database is set up correctly, the function is called at the beginning of the script.

Ensure that your MySQL server is running and accessible before running the code.

### Step 3: Run the Application

To start the chatbot:

1. Ensure your MySQL server is running.
2. Open a terminal and run the Python script:

```bash
python3 chat_db.py
```

The chatbot will initialize, and you can interact with it by typing your inputs. Type `/stop` to end the conversation.

### Step 4: Test and Validate Code

This project uses doctests to ensure that the functions work as expected. To run the doctests:

```bash
python3 -m doctest -v chatbot.py
```

Make sure to add doctests to all your functions where applicable, to validate both valid and erroneous inputs.

### Key Functions

- **create_tables()**: Sets up the MySQL tables (`Chat_history` and `Chat_data`) and the `update_is_stream` trigger.
- **insert_chat_history()**: Inserts a new chat session into the `Chat_history` table.
- **insert_chat_data()**: Inserts user-assistant message pairs into the `Chat_data` table.
- **generate_llm_response()**: Generates a response from the selected LLM API service, either **Together** or **Groq**.

