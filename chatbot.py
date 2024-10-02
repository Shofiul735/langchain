from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memeory import ConversationBufferMemeory,FileChatMessageMemory,ConversationSummaryMemory
from dotenv import load_env

load_env()

memeory = ConversationBufferMemeory(
    chat_memory=FileChatMessageHistory("messages.json")
    memery_key="messages",
    return_messages=True
    )
llm = ChatOpenAI()

prompt = ChatPromptTemplate(
    input_variables=["content","messages"],
    messgaes=[
        MessagesPlaceholder(variable_name="messages")
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=llm,
    prompt= prompt
    memeory=memeory
)

while True:
    content = input(">> ")
    result = chain({"content":content})
    