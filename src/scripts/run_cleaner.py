#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
洗資料程式執行腳本
直接執行，無需命令列參數
"""

import os
import sys
from pathlib import Path

# 添加 src 目錄到 Python 路徑
src_dir = Path(__file__).parent.parent  # 回到 src 目錄
sys.path.insert(0, str(src_dir))

from ..data_cleaner import DataCleaner

def main():
    """主程式"""
    # 設定路徑
    project_root = Path(__file__).parent.parent.parent  # 回到專案根目錄
    
    input_dir = r"C:\Users\ardenlo\Dropbox\genAI-tools-rag\data\edit\tools"
    output_dir = project_root / "data" / "cleaned"
    
    print("=== 洗資料程式 ===")
    print(f"輸入目錄: {input_dir}")
    print(f"輸出目錄: {output_dir}")
    print()
    
    # 建立洗資料程式實例並執行
    cleaner = DataCleaner(input_dir, str(output_dir))
    cleaner.process_directory()
    
    print("\n=== 處理完成 ===")

if __name__ == "__main__":
    main() 