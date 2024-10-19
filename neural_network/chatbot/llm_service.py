import os
from together import Together
from groq import Groq
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()


class LLMService:
    """
    A class to interact with different LLM (Large Language Model) API services, such as Together and Groq.

    Attributes:
    -----------
    api_service : str
        The name of the API service to use ("Together" or "Groq").
    """

    def __init__(self, api_service: str) -> None:
        """
        Initialize the LLMService with a specific API service.

        Parameters:
        -----------
        api_service : str
            The name of the LLM API service, either "Together" or "Groq".
        """
        self.api_service = api_service

    def generate_response(self, conversation_history: List[Dict[str, str]]) -> str:
        """
        Generate a response from the specified LLM API based on the conversation history.

        Parameters:
        -----------
        conversation_history : List[Dict[str, str]]
            The list of conversation messages, where each message is a dictionary with 'role' and 'content' keys.

        Returns:
        --------
        str
            The generated response content from the assistant.

        Raises:
        -------
        ValueError
            If the specified API service is neither "Together" nor "Groq".
        """
        if self.api_service == "Together":
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
        elif self.api_service == "Groq":
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
        else:
            raise ValueError(f"Unsupported API service: {self.api_service}")

        # Extracting the content of the generated response
        return response.choices[0].message.content
