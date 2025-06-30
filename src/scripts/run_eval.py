#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
執行 RAG 系統評估的腳本
支援多輪測試和 Excel 輸出
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# 添加 src 目錄到 Python 路徑
src_dir = Path(__file__).parent.parent  # 回到 src 目錄
sys.path.insert(0, str(src_dir))

from ..rag_evaluator import RAGEvaluator

def create_report_directory():
    """建立報告目錄"""
    report_dir = Path(__file__).parent.parent.parent / "report"  # 回到專案根目錄
    report_dir.mkdir(exist_ok=True)
    return report_dir

def get_test_name():
    """取得測試名稱"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"rag_evaluation_{timestamp}"

def run_single_test(evaluator: RAGEvaluator, k: int, test_name: str, report_dir: Path):
    """執行單次測試"""
    print(f"\n=== 執行測試: Top {k} ===")
    
    # 執行評估
    results = evaluator.evaluate_all_questions(k=k)
    
    # 儲存 JSON 結果
    json_file = report_dir / f"{test_name}_top{k}.json"
    evaluator.save_results(results, str(json_file))
    
    # 儲存 Excel 結果
    excel_file = report_dir / f"{test_name}_top{k}.xlsx"
    evaluator.save_results_to_excel(results, str(excel_file))
    
    print(f"測試完成！")
    print(f"  JSON 結果: {json_file}")
    print(f"  Excel 結果: {excel_file}")
    
    return results

def main():
    """主程式"""
    print("=== RAG 系統多輪評估 ===")
    
    # 檢查環境變數
    if not os.environ.get("AZURE_OPENAI_API_KEY"):
        print("錯誤: 請設定 AZURE_OPENAI_API_KEY 環境變數")
        print("請在 .env 檔案中設定您的 API 金鑰")
        return
    
    try:
        # 建立報告目錄
        report_dir = create_report_directory()
        
        # 初始化評估器
        evaluator = RAGEvaluator()
        
        # 檢查問題檔案
        if not evaluator.questions_file.exists():
            print(f"錯誤: 找不到問題檔案 {evaluator.questions_file}")
            return
        
        # 取得測試名稱
        test_name = get_test_name()
        print(f"測試名稱: {test_name}")
        print(f"報告目錄: {report_dir}")
        
        # 顯示選項
        print("\n請選擇測試模式:")
        print("1. 單次測試 (Top 10)")
        print("2. 單次測試 (Top 20)")
        print("3. 多輪測試 (Top 10 + Top 20)")
        print("4. 自訂 Top K 測試")
        print("5. 退出")
        
        while True:
            try:
                choice = input("\n請輸入選項 (1-5): ").strip()
                
                if choice == "1":
                    # 單次測試 Top 10
                    run_single_test(evaluator, 10, test_name, report_dir)
                    break
                    
                elif choice == "2":
                    # 單次測試 Top 20
                    run_single_test(evaluator, 20, test_name, report_dir)
                    break
                    
                elif choice == "3":
                    # 多輪測試
                    print(f"\n=== 執行多輪測試 ===")
                    results_10 = run_single_test(evaluator, 10, test_name, report_dir)
                    results_20 = run_single_test(evaluator, 20, test_name, report_dir)
                    
                    # 比較結果
                    print(f"\n=== 結果比較 ===")
                    print(f"Top 10 - Recall: {results_10['average_recall']:.3f}, Precision: {results_10['average_precision']:.3f}, F1: {results_10['average_f1_score']:.3f}")
                    print(f"Top 20 - Recall: {results_20['average_recall']:.3f}, Precision: {results_20['average_precision']:.3f}, F1: {results_20['average_f1_score']:.3f}")
                    break
                    
                elif choice == "4":
                    # 自訂 Top K 測試
                    try:
                        k = int(input("請輸入 Top K 值: "))
                        if k > 0:
                            run_single_test(evaluator, k, test_name, report_dir)
                        else:
                            print("請輸入正整數")
                            continue
                    except ValueError:
                        print("請輸入有效的數字")
                        continue
                    break
                    
                elif choice == "5":
                    print("退出程式")
                    return
                    
                else:
                    print("無效的選項，請輸入 1-5")
                    
            except KeyboardInterrupt:
                print("\n\n操作已取消")
                return
            except Exception as e:
                print(f"發生錯誤: {e}")
                continue
        
        print(f"\n所有測試完成！結果已儲存至: {report_dir}")
        
    except Exception as e:
        print(f"執行評估時發生錯誤: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 