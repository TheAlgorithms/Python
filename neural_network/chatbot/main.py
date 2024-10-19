from db import Database, ChatDatabase
from llm_service import LLMService
from chatbot import Chatbot
from typing import NoReturn


def main() -> NoReturn:
    """
    Main function to initialize and start the chatbot application.

    This function initializes the database and LLM service, creates necessary tables, and starts
    the chatbot for user interaction.
    """
    # Initialize and configure the database
    db = Database()
    chat_db = ChatDatabase(db)
    chat_db.create_tables()

    # Set the API service to either "Together" or "Groq"
    api_service = (
        "Groq"  # Can be set dynamically based on user preference or environment
    )
    llm_service = LLMService(api_service)

    # Initialize the Chatbot with the database and LLM service
    chatbot = Chatbot(chat_db, llm_service)

    print("Welcome to the chatbot! Type '/stop' to end the conversation.")
    chatbot.start_chat()

    # Chat loop to handle user input
    while True:
        user_input = input("\nYou: ")
        if user_input.strip().lower() == "/stop":
            chatbot.end_chat()  # End the conversation if user types "/stop"
            break
        chatbot.handle_user_message(
            user_input
        )  # Process user input and generate response
        chatbot.continue_chat()  # Handle long conversations (trim history if necessary)


if __name__ == "__main__":
    main()
