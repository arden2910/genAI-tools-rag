#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
檢索器
負責從向量資料庫檢索相關的 chunks，不進行 LLM 查詢
"""

import os
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dotenv import load_dotenv

# LangChain imports
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_openai.embeddings import AzureOpenAIEmbeddings

# 載入環境變數
load_dotenv()

class Retriever:
    def __init__(self, 
                 chroma_dir: str = r"C:\Users\ardenlo\Dropbox\genAI-tools-rag\chroma_db",
                 collection_name: str = "genai_tools"):
        """
        初始化檢索器
        
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
        }
        
        # 初始化 Embedding 模型
        self._init_embeddings()
        
        # 初始化向量資料庫
        self._init_vectorstore()
    
    def _init_embeddings(self):
        """初始化 Embedding 模型"""
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
            搜尋結果列表，每個元素為 (Document, score) 的元組
        """
        try:
            results = self.vectorstore.similarity_search_with_score(
                query, k=k, filter=filter_dict
            )
            return results
        except Exception as e:
            print(f"搜尋時發生錯誤: {e}")
            return []
    
    def similarity_search_with_metadata(self, 
                                       query: str, 
                                       k: int = 5, 
                                       filter_dict: Optional[Dict] = None) -> Dict:
        """
        相似度搜尋並返回詳細的 metadata 資訊
        
        Args:
            query: 查詢文字
            k: 返回結果數量
            filter_dict: 過濾條件
            
        Returns:
            包含 documents, metadatas, distances 的字典
        """
        try:
            results = self.vectorstore.similarity_search_with_score(
                query, k=k, filter=filter_dict
            )
            
            documents = []
            metadatas = []
            distances = []
            
            for doc, score in results:
                documents.append(doc.page_content)
                metadatas.append(doc.metadata)
                distances.append(score)
            
            return {
                'documents': documents,
                'metadatas': metadatas,
                'distances': distances
            }
        except Exception as e:
            print(f"搜尋時發生錯誤: {e}")
            return {'documents': [], 'metadatas': [], 'distances': []}
    
    def get_filenames_from_results(self, results: Dict) -> List[str]:
        """
        從搜尋結果中提取 filename 列表
        
        Args:
            results: similarity_search_with_metadata 的結果
            
        Returns:
            filename 列表
        """
        filenames = []
        for metadata in results.get('metadatas', []):
            filename = metadata.get('filename', '')
            if filename:
                filenames.append(filename)
        return filenames
    
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
    
    def get_all_documents(self, filter_dict: Optional[Dict] = None) -> List[Document]:
        """
        獲取所有文件（可選過濾）
        
        Args:
            filter_dict: 過濾條件
            
        Returns:
            文件列表
        """
        try:
            results = self.vectorstore.get(include=['documents', 'metadatas'], where=filter_dict)
            documents = []
            for i, content in enumerate(results.get('documents', [])):
                metadata = results.get('metadatas', [{}])[i] if results.get('metadatas') else {}
                doc = Document(page_content=content, metadata=metadata)
                documents.append(doc)
            return documents
        except Exception as e:
            print(f"獲取文件時發生錯誤: {e}")
            return []
    
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
    
    def print_search_results(self, results: List[Tuple[Document, float]], title: str = "搜尋結果"):
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
            print(f"   內容: {doc.page_content[:150]}...")
            print()


def main():
    """主程式 - 示範檢索功能"""
    print("=== 檢索器 ===")
    
    # 檢查環境變數
    if not os.environ.get("AZURE_OPENAI_API_KEY"):
        print("錯誤: 請設定 AZURE_OPENAI_API_KEY 環境變數")
        return
    
    # 初始化檢索器
    retriever = Retriever()
    
    # 顯示集合資訊
    info = retriever.get_collection_info()
    print(f"集合資訊: {info}")
    
    # 示範搜尋
    print("\n=== 示範搜尋 ===")
    
    # 1. 一般相似度搜尋
    # print("1. 搜尋 'AI 助手':")
    # results = retriever.similarity_search("AI 助手", k=100)
    # retriever.print_search_results(results, "AI 助手搜尋結果")

    # 2. 按前綴搜尋
    print("2. 在 application 中搜尋 '語音':")
    results = retriever.search_by_prefix("語音", "application", k=100)
    retriever.print_search_results(results, "Application 語音工具搜尋結果")

    # # 3. 在 development 中搜尋
    # print("3. 在 development 中搜尋 'LangChain':")
    # results = retriever.search_by_prefix("LangChain", "development", k=3)
    # retriever.print_search_results(results, "Development LangChain 搜尋結果")
    #
    # # 互動式搜尋
    # print("\n=== 互動式搜尋 ===")
    # print("輸入 'quit' 退出")
    # print("格式: [前綴:] 查詢文字")
    # print("範例: application:語音生成")
    # print("範例: 搜尋所有")
    # print("-" * 50)
    #
    # while True:
    #     try:
    #         user_input = input("\n請輸入搜尋: ").strip()
    #
    #         if user_input.lower() in ['quit', 'exit', 'q']:
    #             print("再見！")
    #             break
    #
    #         if ':' in user_input:
    #             # 按前綴搜尋
    #             prefix, query = user_input.split(':', 1)
    #             prefix = prefix.strip()
    #             query = query.strip()
    #
    #             if prefix and query:
    #                 results = retriever.search_by_prefix(query, prefix, k=5)
    #                 retriever.print_search_results(results, f"{prefix} 搜尋結果")
    #             else:
    #                 print("格式錯誤，請使用 '前綴:查詢' 格式")
    #         else:
    #             # 一般搜尋
    #             if user_input:
    #                 results = retriever.similarity_search(user_input, k=5)
    #                 retriever.print_search_results(results, "搜尋結果")
    #             else:
    #                 print("請輸入搜尋內容")
    #
    #     except KeyboardInterrupt:
    #         print("\n\n再見！")
    #         break
    #     except Exception as e:
    #         print(f"發生錯誤: {e}")


if __name__ == "__main__":
    main() 