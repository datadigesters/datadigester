from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# open ai의 LLM 모델 이용
llm = ChatOpenAI(api_key="sk-proj-ej3Oeiw2RQISNgFiwq7AT3BlbkFJ3b03ApL2SsGdivEsh0tB")

# openai chat 설정. prompt 기능 사용
prompt = ChatPromptTemplate.from_messages([
    #AI 컨셉설정
    ("system", "You are a korean researcher conducting data collection to write a thesis at the university. Procced in the follwing order."), #AI 컨셉설정
    ("user", "{input}")
])

# open ai의 출력 기능 사용
output_parser = StrOutputParser()

# chain 으로 openAI의 3가지 기능 연결
chain = prompt | llm | output_parser

def generate_summary(query):
    # 요청할 텍스트의 양을 줄입니다.
    result = chain.invoke({"input": query + "에 대한 자료조사 결과를 500자 이상의 한글로 요약해줘"})
    return result