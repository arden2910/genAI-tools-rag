#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
資料索引器
負責載入資料到 Chroma 向量資料庫，支援增量 upsert
"""

import os
from pathlib import Path
from typing import List, Optional, Dict, Any
from dotenv import load_dotenv

# LangChain imports
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_openai.embeddings import AzureOpenAIEmbeddings

# 載入環境變數
load_dotenv()

class DataIndexer:
    def __init__(self, 
                 data_dir: str = r"C:\Users\ardenlo\Dropbox\genAI-tools-rag\data\cleaned",
                 chroma_dir: str = r"C:\Users\ardenlo\Dropbox\genAI-tools-rag\chroma_db",
                 collection_name: str = "genai_tools"):
        """
        初始化資料索引器
        
        Args:
            data_dir: 資料來源目錄
            chroma_dir: Chroma 資料庫目錄
            collection_name: Chroma 集合名稱
        """
        self.data_dir = Path(data_dir)
        self.chroma_dir = Path(chroma_dir)
        self.collection_name = collection_name
        
        # 確保 Chroma 目錄存在
        self.chroma_dir.mkdir(parents=True, exist_ok=True)
        
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
    
    def get_existing_document_ids(self) -> set:
        """
        獲取資料庫中已存在的文件 ID
        
        Returns:
            已存在的文件 ID 集合
        """
        try:
            results = self.vectorstore.get(include=['metadatas'])
            existing_ids = set()
            for metadata in results.get('metadatas', []):
                if metadata and 'filename' in metadata:
                    existing_ids.add(metadata['filename'])
            return existing_ids
        except Exception as e:
            print(f"獲取現有文件 ID 時發生錯誤: {e}")
            return set()
    
    def load_documents(self, date_folder: Optional[str] = None) -> List[Document]:
        """
        載入文件
        
        Args:
            date_folder: 日期資料夾名稱，如果為 None 則使用最新的資料夾
            
        Returns:
            載入的文件列表
        """
        # 如果沒有指定日期資料夾，使用最新的
        if date_folder is None:
            date_folders = [d for d in self.data_dir.iterdir() if d.is_dir()]
            if not date_folders:
                raise ValueError(f"在 {self.data_dir} 中沒有找到日期資料夾")
            date_folder = max(date_folders, key=lambda x: x.name).name
        
        data_folder = self.data_dir / date_folder
        if not data_folder.exists():
            raise ValueError(f"資料夾 {data_folder} 不存在")
        
        documents = []
        
        # 遍歷所有 txt 檔案
        for txt_file in data_folder.glob("*.txt"):
            try:
                with open(txt_file, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                
                if content:
                    # 解析檔案名稱獲取前綴和序號
                    filename = txt_file.stem
                    parts = filename.split('_', 2)  # 最多分割2次
                    
                    if len(parts) >= 3:
                        prefix, number, title = parts[0], parts[1], parts[2]
                    else:
                        prefix, number, title = parts[0], "00", "_".join(parts[1:]) if len(parts) > 1 else "untitled"
                    
                    # 建立 metadata
                    metadata = {
                        "filename": txt_file.name,  # 使用完整檔案名稱作為唯一標識
                        "prefix": prefix,
                        "number": number,
                        "title": title,
                        "date_folder": date_folder,
                        "source": str(txt_file),
                        "file_path": str(txt_file)
                    }
                    
                    # 建立 Document
                    doc = Document(
                        page_content=content,
                        metadata=metadata
                    )
                    documents.append(doc)
                    
            except Exception as e:
                print(f"讀取檔案 {txt_file} 時發生錯誤: {e}")
        
        print(f"成功載入 {len(documents)} 個文件")
        return documents
    
    def upsert_documents(self, documents: List[Document], batch_size: int = 20):
        """
        增量 upsert 文件到向量資料庫
        
        Args:
            documents: 文件列表
            batch_size: 批次大小
        """
        if not documents:
            print("沒有文件需要處理")
            return
        
        # 獲取現有的文件 ID
        existing_ids = self.get_existing_document_ids()
        print(f"資料庫現有文件數量: {len(existing_ids)}")
        
        # 分類文件：新增 vs 更新
        new_documents = []
        update_documents = []
        update_ids = []
        
        for doc in documents:
            filename = doc.metadata.get('filename')
            if filename in existing_ids:
                update_documents.append(doc)
                update_ids.append(filename)
            else:
                new_documents.append(doc)
        
        print(f"新增文件: {len(new_documents)} 個")
        print(f"更新文件: {len(update_documents)} 個")
        
        # 處理新增文件
        if new_documents:
            print("正在添加新文件...")
            self._add_documents_batch(new_documents, batch_size)
        
        # 處理更新文件
        if update_documents:
            print("正在更新現有文件...")
            self._update_documents_batch(update_documents, update_ids, batch_size)
        
        # 檢查最終文件數量
        final_count = len(self.get_existing_document_ids())
        print(f"資料庫最終文件數量: {final_count}")
    
    def _add_documents_batch(self, documents: List[Document], batch_size: int):
        """
        批次添加新文件
        
        Args:
            documents: 文件列表
            batch_size: 批次大小
        """
        for i in range(0, len(documents), batch_size):
            batch = documents[i:i + batch_size]
            batch_ids = [doc.metadata.get('filename') for doc in batch]
            
            try:
                self.vectorstore.add_documents(documents=batch, ids=batch_ids)
                print(f"已添加批次 {i//batch_size + 1}/{(len(documents) + batch_size - 1)//batch_size}")
            except Exception as e:
                print(f"添加批次時發生錯誤: {e}")
    
    def _update_documents_batch(self, documents: List[Document], ids: List[str], batch_size: int):
        """
        批次更新文件
        
        Args:
            documents: 文件列表
            ids: 文件 ID 列表
            batch_size: 批次大小
        """
        for i in range(0, len(documents), batch_size):
            batch_docs = documents[i:i + batch_size]
            batch_ids = ids[i:i + batch_size]
            
            try:
                # 使用 upsert 方法更新文件
                self.vectorstore.upsert_documents(documents=batch_docs, ids=batch_ids)
                print(f"已更新批次 {i//batch_size + 1}/{(len(documents) + batch_size - 1)//batch_size}")
            except Exception as e:
                print(f"更新批次時發生錯誤: {e}")
    
    def get_collection_info(self) -> Dict[str, Any]:
        """獲取集合資訊"""
        try:
            results = self.vectorstore.get(include=['documents', 'metadatas'])
            metadatas = results.get('metadatas', [])
            
            # 統計各前綴的文件數量
            prefix_counts = {}
            for metadata in metadatas:
                if metadata and 'prefix' in metadata:
                    prefix = metadata['prefix']
                    prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1
            
            return {
                "document_count": len(results.get('documents', [])),
                "metadata_keys": list(metadatas[0].keys()) if metadatas else [],
                "prefixes": list(set([meta.get('prefix', '') for meta in metadatas if meta])),
                "prefix_counts": prefix_counts
            }
        except Exception as e:
            print(f"獲取集合資訊時發生錯誤: {e}")
            return {}
    
    def delete_document(self, filename: str):
        """
        刪除指定文件
        
        Args:
            filename: 檔案名稱
        """
        try:
            self.vectorstore.delete(ids=[filename])
            print(f"已刪除文件: {filename}")
        except Exception as e:
            print(f"刪除文件時發生錯誤: {e}")
    
    def delete_documents_by_prefix(self, prefix: str):
        """
        按前綴刪除文件
        
        Args:
            prefix: 前綴（application, development, model）
        """
        try:
            # 獲取指定前綴的文件 ID
            results = self.vectorstore.get(include=['metadatas'], where={"prefix": prefix})
            filenames = [meta.get('filename') for meta in results.get('metadatas', []) if meta]
            
            if filenames:
                self.vectorstore.delete(ids=filenames)
                print(f"已刪除 {len(filenames)} 個 {prefix} 文件")
            else:
                print(f"沒有找到 {prefix} 文件")
        except Exception as e:
            print(f"刪除文件時發生錯誤: {e}")


def main():
    """主程式 - 索引資料"""
    print("=== 資料索引器 (增量 Upsert) ===")
    
    # 檢查環境變數
    if not os.environ.get("AZURE_OPENAI_API_KEY"):
        print("錯誤: 請設定 AZURE_OPENAI_API_KEY 環境變數")
        return
    
    # 初始化索引器
    indexer = DataIndexer()
    
    # 顯示初始集合資訊
    initial_info = indexer.get_collection_info()
    print(f"初始集合資訊: {initial_info}")
    
    # 載入文件
    print("\n正在載入文件...")
    documents = indexer.load_documents()
    
    # 增量 upsert 到向量資料庫
    print("\n正在進行增量 upsert...")
    indexer.upsert_documents(documents)
    
    # 顯示最終集合資訊
    final_info = indexer.get_collection_info()
    print(f"\n最終集合資訊: {final_info}")
    print("索引完成！")


if __name__ == "__main__":
    main() 