import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import MySQLConnection

load_dotenv()


class Database:
    """
    A class to manage the connection to the MySQL database using configuration from environment variables.

    Attributes:
    -----------
    config : dict
        The database connection parameters like user, password, host, and database name.
    """

    def __init__(self) -> None:
        self.config = {
            "user": os.environ.get("DB_USER"),
            "password": os.environ.get("DB_PASSWORD"),
            "host": os.environ.get("DB_HOST"),
            "database": os.environ.get("DB_NAME"),
        }

    def connect(self) -> MySQLConnection:
        """
        Establish a connection to the MySQL database.

        Returns:
        --------
        MySQLConnection
            A connection object for interacting with the MySQL database.

        Raises:
        -------
        mysql.connector.Error
            If the connection to the database fails.
        """
        return mysql.connector.connect(**self.config)


class ChatDatabase:
    """
    A class to manage chat-related database operations, such as creating tables,
    inserting chat history, and retrieving chat data.

    Attributes:
    -----------
    db : Database
        An instance of the `Database` class for establishing connections to the MySQL database.
    """

    def __init__(self, db: Database) -> None:
        self.db = db

    def create_tables(self) -> None:
        """
        Create the necessary tables for chat history and chat data in the database.
        If the tables already exist, they will not be created again.

        Raises:
        -------
        mysql.connector.Error
            If there is any error executing the SQL statements.
        """
        conn = self.db.connect()
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

        cursor.execute("DROP TRIGGER IF EXISTS update_is_stream")

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
        cursor.close()
        conn.close()

    def insert_chat_history(self, start_time: str, is_stream: int) -> None:
        """
        Insert a new chat history record into the database.

        Parameters:
        -----------
        start_time : str
            The starting time of the chat session.
        is_stream : int
            An integer indicating whether the chat is in progress (1) or ended (2).

        Raises:
        -------
        mysql.connector.Error
            If there is any error executing the SQL statements.
        """
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO ChatDB.Chat_history (start_time, is_stream)
            VALUES (%s, %s)
        """,
            (start_time, is_stream),
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_latest_chat_id(self) -> int:
        """
        Retrieve the chat ID of the most recent chat session from the database.

        Returns:
        --------
        int
            The ID of the latest chat session.

        Raises:
        -------
        mysql.connector.Error
            If there is any error executing the SQL statements.
        """
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT chat_id FROM ChatDB.Chat_history WHERE
            chat_id=(SELECT MAX(chat_id) FROM ChatDB.Chat_history)
        """
        )
        chat_id_pk = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return chat_id_pk

    def insert_chat_data(
        self, chat_id: int, user_message: str, assistant_message: str
    ) -> None:
        """
        Insert a new chat data record into the database.

        Parameters:
        -----------
        chat_id : int
            The ID of the chat session to which this data belongs.
        user_message : str
            The message provided by the user in the chat session.
        assistant_message : str
            The response from the assistant in the chat session.

        Raises:
        -------
        mysql.connector.Error
            If there is any error executing the SQL statements.
        """
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO ChatDB.Chat_data (chat_id, user, assistant)
            VALUES (%s, %s, %s)
        """,
            (chat_id, user_message, assistant_message),
        )
        conn.commit()
        cursor.close()
        conn.close()
