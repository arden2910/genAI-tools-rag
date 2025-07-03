#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
驗證問題集生成器
使用 LangChain 進行批次相關性評估，生成評估用的問題集
"""

import os
import yaml
import json
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

# LangChain imports
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_openai.embeddings import AzureOpenAIEmbeddings
from langchain_openai.chat_models import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import JsonOutputParser
from tqdm import tqdm

# 載入環境變數
load_dotenv()

class EvalGenerator:
    def __init__(self, 
                 data_dir: str = r"C:\Users\ardenlo\Dropbox\genAI-tools-rag\data\cleaned",
                 chroma_dir: str = r"C:\Users\ardenlo\Dropbox\genAI-tools-rag\chroma_db",
                 eval_dir: str = r"C:\Users\ardenlo\Dropbox\genAI-tools-rag\eval",
                 report_dir: str = r"C:\Users\ardenlo\Dropbox\genAI-tools-rag\report",
                 collection_name: str = "genai_tools"):
        """
        初始化驗證生成器
        
        Args:
            data_dir: 資料來源目錄
            chroma_dir: Chroma 資料庫目錄
            eval_dir: 評估結果目錄
            report_dir: 報告目錄
            collection_name: Chroma 集合名稱
        """
        self.data_dir = Path(data_dir)
        self.chroma_dir = Path(chroma_dir)
        self.eval_dir = Path(eval_dir)
        self.report_dir = Path(report_dir)
        self.collection_name = collection_name
        
        # 確保評估目錄和報告目錄存在
        self.eval_dir.mkdir(parents=True, exist_ok=True)
        self.report_dir.mkdir(parents=True, exist_ok=True)
        
        # 初始化 Azure OpenAI 配置
        self.azure_configs = {
            "base_url": "https://iii-azure-openai-eastus.openai.azure.com/",
            "embedding_name": "text-embedding-3-small",
            'api_key': os.environ.get("AZURE_OPENAI_API_KEY"),
            "api_version": "2024-05-01-preview",
            "model_name": "gpt-4o"
        }
        
        # 初始化模型和向量資料庫
        self._init_models()
        self._init_vectorstore()
        self._init_evaluation_chain()
        
        # 初始化 Excel 記錄列表
        self.excel_records = []
    
    def _init_models(self):
        """初始化模型"""
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
            api_version=self.azure_configs["api_version"],
        )
    
    def _init_vectorstore(self):
        """初始化 Chroma 向量資料庫"""
        self.vectorstore = Chroma(
            collection_name=self.collection_name,
            embedding_function=self.embeddings,
            persist_directory=str(self.chroma_dir),
        )
    
    def _init_evaluation_chain(self):
        """初始化評估鏈"""
        # 評估模板
        self.evaluation_template = """
你現在的任務是評估「問題」與「內容片段（chunk）」之間的主題相關性，並以 1–10 的整數給分（10 = 完全相關，1 = 完全無關）。請遵守以下指引：

| 分數   | 判準    | 說明                                       |
| ---- | ----- | ---------------------------------------- |
| 7–10  | 高度相關  | chunk 提供關鍵資訊且與問題緊密相扣，幾乎完整、精確地回應了問題核心，或直接提供問題所需的主要資訊／解答。       |
| 6  | 中度相關  | chunk 與問題有明確交集，但資訊片段零散、或只能回答問題的一小部分。     |
| 2–5  | 低度相關  | chunk 僅輕微提及相關主題，無法實質回應問題。                |
| 1    | 完全無關  | chunk 與問題主題幾乎無交集。                        |

問題：{question}

內容片段：{content}

1. 問題折解
請先將「問題」拆解成一個或多個更細的子問題、需求或核心元素，以捕捉問題的重點。例如：
問題：「我需要做一個可電話通話的 AI 機器人」
折解成：
「有哪些 ASR（語音辨識）服務可用？」
「有哪些 TTS（語音合成）服務可用？」
「如何將 ASR、LLM、TTS 串成電話通話流程？」

2. 進行相關性評估
逐一檢視 chunk 是否有回應到上述折解後的子問題或重點。
給出 1–10 的整數分數。
說明你為什麼這樣評分。



請以 JSON 格式回應，結構如下：
{{
    "relevance": {{
        "question_breakdown": [
            "折解後子問題或重點1",
            "折解後子問題或重點2",
            "... (可多筆)"
        ],
        "reason": "評估理由",
        "score": 分數
    }}
}}
"""
        
        # 建立評估鏈
        self.evaluation_chain = (
            ChatPromptTemplate.from_template(self.evaluation_template)
            | self.llm
            | JsonOutputParser()
        )
    
    def batch_evaluate_relevance(self, questions: List[str], contents: List[str]) -> List[Dict[str, Any]]:
        """
        批次評估問題與內容的相關性
        
        Args:
            questions: 問題列表
            contents: 內容列表
            
        Returns:
            評估結果列表
        """
        try:
            # 批次處理
            batch_size = 10  # 每次處理 5 個樣本
            results = []
            
            for i in tqdm(range(0, len(questions), batch_size), desc="批次評估"):
                batch_questions = questions[i:i + batch_size]
                batch_contents = contents[i:i + batch_size]
                
                # 建立批次輸入
                batch_inputs = []
                for q, c in zip(batch_questions, batch_contents):
                    batch_inputs.append({
                        "question": q,
                        "content": c
                    })
                
                # 批次評估
                batch_results = self.evaluation_chain.batch(batch_inputs)
                results.extend(batch_results)
            
            return results
            
        except Exception as e:
            print(f"批次評估時發生錯誤: {e}")
            return [{"relevance": {"question_breakdown": [], "reason": "評估失敗", "score": 1}}] * len(questions)
    
    def load_questions_from_json(self, json_file: str) -> Tuple[List[Dict[str, Any]], float]:
        """
        從 JSON 檔案載入問題和 threshold
        
        Args:
            json_file: JSON 檔案路徑
            
        Returns:
            (問題列表, threshold值)
        """
        json_path = self.eval_dir / json_file
        if not json_path.exists():
            print(f"JSON 檔案不存在: {json_path}")
            return [], 0.4
        
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            questions = data.get('questions', [])
            threshold = data.get('threshold', 0.4)
            print(f"從 JSON 載入 {len(questions)} 個問題，threshold: {threshold}")
            return questions, threshold
        except Exception as e:
            print(f"載入 JSON 檔案時發生錯誤: {e}")
            return [], 0.4
    
    def save_excel_report(self, name: str = "eval_report"):
        """
        儲存 Excel 報告
        
        Args:
            name: 報告名稱
        """
        if not self.excel_records:
            print("沒有記錄可儲存")
            return
        
        # 建立 DataFrame
        df = pd.DataFrame(self.excel_records)
        
        # 生成檔案名稱
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{name}.xlsx"
        filepath = self.report_dir / filename
        
        try:
            # 儲存到 Excel
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='評估結果', index=False)
            
            print(f"Excel 報告已儲存: {filepath}")
            print(f"總共記錄了 {len(self.excel_records)} 筆評估結果")
        except Exception as e:
            print(f"儲存 Excel 報告時發生錯誤: {e}")
    
    def process_questions(self, json_file: str, output_file: Optional[str] = None):
        """
        處理問題集，生成驗證結果
        
        Args:
            json_file: 輸入 JSON 檔案
            output_file: 輸出 JSON 檔案
        """
        # 清空之前的記錄
        self.excel_records = []
        
        # 載入問題
        questions, threshold = self.load_questions_from_json(json_file)
        if not questions:
            return
        
        # 載入所有清理後的文件
        cleaned_files = list(self.data_dir.rglob("*.txt"))
        print(f"找到 {len(cleaned_files)} 個清理後的文件")
        
        # 處理每個問題
        updated_questions = []
        
        for i, question_data in enumerate(questions, 1):
            question = question_data.get('question', '')
            if not question:
                continue
            
            print(f"處理問題 {i}/{len(questions)}: {question[:50]}...")
            
            # 檢查 expected_chunks 是否為空
            expected_chunks = question_data.get('expected_chunks', [])
            
            if not expected_chunks:
                print("  expected_chunks 為空，開始評估文件相關性...")
                
                # 批次處理：準備所有問題和文件內容
                batch_questions = []
                batch_contents = []
                file_paths = []
                
                print(f"  準備批次處理 {len(cleaned_files)} 個文件...")
                for file_path in cleaned_files:
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        batch_questions.append(question)
                        batch_contents.append(content)
                        file_paths.append(file_path)
                        
                    except Exception as e:
                        print(f"    處理文件 {file_path} 時發生錯誤: {e}")
                
                # 批次評估相關性
                print(f"  開始批次評估相關性...")
                evaluation_results = self.batch_evaluate_relevance(batch_questions, batch_contents)
                
                # 找出相關文件並記錄到 Excel
                relevant_files = []
                for i, (file_path, result) in enumerate(zip(file_paths, evaluation_results)):
                    try:
                        score = result.get('relevance', {}).get('score', 1)
                        file_id = file_path.name
                        
                        # 記錄到 Excel 列表
                        question_breakdown = result.get('relevance', {}).get('question_breakdown', [])
                        breakdown_text = '; '.join(question_breakdown) if question_breakdown else ''
                        
                        self.excel_records.append({
                            '是否高於threshold': '是' if score >= threshold else '否',
                            '問題': question,
                            '文件名': file_id,
                            '分數': score,
                            '問題拆解': breakdown_text,
                            '評估理由': result.get('relevance', {}).get('reason', '')
                        })
                        
                        if score >= threshold:
                            relevant_files.append({
                                'id': file_id,
                                'score': score,
                                'path': str(file_path),
                                'reason': result.get('relevance', {}).get('reason', '')
                            })
                            print(f"    發現相關文件: {file_id} (分數: {score})")
                    except Exception as e:
                        print(f"    處理評估結果時發生錯誤: {e}")
                

                
                # 更新 expected_chunks
                expected_chunks = [f['id'] for f in relevant_files]
                print(f"  自動發現 {len(expected_chunks)} 個相關文件")
            
            # 建立更新的問題資料（用於儲存回 YAML）
            updated_question = {
                'question': question,
                'expected_chunks': expected_chunks
            }
            updated_questions.append(updated_question)
            
            # 每處理完一個問題就儲存一次
            self._save_yaml(json_file, updated_questions, questions, threshold)
        
        # 儲存 Excel 報告
        self.save_excel_report("eval_generator")
        
        print("所有問題處理完成！")
    
    def _save_yaml(self, json_file: str, updated_questions: List[Dict], original_questions: List[Dict], threshold: float):
        """儲存 YAML 檔案"""
        json_path = self.eval_dir / json_file
        try:
            # 準備完整的資料結構
            output_data = {
                'threshold': threshold,
                'questions': updated_questions
            }
            
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, ensure_ascii=False, indent=2)
            print(f"已更新 JSON 檔案: {json_path}")
        except Exception as e:
            print(f"更新 JSON 檔案時發生錯誤: {e}")
    
    def create_sample_yaml(self, filename: str = "sample_questions.json"):
        """
        建立範例 JSON 檔案
        
        Args:
            filename: 檔案名稱
        """
        sample_data = {
            'threshold': 0.7,
            'questions': [
                {'question': '有哪些語音生成工具？', 'expected_chunks': []},
                {'question': '有哪些圖片生成工具？', 'expected_chunks': []},
            ]
        }
        
        output_path = self.eval_dir / filename
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(sample_data, f, ensure_ascii=False, indent=2)
            print(f"範例 JSON 檔案已建立: {output_path}")
        except Exception as e:
            print(f"建立範例檔案時發生錯誤: {e}")


def main():
    """主程式"""
    print("=== 驗證問題集生成器 ===")
    
    # 檢查環境變數
    if not os.environ.get("AZURE_OPENAI_API_KEY"):
        print("錯誤: 請設定 AZURE_OPENAI_API_KEY 環境變數")
        return
    
    # 初始化生成器
    generator = EvalGenerator()
    
    # 檢查是否有現有的問題集
    json_files = list(generator.eval_dir.glob("*.json"))
    
    if not json_files:
        print("沒有找到 JSON 問題集，建立範例檔案...")
        generator.create_sample_yaml()
        print("請編輯 sample_questions.json 檔案，然後重新執行程式")
        return
    
    print("找到以下 JSON 檔案:")
    for i, json_file in enumerate(json_files, 1):
        print(f"  {i}. {json_file.name}")
    
    # 選擇要處理的檔案
    try:
        choice = input("\n請選擇要處理的檔案 (輸入編號): ").strip()
        choice_idx = int(choice) - 1
        
        if 0 <= choice_idx < len(json_files):
            selected_file = json_files[choice_idx].name
            print(f"選擇處理: {selected_file}")
            
            # 處理問題集
            
            generator.process_questions(selected_file)
        else:
            print("無效的選擇")
    except (ValueError, IndexError):
        print("無效的輸入")
    except KeyboardInterrupt:
        print("\n操作已取消")


if __name__ == "__main__":
    main() 