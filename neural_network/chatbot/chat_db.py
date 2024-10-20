"""
credits : https://medium.com/google-developer-experts/beyond-live-sessions-building-persistent-memory-chatbots-with-langchain-gemini-pro-and-firebase-19d6f84e21d3
"""

import os
import datetime
import mysql.connector
from dotenv import load_dotenv
from together import Together
from groq import Groq
import unittest
from unittest.mock import patch
from io import StringIO

load_dotenv()

# Database configuration
db_config = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "host": os.environ.get("DB_HOST"),
    "database": os.environ.get("DB_NAME"),
}


class LLMService:
    def __init__(self, api_service: str):
        self.api_service = api_service
        if self.api_service == "Together":
            self.client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
        else:
            self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    def generate_response(self, conversation_history: list[dict]) -> str:
        """
        Generate a response from the LLM based on the conversation history.

        Example:
        >>> llm_service = LLMService(api_service="Groq")
        >>> response = llm_service.generate_response([{"role": "user", "content": "Hello"}])
        >>> isinstance(response, str)
        True
        """
        if self.api_service == "Together":
            response = self.client.chat.completions.create(
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
        else:
            response = self.client.chat.completions.create(
                model="llama3-8b-8192",
                messages=conversation_history,
                max_tokens=1024,
                temperature=0.3,
                top_p=0.7,
                stop=["<|eot_id|>", "<|eom_id|>"],
                stream=False,
            )

        return response.choices[0].message.content


class ChatDB:
    @staticmethod
    def create_tables() -> None:
        """
        Create the ChatDB.Chat_history and ChatDB.Chat_data tables
        if they do not exist. Also, create a trigger to update is_stream
        in Chat_data when Chat_history.is_stream is updated.

        Example:
        >>> ChatDB.create_tables()
        Tables and trigger created successfully
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
            print("Tables and trigger created successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def insert_chat_history(start_time: datetime.datetime, is_stream: int) -> int:
        """
        Insert a new row into the ChatDB.Chat_history table and return the inserted chat_id.

        Example:
        >>> from datetime import datetime
        >>> chat_id = ChatDB.insert_chat_history(datetime(2024, 1, 1, 12, 0, 0), 1)
        >>> isinstance(chat_id, int)
        True
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
            cursor.execute("SELECT LAST_INSERT_ID()")
            chat_id = cursor.fetchone()[0]
            print("Chat history inserted successfully.")
            return chat_id
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_latest_chat_id() -> int:
        """
        Retrieve the latest chat_id from the ChatDB.Chat_history table.
        :return: The latest chat_id or None if no chat_id exists.

        Example:
        >>> chat_id = ChatDB.get_latest_chat_id()
        >>> isinstance(chat_id, int)
        True
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
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def insert_chat_data(
        chat_id: int, user_message: str, assistant_message: str
    ) -> None:
        """
        Insert a new row into the ChatDB.Chat_data table.

        Example:
        >>> ChatDB.insert_chat_data(1, 'Hello', 'Hi there!')
        Chat data inserted successfully.
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
            print("Chat data inserted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()


class Chatbot:
    def __init__(self, api_service: str):
        self.llm_service = LLMService(api_service)
        self.conversation_history = []
        self.chat_id_pk = None
        self.start_time = datetime.datetime.now(datetime.timezone.utc)

    def chat_session(self) -> None:
        """
        Start a chatbot session, allowing the user to interact with the LLM.
        Saves conversation history in the database and ends the session on "/stop" command.

        Example:
        >>> chatbot = Chatbot(api_service="Groq")
        >>> chatbot.chat_session()  # This will be mocked in the tests
        Welcome to the chatbot! Type '/stop' to end the conversation.
        """
        print("Welcome to the chatbot! Type '/stop' to end the conversation.")

        while True:
            user_input = input("\nYou: ").strip()
            self.conversation_history.append({"role": "user", "content": user_input})

            if self.chat_id_pk is None:
                if user_input.lower() == "/stop":
                    break
                bot_response = self.llm_service.generate_response(
                    self.conversation_history
                )
                self.conversation_history.append(
                    {"role": "assistant", "content": bot_response}
                )

                is_stream = 1  # New conversation
                self.chat_id_pk = ChatDB.insert_chat_history(
                    self.start_time, is_stream
                )  # Return the chat_id
                if self.chat_id_pk:
                    ChatDB.insert_chat_data(self.chat_id_pk, user_input, bot_response)
            else:
                if user_input.lower() == "/stop":
                    is_stream = 2  # End of conversation
                    current_time = datetime.datetime.now(datetime.timezone.utc)
                    ChatDB.insert_chat_history(current_time, is_stream)
                    break

                bot_response = self.llm_service.generate_response(
                    self.conversation_history
                )
                self.conversation_history.append(
                    {"role": "assistant", "content": bot_response}
                )

                is_stream = 0  # Continuation of conversation
                current_time = datetime.datetime.now(datetime.timezone.utc)
                ChatDB.insert_chat_history(current_time, is_stream)
                ChatDB.insert_chat_data(self.chat_id_pk, user_input, bot_response)

            if len(self.conversation_history) > 1000:
                self.conversation_history = self.conversation_history[-3:]


# Test cases for Chatbot
class TestChatbot(unittest.TestCase):
    @patch("builtins.input", side_effect=["Hello", "/stop"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_chat_session(self, mock_stdout, mock_input):
        """
        Test the chat_session method for expected welcome message.
        """
        chatbot = Chatbot(api_service="Groq")
        chatbot.chat_session()

        # Check for the welcome message in the output
        output = mock_stdout.getvalue().strip().splitlines()
        self.assertIn(
            "Welcome to the chatbot! Type '/stop' to end the conversation.", output
        )
        self.assertTrue(
            any("Chat history inserted successfully." in line for line in output)
        )
        self.assertTrue(
            any("Chat data inserted successfully." in line for line in output)
        )


if __name__ == "__main__":
    #
    ChatDB.create_tables()
    unittest.main()
