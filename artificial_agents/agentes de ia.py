# %%
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

google_api_key = os.environ.get("API_KEY")

# %%

TRIAGEM_PROMPT = (
    "Você é um triador de Service Desk para políticas internas da empresa Carraro Desenvolvimento. "
    "Dada a mensagem do usuário, retorne SOMENTE um JSON com:\n"
    "{\n"
    '  "decisao": "AUTO_RESOLVER" | "PEDIR_INFO" | "ABRIR_CHAMADO",\n'
    '  "urgencia": "BAIXA" | "MEDIA" | "ALTA",\n'
    '  "campos_faltantes": ["..."]\n'
    "}\n"
    "Regras:\n"
    '- **AUTO_RESOLVER**: Perguntas claras sobre regras ou procedimentos descritos nas políticas (Ex: "Posso reembolsar a internet do meu home office?", "Como funciona a política de alimentação em viagens?").\n'
    '- **PEDIR_INFO**: Mensagens vagas ou que faltam informações para identificar o tema ou contexto (Ex: "Preciso de ajuda com uma política", "Tenho uma dúvida geral").\n'
    '- **ABRIR_CHAMADO**: Pedidos de exceção, liberação, aprovação ou acesso especial, ou quando o usuário explicitamente pede para abrir um chamado (Ex: "Quero exceção para trabalhar 5 dias remoto.", "Solicito liberação para anexos externos.", "Por favor, abra um chamado para o RH.").'
    "Analise a mensagem e decida a ação mais apropriada."
    
    """
    decisao: AUTO_RESOLVER 
    ugencia: BAIXA
    campos_faltantes: []
    """
)
# %%

from pydantic import BaseModel, Field
from typing import Literal, List, Dict

class TriagemOut(BaseModel):
    decisao: Literal["AUTO_RESOLVER", "PEDIR_INFO", "ABRIR_CHAMADO"]
    urgencia: Literal["BAIXA", "MEDIA", "ALTA"] 
    campos_faltantes: List[str] = Field(default_factory=list)
    
# %%
    
llm_triagem = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0, api_key=google_api_key)
# %%

from langchain_core.messages import SystemMessage, HumanMessage

triagem_chain = llm_triagem.with_structured_output(TriagemOut)

def triagem(mensagem: str) -> Dict:
    saida: TriagemOut = triagem_chain.invoke([SystemMessage(content=TRIAGEM_PROMPT), HumanMessage(content=mensagem)])
    return saida.model_dump()
# %%

testes = ["posso reembolsar a internet?", "Quero ter mais 5 dias remoto?", "Como sacar o pino do coquilho traseiro do guindaste zunlaine 75"]

for msg_test in testes:
    print(f"Pergunta: {msg_test}\n -> Resposta: {triagem(msg_test)}\n")
    
# %%

from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

docs = [];

for n in Path(".").glob("*.pdf"):
    try:
        loader = PyMuPDFLoader(str(n))
        docs.extend(loader.load()) 
        print(f"carregado arquivo com sucesso: {n.name}")
    except Exception as a:
            print(f"Erro ao carregar arquivo {n.name}: {a}")
# %%
            
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=30)

chunks = splitter.split_documents(docs)

# %%

for chunk in chunks:
    print(chunk);
    print("--------------------------")
# %%
    
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embedding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=google_api_key)

# %%

from langchain_community.vectorstores import FAISS

vectorstoe = FAISS.from_documents(chunks, embedding)

retriever = vectorstoe.as_retriever(search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.3, "k": 4})
+
# %%

from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

prompt_rag = ChatPromptTemplate.from_messages([
    ("system",
     "Você é um Assistente de Políticas Internas (RH/IT) da empresa Carraro Desenvolvimento. "
     "Responda SOMENTE com base no contexto fornecido. "
     "Se não houver base suficiente, responda apenas 'Não sei'."),

    ("human", "Pergunta: {input}\n\nContexto:\n{context}")
])

document_chain = create_stuff_documents_chain(llm_triagem, prompt_rag)

# %%

def askPolitic_rag(pergunta: str) -> Dict:
    
    
    