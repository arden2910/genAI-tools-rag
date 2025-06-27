#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
洗資料程式執行腳本
直接執行，無需命令列參數
"""

from data_cleaner import DataCleaner
import os

def main():
    """主程式"""
    # 設定路徑
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    
    input_dir = r"C:\Users\ardenlo\Dropbox\genAI-tools-rag\data\edit\tools"
    output_dir = os.path.join(project_root, "data", "cleaned")
    
    print("=== 洗資料程式 ===")
    print(f"輸入目錄: {input_dir}")
    print(f"輸出目錄: {output_dir}")
    print()
    
    # 建立洗資料程式實例並執行
    cleaner = DataCleaner(input_dir, output_dir)
    cleaner.process_directory()
    
    print("\n=== 處理完成 ===")

if __name__ == "__main__":
    main() 