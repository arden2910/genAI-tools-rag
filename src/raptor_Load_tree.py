from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from raptor import RetrievalAugmentation
from langchain_openai.chat_models import AzureChatOpenAI
from langchain_openai.embeddings import AzureOpenAIEmbeddings
from raptor import BaseSummarizationModel, BaseQAModel, BaseEmbeddingModel, RetrievalAugmentationConfig
import dotenv
import os
from pathlib import Path

dotenv.load_dotenv()


def llm_api_call(input_string: str, model_name='gpt-4o', system='you are a helpful assistant') -> str:
    # 建立 embedding

    # 建立 LLM
    llm = AzureChatOpenAI(
        azure_deployment=model_name,
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        model=model_name,
        azure_endpoint=os.getenv("AZURE_OPENAI_BASE_URL"),
        max_retries=2,
        temperature=1,
        max_tokens=1000,
        timeout=None,
    )
    # 定義 Prompt 模板
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system),
            ("human", "{input_string}")
        ]
    )

    # 建立可執行管道 (提示詞 | LLM | 輸出解析器)
    runnable = prompt | llm | StrOutputParser()

    # 執行推理並獲得結果
    result_data = runnable.invoke({"input_string": input_string})

    # 最終僅以 return 方式回傳結果
    return str(result_data)

class SummarizationModel(BaseSummarizationModel):
    def __init__(self, model_name=""):
        pass

    def summarize(self, context, max_tokens=150):
        summary = llm_api_call(
            f"Write a summary of the following, including as many key details as possible: {context}")
        return summary

class QAModel(BaseQAModel):
    def __init__(self, model_name=""):
        pass

    def answer_question(self, context, question):
        # Apply the chat template for the context and question

        answer = llm_api_call(
            f"Given Context: {context} Give the best full answer to the question {question}"
        )
        return answer

class EmbeddingModel(BaseEmbeddingModel):
    def __init__(self, model_name=""):
        pass

    def create_embedding(self, text):
        embeddings = AzureOpenAIEmbeddings(
            model=os.getenv("AZURE_OPENAI_EMBEDDING_NAME"),
            azure_endpoint=os.getenv("AZURE_OPENAI_BASE_URL"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        )
        return embeddings.embed_query(text)


def main():
    RAC = RetrievalAugmentationConfig(summarization_model=SummarizationModel(), qa_model=QAModel(),
                                      embedding_model=EmbeddingModel())
    RA = RetrievalAugmentation(config=RAC, tree=r'C:\Users\ardenlo\Dropbox\genAI-tools-rag\raptor_tree\0630_v1')

    question = "有哪些AI工具?"


    context, layer_information = RA.retrieve(question,top_k=20)

    # print("context: ", context)
    chunks = context.split('\n\n')
    chunks = [each for each in chunks if each.strip() != '']

    print("number of chunks: ", len(chunks))
    filenames = [c.split("###content---")[0] for c in chunks]
    print(filenames)
    print("number of filenames: ", len(filenames))


if __name__ == '__main__':
    main()
