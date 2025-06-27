#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
聊天系統
結合檢索和 LLM 查詢功能，提供完整的 RAG 聊天體驗
"""

import os
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dotenv import load_dotenv

# LangChain imports
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_openai.chat_models import AzureChatOpenAI
from langchain_openai.embeddings import AzureOpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# 載入環境變數
load_dotenv()

class ChatSystem:
    def __init__(self, 
                 chroma_dir: str = r"C:\Users\ardenlo\Dropbox\genAI-tools-rag\chroma_db",
                 collection_name: str = "genai_tools"):
        """
        初始化聊天系統
        
        Args:
            chroma_dir: Chroma 資料庫目錄
            collection_name: Chroma 集合名稱
        """
        self.chroma_dir = Path(chroma_dir)
        self.collection_name = collection_name
        
        # 初始化 Azure OpenAI 配置
        self.azure_configs = {
            "base_url": "https://iii-azure-openai-eastus.openai.azure.com/",
            "embedding_name": "text-embedding-3-small",
            'api_key': os.environ.get("AZURE_OPENAI_API_KEY"),
            "api_version": "2024-05-01-preview",
            "model_name": "gpt-4o"
        }
        
        # 初始化模型
        self._init_models()
        
        # 初始化向量資料庫
        self._init_vectorstore()
        
        # 初始化 RAG 鏈
        self._init_rag_chain()
    
    def _init_models(self):
        """初始化 LLM 和 Embedding 模型"""
        # 初始化 LLM
        self.llm = AzureChatOpenAI(
            azure_deployment=self.azure_configs["model_name"],
            api_version=self.azure_configs['api_version'],
            api_key=self.azure_configs["api_key"],
            model=self.azure_configs["model_name"],
            azure_endpoint=self.azure_configs["base_url"],
            max_retries=2,
            temperature=0,
            max_tokens=2000,
            timeout=None,
        )
        
        # 初始化 Embedding 模型
        self.embeddings = AzureOpenAIEmbeddings(
            model=self.azure_configs["embedding_name"],
            azure_endpoint=self.azure_configs["base_url"],
            api_key=self.azure_configs["api_key"],
            openai_api_version=self.azure_configs["api_version"],
        )
    
    def _init_vectorstore(self):
        """初始化 Chroma 向量資料庫"""
        self.vectorstore = Chroma(
            collection_name=self.collection_name,
            embedding_function=self.embeddings,
            persist_directory=str(self.chroma_dir),
        )
    
    def _init_rag_chain(self):
        """初始化 RAG 檢索鏈"""
        # 檢索模板
        self.retrieval_template = """
        你是一個專業的 AI 工具專家。請根據以下上下文回答問題。
        
        上下文：
        {context}
        
        問題：{question}
        
        請提供詳細且準確的回答，如果上下文中沒有相關資訊，請明確說明。
        """
        
        # 建立 RAG 鏈
        self.rag_chain = (
            {"context": self.vectorstore.as_retriever(search_kwargs={"k": 5}), 
             "question": RunnablePassthrough()}
            | ChatPromptTemplate.from_template(self.retrieval_template)
            | self.llm
            | StrOutputParser()
        )
    
    def similarity_search(self, 
                         query: str, 
                         k: int = 5, 
                         filter_dict: Optional[Dict] = None) -> List[Tuple[Document, float]]:
        """
        相似度搜尋
        
        Args:
            query: 查詢文字
            k: 返回結果數量
            filter_dict: 過濾條件
            
        Returns:
            搜尋結果列表
        """
        try:
            results = self.vectorstore.similarity_search_with_score(
                query, k=k, filter=filter_dict
            )
            return results
        except Exception as e:
            print(f"搜尋時發生錯誤: {e}")
            return []
    
    def search_by_prefix(self, query: str, prefix: str, k: int = 5) -> List[Tuple[Document, float]]:
        """
        按前綴過濾搜尋
        
        Args:
            query: 查詢文字
            prefix: 前綴（application, development, model）
            k: 返回結果數量
            
        Returns:
            搜尋結果列表
        """
        return self.similarity_search(query, k=k, filter_dict={"prefix": prefix})
    
    def query(self, question: str) -> str:
        """
        使用 RAG 鏈回答問題
        
        Args:
            question: 問題
            
        Returns:
            回答
        """
        try:
            response = self.rag_chain.invoke(question)
            return response
        except Exception as e:
            print(f"查詢時發生錯誤: {e}")
            return f"抱歉，處理您的問題時發生錯誤: {e}"
    
    def query_with_context(self, question: str, k: int = 5) -> Tuple[str, List[Tuple[Document, float]]]:
        """
        查詢並返回上下文
        
        Args:
            question: 問題
            k: 檢索數量
            
        Returns:
            (回答, 檢索結果)
        """
        # 先進行檢索
        search_results = self.similarity_search(question, k=k)
        
        # 使用檢索結果進行回答
        try:
            # 建立上下文
            context = "\n\n".join([doc.page_content for doc, _ in search_results])
            
            # 使用模板生成回答
            prompt = ChatPromptTemplate.from_template(self.retrieval_template)
            chain = prompt | self.llm | StrOutputParser()
            
            response = chain.invoke({"context": context, "question": question})
            return response, search_results
        except Exception as e:
            print(f"查詢時發生錯誤: {e}")
            return f"抱歉，處理您的問題時發生錯誤: {e}", search_results
    
    def get_collection_info(self) -> Dict:
        """獲取集合資訊"""
        try:
            results = self.vectorstore.get(include=['documents', 'metadatas'])
            return {
                "document_count": len(results.get('documents', [])),
                "metadata_keys": list(results.get('metadatas', [{}])[0].keys()) if results.get('metadatas') else [],
                "prefixes": list(set([meta.get('prefix', '') for meta in results.get('metadatas', [])]))
            }
        except Exception as e:
            print(f"獲取集合資訊時發生錯誤: {e}")
            return {}
    
    def print_search_results(self, results: List[Tuple[Document, float]], title: str = "檢索結果"):
        """
        格式化輸出搜尋結果
        
        Args:
            results: 搜尋結果
            title: 標題
        """
        print(f"\n=== {title} ===")
        if not results:
            print("沒有找到相關結果")
            return
        
        for i, (doc, score) in enumerate(results, 1):
            print(f"{i}. [{score:.3f}] {doc.metadata.get('title', 'Unknown')}")
            print(f"   前綴: {doc.metadata.get('prefix', 'Unknown')}")
            print(f"   內容: {doc.page_content[:100]}...")
            print()


def main():
    """主程式 - 互動式聊天"""
    print("=== GenAI Tools 聊天系統 ===")
    
    # 檢查環境變數
    if not os.environ.get("AZURE_OPENAI_API_KEY"):
        print("錯誤: 請設定 AZURE_OPENAI_API_KEY 環境變數")
        return
    
    # 初始化聊天系統
    chat = ChatSystem()
    
    # 檢查是否已有資料
    info = chat.get_collection_info()
    if info.get("document_count", 0) == 0:
        print("向量資料庫為空，請先執行 data_indexer.py 載入資料")
        return
    
    print(f"向量資料庫已有 {info['document_count']} 個文件")
    print(f"可用前綴: {info.get('prefixes', [])}")
    
    # 互動式聊天
    print("\n=== 互動式聊天 ===")
    print("輸入 'quit' 或 'exit' 退出")
    print("輸入 'info' 查看資料庫資訊")
    print("輸入 'search <關鍵字>' 進行相似度搜尋")
    print("輸入 'search <前綴>:<關鍵字>' 按前綴搜尋")
    print("輸入 'context <問題>' 查看檢索上下文")
    print("輸入其他內容進行 RAG 查詢")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n請輸入: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("再見！")
                break
            
            elif user_input.lower() == 'info':
                info = chat.get_collection_info()
                print(f"文件數量: {info.get('document_count', 0)}")
                print(f"前綴類型: {info.get('prefixes', [])}")
                print(f"Metadata 欄位: {info.get('metadata_keys', [])}")
            
            elif user_input.lower().startswith('search '):
                query = user_input[7:].strip()
                if ':' in query:
                    # 按前綴搜尋
                    prefix, search_query = query.split(':', 1)
                    prefix = prefix.strip()
                    search_query = search_query.strip()
                    
                    if prefix and search_query:
                        print(f"在 {prefix} 中搜尋: {search_query}")
                        results = chat.search_by_prefix(search_query, prefix, k=3)
                        chat.print_search_results(results, f"{prefix} 搜尋結果")
                    else:
                        print("格式錯誤，請使用 'search 前綴:關鍵字' 格式")
                else:
                    # 一般搜尋
                    if query:
                        print(f"搜尋: {query}")
                        results = chat.similarity_search(query, k=3)
                        chat.print_search_results(results, "搜尋結果")
                    else:
                        print("請輸入搜尋關鍵字")
            
            elif user_input.lower().startswith('context '):
                question = user_input[8:].strip()
                if question:
                    print("正在處理查詢...")
                    response, search_results = chat.query_with_context(question)
                    print(f"回答: {response}")
                    chat.print_search_results(search_results, "檢索上下文")
                else:
                    print("請輸入問題")
            
            elif user_input:
                print("正在處理查詢...")
                response = chat.query(user_input)
                print(f"回答: {response}")
            
        except KeyboardInterrupt:
            print("\n\n再見！")
            break
        except Exception as e:
            print(f"發生錯誤: {e}")


if __name__ == "__main__":
    main() 