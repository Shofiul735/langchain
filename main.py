from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv

load_dotenv()

api_key = 'key'

llm = OpenAI(
    openai_api_key=api_key
)

prompt = PromptTemplate(
    template = "Write a very short {language} function that will {task}",
    input_variables = ["language","task"]
)

test_prompt = PromptTemplate(
    template="Write a test code in {language} for this code:\n {code}",
    input_variables = ["language","code"]
)

code_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    output_key="code"
)
test_chain = LLMChain(
    llm=llm,
    prompt=test_prompt,
    output_key="test"
)

chain = SequentialChain(
    chains=[
        code_chain,
        test_chain
    ],
    input_variables=["task","language"],
    output_variable=["test","code"]
)

result = chain({
    "language":"python",
    "task": "return a list of number"
})

print(">>>> Generated code:")

print(result["code"])

print(">>>> Generated Test")

print(result["test"])