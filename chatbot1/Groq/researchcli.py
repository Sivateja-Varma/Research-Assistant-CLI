from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

prompt=ChatPromptTemplate.from_messages([('system','you are a helpful assistant'),
                                         ('user','{question}')])
llm=ChatGroq(model='openai/gpt-oss-120b')
parser=StrOutputParser()
def inference(input_query:str):
  if input_query:
    chain = prompt|llm|parser
    response=chain.invoke({'question':input_query})
  return response  

cap=True
while cap:
  input_query=input('enter your query 🔬: ')

  if input_query.strip() == "":
    print('cannot process empty spaces ❌')
    continue
  elif input_query in ['exit','Exit','End','end']:
    print('thanks for invoking hope I helped u 😊')
    cap=False
  else:  
    print('thinking....🤔')
    response=inference(input_query)
    print(response)  




