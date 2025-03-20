README - Projeto de Tradução com LangChain e Groq
Índice
Descrição do Projeto
Como Copiar o Repositório
Instalação das Dependências
Estrutura do Código
Explicação do Código
Glossário
Descrição do Projeto
Este projeto utiliza o framework LangChain para construção de pipelines de processamento de linguagem natural, utilizando o modelo Gemma2-9b-It através da API da Groq. O objetivo do projeto é traduzir frases entre diferentes idiomas utilizando um pipeline de prompt engineering com componentes do LangChain.

A implementação utiliza variáveis de ambiente para gerenciar as chaves de API, o que facilita a integração e segurança dos dados utilizados. O código também demonstra o uso de prompts, parsers de saída e templates, permitindo personalizar a tradução de frases de acordo com o idioma desejado.

Como Copiar o Repositório
Para copiar o repositório, siga as instruções abaixo:

Acesse o repositório do projeto no GitHub.
Clique no botão Code e copie a URL do repositório.
Abra seu terminal e digite o seguinte comando para clonar o repositório:
bash
Copiar
Editar
git clone <URL_DO_REPOSITORIO>
Instalação das Dependências
Este projeto depende de algumas bibliotecas Python para funcionar corretamente. Você pode instalar todas as dependências utilizando o arquivo requirements.txt ou manualmente via pip.

Instalando a partir do arquivo requirements.txt
Após clonar o repositório, navegue até o diretório do projeto no terminal.
Execute o seguinte comando para instalar as dependências:
bash
Copiar
Editar
pip install -r requirements.txt
Instalando manualmente
Caso prefira, você também pode instalar as dependências manualmente utilizando o pip. Execute o seguinte comando para instalar cada uma das bibliotecas necessárias:

bash
Copiar
Editar
pip install langchain_core
pip install langchain_groq
pip install python-dotenv
Estrutura do Código
O código é dividido em três blocos principais:

Importação das Bibliotecas: Carrega as bibliotecas necessárias para utilizar o LangChain, a API do Groq e gerenciar variáveis de ambiente.
Carregamento de Variáveis de Ambiente: Carrega as credenciais da API Groq a partir de um arquivo .env.
Construção do Modelo e Pipeline de Tradução: Define o modelo, o prompt e o parser para realizar a tradução de frases entre diferentes idiomas.
Explicação do Código
1. Importação das Bibliotecas
python
Copiar
Editar
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os
langchain_core.messages: Importa as classes HumanMessage e SystemMessage para definir as mensagens no pipeline de conversa.
langchain_core.prompts: Importa ChatPromptTemplate para criar prompts personalizados.
langchain_core.output_parsers: Importa StrOutputParser para tratar a saída do modelo.
langchain_groq: Importa o ChatGroq, que permite interagir com a API do Groq.
dotenv: Carrega variáveis de ambiente a partir de um arquivo .env para segurança das credenciais.
os: Permite acessar as variáveis de ambiente no sistema operacional.
2. Carregamento de Variáveis de Ambiente
python
Copiar
Editar
load_dotenv(find_dotenv())
groq_api_key = os.getenv("GROQ_API_KEY")
load_dotenv: Carrega o arquivo .env que contém as variáveis de ambiente.
groq_api_key: Obtém a chave de API do Groq a partir da variável de ambiente GROQ_API_KEY.
3. Criando o Modelo Groq
python
Copiar
Editar
llm = ChatGroq(
    model = "Gemma2-9b-It",
    groq_api_key = groq_api_key,
)
ChatGroq: Instancia o modelo de linguagem Gemma2-9b-It da Groq, utilizando a chave de API.
4. Definindo o Prompt
python
Copiar
Editar
messagens = [
    SystemMessage(content = 'Translate the following sentence from English to French'),
    HumanMessage(content = 'Hello, how are you?')
]
Define um conjunto de mensagens que representam a interação com o modelo, especificando o sistema e o usuário. O modelo recebe a instrução de traduzir a frase do inglês para o francês.
5. Parser de Saída
python
Copiar
Editar
parser = StrOutputParser()
StrOutputParser: Utilizado para processar e formatar a saída gerada pelo modelo, transformando a resposta em texto simples.
6. Criando o Template de Prompt
python
Copiar
Editar
generic_template = 'Traduza a seguinte frase em {language}'

prompt = ChatPromptTemplate.from_messages(
    [
        ('system', generic_template),
        ('user', '{text}')
    ]
)
ChatPromptTemplate: Cria um template de prompt que aceita dois parâmetros (language e text), permitindo flexibilidade na tradução entre diferentes idiomas.
7. Montando a Cadeia de Execução
python
Copiar
Editar
chain = prompt | llm | parser
chain: Cria a sequência de execução do pipeline, onde o prompt é passado para o modelo, que por sua vez é processado pelo parser para gerar a resposta final.
8. Executando o Pipeline
python
Copiar
Editar
print(chain.invoke({'language': 'German', 'text': 'Como você está?'}))
invoke: Executa a cadeia de componentes com os parâmetros fornecidos (language e text), neste caso traduzindo a frase "Como você está?" para o alemão.
Glossário
LangChain: Framework que facilita a criação de pipelines de processamento de linguagem natural, integrando diferentes componentes como modelos de linguagem, prompts e parsers.
Groq: Plataforma que fornece acesso a modelos de linguagem de última geração, como o Gemma2-9b-It.
ChatPromptTemplate: Classe utilizada para criar prompts estruturados para interação com modelos de linguagem.
StrOutputParser: Parser utilizado para processar e formatar a saída de texto gerada pelo modelo de linguagem.
dotenv: Biblioteca que permite carregar variáveis de ambiente de um arquivo .env para melhorar a segurança e gestão de credenciais.
API Key: Chave de acesso utilizada para autenticar a comunicação com a API da Groq.
Esse README fornece todas as informações necessárias para entender e executar o código do projeto. Caso haja dúvidas ou a necessidade de mais informações, sinta-se à vontade para explorar os recursos adicionais na documentação do LangChain e da Groq.
