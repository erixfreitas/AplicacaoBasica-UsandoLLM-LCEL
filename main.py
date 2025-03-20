# IMPORTANDO AS BIBLIOTECAS
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os

# CARREGANDO AS VARIÁVEIS DE AMBIENTE
load_dotenv(find_dotenv())
groq_api_key = os.getenv("GROQ_API_KEY")

# 1 CRIAR O MODELO GROQ 
llm = ChatGroq(
    model = "Gemma2-9b-It", # MODELO DE LLM UTILIZADO
    groq_api_key = groq_api_key, # CHAVE DE API DO GROQ
)

# CRIAR O PROMPT *** ESTUDAR SOBRE PROMPT ENGINEERING (FEW-SHOT, ZERO-SHOT, ONE-SHOT, CHAIN OF THOUGHTS)
messagens = [
    SystemMessage(content = 'Translate the following sentence from English to French'),
    HumanMessage(content = 'Hello, how are you?')
]

# 2 PARSER DE SAÍDA - ISSo É PARA TRATAR A SAÍDA DO MODELO
parser = StrOutputParser()

# 3 PROMPT TEMPLATE UTILIZANDO O LCEL - CHAIN THE COMPONENTS
generic_template = 'Traduza a seguinte frase em {language}'

prompt = ChatPromptTemplate.from_messages(
    [
        ('system', generic_template),
        ('user', '{text}')
    ]
)

chain = prompt | llm | parser

# EXECUTAR A CHAIN
print(chain.invoke({'language': 'German', 'text': 'Como você está?'}))