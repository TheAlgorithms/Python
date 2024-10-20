"""
credits : https://medium.com/google-developer-experts/beyond-live-sessions-building-persistent-memory-chatbots-with-langchain-gemini-pro-and-firebase-19d6f84e21d3

"""

import os
import datetime
from dotenv import load_dotenv
import mysql.connector
from together import Together
from groq import Groq

load_dotenv()

# Database configuration
db_config = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "host": os.environ.get("DB_HOST"),
    "database": os.environ.get("DB_NAME"),
}

api_service = os.environ.get("API_SERVICE")


def create_tables() -> None:
    """
    Create the ChatDB.Chat_history and ChatDB.Chat_data tables
    if they do not exist.Also, create a trigger to update is_stream
    in Chat_data when Chat_history.is_stream is updated.
    """
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS ChatDB.Chat_history (
            chat_id INT AUTO_INCREMENT PRIMARY KEY,
            start_time DATETIME,
            is_stream INT
        )
        """
        )

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS ChatDB.Chat_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            chat_id INT,
            user TEXT,
            assistant TEXT,
            FOREIGN KEY (chat_id) REFERENCES ChatDB.Chat_history(chat_id)
        )
        """
        )

        cursor.execute("DROP TRIGGER IF EXISTS update_is_stream;")

        cursor.execute(
            """
        CREATE TRIGGER update_is_stream
        AFTER UPDATE ON ChatDB.Chat_history
        FOR EACH ROW
        BEGIN
            UPDATE ChatDB.Chat_data
            SET is_stream = NEW.is_stream
            WHERE chat_id = NEW.chat_id;
        END;
        """
        )

        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()
    print("Tables and trigger created successfully")


def insert_chat_history(start_time: datetime.datetime, is_stream: int) -> None:
    """
    Insert a new row into the ChatDB.Chat_history table.
    :param start_time: Timestamp of when the chat started
    :param is_stream: Indicator of whether the conversation is
                                 ongoing, starting, or ending
    """
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO ChatDB.Chat_history (start_time, is_stream)
            VALUES (%s, %s)
        """,
            (start_time, is_stream),
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()


def get_latest_chat_id() -> int:
    """
    Retrieve the latest chat_id from the ChatDB.Chat_history table.
    :return: The latest chat_id or None if no chat_id exists.
    """
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT chat_id FROM ChatDB.Chat_history
            ORDER BY chat_id DESC LIMIT 1
        """
        )
        chat_id = cursor.fetchone()[0]
        return chat_id if chat_id else None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return 0
    finally:
        cursor.close()
        conn.close()


def insert_chat_data(chat_id: int, user_message: str, assistant_message: str) -> None:
    """
    Insert a new row into the ChatDB.Chat_data table.
    :param chat_id: The ID of the chat session
    :param user_message: The user's message
    :param assistant_message: The assistant's message
    """
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO ChatDB.Chat_data (chat_id, user, assistant)
            VALUES (%s, %s, %s)
        """,
            (chat_id, user_message, assistant_message),
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()


def generate_llm_response(
    conversation_history: list[dict], api_service: str = "Groq"
) -> str:
    """
    Generate a response from the LLM based on the conversation history.
    :param conversation_history: List of dictionaries representing
                                                        the conversation so far
    :param api_service: Choose between "Together" or "Groq" as the
                                        API service
    :return: Assistant's response as a string
    """
    bot_response = ""
    if api_service == "Together":
        client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct-Turbo",
            messages=conversation_history,
            max_tokens=512,
            temperature=0.3,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1,
            stop=["<|eot_id|>", "<|eom_id|>"],
            stream=False,
        )
        bot_response = response.choices[0].message.content
    else:
        client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=conversation_history,
            max_tokens=1024,
            temperature=0.3,
            top_p=0.7,
            stop=["<|eot_id|>", "<|eom_id|>"],
            stream=False,
        )
        bot_response = response.choices[0].message.content

    return bot_response


def chat_session() -> None:
    """
    Start a chatbot session, allowing the user to interact with the LLM.
    Saves conversation history in the database and ends the session on "/stop" command.
    """
    print("Welcome to the chatbot! Type '/stop' to end the conversation.")

    conversation_history = []
    start_time = datetime.datetime.now(datetime.timezone.utc)

    chat_id_pk = None
    api_service = "Groq"  # or "Together"

    while True:
        user_input = input("\nYou: ").strip()
        conversation_history.append({"role": "user", "content": user_input})

        if chat_id_pk is None:
            if user_input.lower() == "/stop":
                break
            bot_response = generate_llm_response(conversation_history, api_service)
            conversation_history.append({"role": "assistant", "content": bot_response})

            is_stream = 1  # New conversation
            insert_chat_history(start_time, is_stream)
            chat_id_pk = get_latest_chat_id()
            insert_chat_data(chat_id_pk, user_input, bot_response)
        else:
            if user_input.lower() == "/stop":
                is_stream = 2  # End of conversation
                current_time = datetime.datetime.now(datetime.timezone.utc)
                insert_chat_history(current_time, is_stream)
                break

            bot_response = generate_llm_response(conversation_history, api_service)
            conversation_history.append({"role": "assistant", "content": bot_response})

            is_stream = 0  # Continuation of conversation
            current_time = datetime.datetime.now(datetime.timezone.utc)
            insert_chat_history(current_time, is_stream)
            insert_chat_data(chat_id_pk, user_input, bot_response)

        if len(conversation_history) > 1000:
            conversation_history = conversation_history[-3:]


# starting a chat session
create_tables()
chat_session()
