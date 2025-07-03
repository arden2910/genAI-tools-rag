#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RAG 系統評估器
用於驗證 RAG 系統的 recall 和 precision
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Tuple
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

from vector_rag import Retriever

# 載入環境變數
load_dotenv()

class RAGEvaluator:
    def __init__(self, 
                 questions_file: str = r"C:\Users\ardenlo\Dropbox\genAI-tools-rag\eval\sample_questions.json"):
        """
        初始化 RAG 評估器
        
        Args:
            questions_file: 包含測試問題的 JSON 檔案路徑
        """
        self.questions_file = Path(questions_file)
        self.retriever = Retriever()
        self.questions_data = self._load_questions()
    
    def _load_questions(self) -> Dict:
        """載入測試問題"""
        try:
            with open(self.questions_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"載入問題檔案時發生錯誤: {e}")
            return {"threshold": 0.4, "questions": []}
    
    def calculate_metrics(self, 
                         retrieved_files: List[str], 
                         expected_files: List[str]) -> Dict[str, float]:
        """
        計算 recall 和 precision
        
        Args:
            retrieved_files: RAG 系統檢索到的檔案列表
            expected_files: 期望的檔案列表
            
        Returns:
            包含 recall, precision, f1_score 的字典
        """
        # 轉換為集合以便計算
        retrieved_set = set(retrieved_files)
        expected_set = set(expected_files)
        
        # 計算交集
        intersection = retrieved_set.intersection(expected_set)
        
        # 計算 metrics
        if len(expected_set) == 0:
            recall = 0.0
        else:
            recall = len(intersection) / len(expected_set)
        
        if len(retrieved_set) == 0:
            precision = 0.0
        else:
            precision = len(intersection) / len(retrieved_set)
        
        # 計算 F1 score
        if precision + recall == 0:
            f1_score = 0.0
        else:
            f1_score = 2 * (precision * recall) / (precision + recall)
        
        return {
            'recall': recall,
            'precision': precision,
            'f1_score': f1_score,
            'retrieved_count': len(retrieved_set),
            'expected_count': len(expected_set),
            'intersection_count': len(intersection)
        }
    
    def evaluate_single_question(self, 
                                question: str, 
                                expected_files: List[str], 
                                k: int = 10) -> Dict:
        """
        評估單一問題
        
        Args:
            question: 問題文字
            expected_files: 期望的檔案列表
            k: 檢索結果數量
            
        Returns:
            評估結果字典
        """
        print(f"\n=== 評估問題: {question} ===")
        
        # 使用 RAG 系統搜尋
        results = self.retriever.similarity_search_with_metadata(question, k=k)
        retrieved_files = self.retriever.get_filenames_from_results(results)
        
        print(f"檢索到的檔案 ({len(retrieved_files)}):")
        for i, filename in enumerate(retrieved_files, 1):
            print(f"  {i}. {filename}")
        
        print(f"\n期望的檔案 ({len(expected_files)}):")
        for i, filename in enumerate(expected_files, 1):
            print(f"  {i}. {filename}")
        
        # 計算 metrics
        metrics = self.calculate_metrics(retrieved_files, expected_files)
        
        print(f"\n評估結果:")
        print(f"  Recall: {metrics['recall']:.3f}")
        print(f"  Precision: {metrics['precision']:.3f}")
        print(f"  F1 Score: {metrics['f1_score']:.3f}")
        print(f"  交集數量: {metrics['intersection_count']}")
        
        return {
            'question': question,
            'retrieved_files': retrieved_files,
            'expected_files': expected_files,
            'metrics': metrics
        }
    
    def evaluate_all_questions(self, k: int = 10) -> Dict:
        """
        評估所有問題
        
        Args:
            k: 每個問題檢索的結果數量
            
        Returns:
            整體評估結果
        """
        print("=== RAG 系統評估開始 ===")
        
        all_results = []
        total_recall = 0.0
        total_precision = 0.0
        total_f1 = 0.0
        
        for question_data in self.questions_data['questions']:
            question = question_data['question']
            expected_files = question_data['expected_chunks']
            
            result = self.evaluate_single_question(question, expected_files, k)
            all_results.append(result)
            
            # 累計 metrics
            metrics = result['metrics']
            total_recall += metrics['recall']
            total_precision += metrics['precision']
            total_f1 += metrics['f1_score']
        
        # 計算平均 metrics
        num_questions = len(self.questions_data['questions'])
        avg_recall = total_recall / num_questions if num_questions > 0 else 0.0
        avg_precision = total_precision / num_questions if num_questions > 0 else 0.0
        avg_f1 = total_f1 / num_questions if num_questions > 0 else 0.0
        
        overall_results = {
            'total_questions': num_questions,
            'average_recall': avg_recall,
            'average_precision': avg_precision,
            'average_f1_score': avg_f1,
            'individual_results': all_results
        }
        
        print(f"\n=== 整體評估結果 ===")
        print(f"總問題數: {num_questions}")
        print(f"平均 Recall: {avg_recall:.3f}")
        print(f"平均 Precision: {avg_precision:.3f}")
        print(f"平均 F1 Score: {avg_f1:.3f}")
        
        return overall_results
    
    def save_results(self, results: Dict, output_file: str = "rag_evaluation_results.json"):
        """儲存評估結果"""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f"\n評估結果已儲存至: {output_file}")
        except Exception as e:
            print(f"儲存結果時發生錯誤: {e}")

    def save_results_to_excel(self, results: Dict, output_file: str = None):
        """儲存評估結果到 Excel"""
        try:
            # 生成檔案名稱
            if output_file is None:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                output_file = f"vector_rag_evaluation_{timestamp}_top20.xlsx"
            
            # 確保輸出目錄存在
            report_dir = Path(r"C:\Users\ardenlo\Dropbox\genAI-tools-rag\report")
            report_dir.mkdir(exist_ok=True)
            output_path = report_dir / output_file
            
            # 準備資料
            excel_data = []
            
            for result in results['individual_results']:
                metrics = result['metrics']
                row = {
                    '問題': result['question'],
                    'Recall': metrics['recall'],
                    'Precision': metrics['precision'],
                    'F1_Score': metrics['f1_score'],
                    '檢索數量': metrics['retrieved_count'],
                    '期望數量': metrics['expected_count'],
                    '交集數量': metrics['intersection_count'],
                    '檢索檔案': ', '.join(result['retrieved_files']),
                    '期望檔案': ', '.join(result['expected_files']),
                    '評估時間': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                excel_data.append(row)
            
            # 添加整體統計
            summary_row = {
                '問題': '整體平均',
                'Recall': results['average_recall'],
                'Precision': results['average_precision'],
                'F1_Score': results['average_f1_score'],
                '檢索數量': '-',
                '期望數量': '-',
                '交集數量': '-',
                '檢索檔案': f"總問題數: {results['total_questions']}",
                '期望檔案': '-',
                '評估時間': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            excel_data.append(summary_row)
            
            # 轉換為 DataFrame 並儲存
            df = pd.DataFrame(excel_data)
            df.to_excel(output_path, index=False, sheet_name='RAG評估結果')
            
            print(f"\n評估結果已儲存至: {output_path}")
            
        except Exception as e:
            print(f"儲存 Excel 結果時發生錯誤: {e}")
            import traceback
            traceback.print_exc()


def main():
    """主程式"""
    print("=== RAG 系統評估器 ===")
    
    # 檢查環境變數
    if not os.environ.get("AZURE_OPENAI_API_KEY"):
        print("錯誤: 請設定 AZURE_OPENAI_API_KEY 環境變數")
        return
    
    # 初始化評估器
    evaluator = RAGEvaluator()
    
    # 檢查問題檔案
    if not evaluator.questions_file.exists():
        print(f"錯誤: 找不到問題檔案 {evaluator.questions_file}")
        return
    
    # 執行評估
    results = evaluator.evaluate_all_questions(k=20)
    
    # 儲存結果
    evaluator.save_results(results)
    evaluator.save_results_to_excel(results)


if __name__ == "__main__":
    main() 