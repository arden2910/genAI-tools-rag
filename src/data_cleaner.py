#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
洗資料程式
處理 markdown 檔案中的區塊，用 --- 分隔，並輸出到 cleaned 目錄
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Any
import argparse
from datetime import datetime


class DataCleaner:
    def __init__(self, input_dir: str, output_dir: str):
        """
        初始化洗資料程式
        
        Args:
            input_dir: 輸入目錄路徑
            output_dir: 輸出目錄路徑
        """
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        
        # 確保輸出目錄存在
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def read_markdown_file(self, file_path: Path) -> str:
        """
        讀取 markdown 檔案內容
        
        Args:
            file_path: 檔案路徑
            
        Returns:
            檔案內容
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"讀取檔案 {file_path} 時發生錯誤: {e}")
            return ""
    
    def extract_blocks(self, content: str) -> List[str]:
        """
        從 markdown 內容中提取用 --- 分隔的區塊
        
        Args:
            content: markdown 內容
            
        Returns:
            區塊列表
        """
        # 使用 --- 作為分隔符號分割內容
        blocks = re.split(r'\n\s*---\s*\n', content)
        
        # 過濾空區塊並清理
        cleaned_blocks = []
        for block in blocks:
            block = block.strip()
            if block and not block.isspace():
                cleaned_blocks.append(block)
        
        return cleaned_blocks
    
    def clean_block_content(self, block: str) -> str:
        """
        清理區塊內容，移除不必要的標記和格式
        
        Args:
            block: 原始區塊內容
            
        Returns:
            清理後的區塊內容
        """
        # 移除 HTML 標籤
        block = re.sub(r'<[^>]+>', '', block)
        
        # 移除 markdown 標題標記
        block = re.sub(r'^#+\s*', '', block, flags=re.MULTILINE)
        
        # 移除 badge 標記
        block = re.sub(r'!\[.*?\]\(.*?\)', '', block)
        
        # 清理多餘的空白行
        block = re.sub(r'\n\s*\n\s*\n', '\n\n', block)
        
        # 移除開頭和結尾的空白
        block = block.strip()
        
        return block
    
    def get_block_title(self, block: str) -> str:
        """
        從區塊中提取標題作為檔案名稱
        
        Args:
            block: 區塊內容
            
        Returns:
            清理後的標題
        """
        # 尋找第一行作為標題
        lines = block.split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('**') and not line.startswith('-'):
                # 先嘗試保留 emoji 和中文
                title = re.sub(r'[<>:"/\\|?*]', '', line)  # 只移除檔案系統不允許的字符
                title = title.strip()
                if title:
                    # 如果標題太長，截斷並保留有意義的部分
                    if len(title) > 50:
                        # 嘗試在空格處截斷
                        words = title.split()
                        truncated = ""
                        for word in words:
                            if len(truncated + " " + word) <= 50:
                                truncated += (" " + word) if truncated else word
                            else:
                                break
                        title = truncated
                    return title
        
        # 如果還是找不到標題，使用區塊的前幾個字符
        if block.strip():
            # 取前30個字符作為標題
            fallback_title = block.strip()[:30]
            # 清理檔案系統不允許的字符
            fallback_title = re.sub(r'[<>:"/\\|?*]', '', fallback_title)
            fallback_title = fallback_title.strip()
            if fallback_title:
                return fallback_title
        
        return "untitled"
    
    def save_block_to_file(self, block: str, output_file: Path):
        """
        將單個區塊保存到檔案
        
        Args:
            block: 區塊內容
            output_file: 輸出檔案路徑
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(block)
            
            print(f"已保存區塊到 {output_file}")
        except Exception as e:
            print(f"保存檔案 {output_file} 時發生錯誤: {e}")
    
    def process_file(self, file_path: Path, date_folder: Path):
        """
        處理單個 markdown 檔案
        
        Args:
            file_path: 檔案路徑
            date_folder: 日期資料夾路徑
        """
        print(f"處理檔案: {file_path}")
        
        # 讀取檔案內容
        content = self.read_markdown_file(file_path)
        if not content:
            return
        
        # 提取區塊
        blocks = self.extract_blocks(content)
        print(f"找到 {len(blocks)} 個區塊")
        
        # 取得前綴（檔案名稱）
        prefix = file_path.stem
        
        # 處理每個區塊
        saved_count = 0
        for i, block in enumerate(blocks, 1):
            cleaned_block = self.clean_block_content(block)
            if cleaned_block:
                # 提取標題作為檔案名稱
                title = self.get_block_title(cleaned_block)
                # 建立安全的檔案名稱
                safe_title = re.sub(r'[<>:"/\\|?*]', '_', title)
                safe_title = safe_title.replace(' ', '_')
                
                # 生成檔案名稱：前綴_序號_標題.txt
                filename = f"{prefix}_{i:02d}_{safe_title}.txt"
                output_file = date_folder / filename
                
                # 保存區塊
                self.save_block_to_file(cleaned_block, output_file)
                saved_count += 1
        
        print(f"已保存 {saved_count} 個區塊到 {date_folder}")
    
    def process_directory(self):
        """
        處理整個目錄中的所有 markdown 檔案
        """
        print(f"開始處理目錄: {self.input_dir}")
        print(f"輸出目錄: {self.output_dir}")
        
        # 建立日期資料夾
        today = datetime.now()
        date_folder_name = today.strftime("%m.%d")  # 格式：06.27
        date_folder = self.output_dir / date_folder_name
        date_folder.mkdir(exist_ok=True)
        
        print(f"日期資料夾: {date_folder}")
        
        # 尋找所有 .md 檔案
        md_files = list(self.input_dir.glob("*.md"))
        
        if not md_files:
            print(f"在 {self.input_dir} 中沒有找到 .md 檔案")
            return
        
        print(f"找到 {len(md_files)} 個 markdown 檔案")
        
        # 處理每個檔案
        for file_path in md_files:
            self.process_file(file_path, date_folder)
        
        print("所有檔案處理完成！")


def main():
    """主程式"""
    parser = argparse.ArgumentParser(description="洗資料程式 - 處理 markdown 檔案中的區塊")
    parser.add_argument(
        "--input", 
        default=r"C:\Users\ardenlo\Dropbox\genAI-tools-rag\data\edit\tools",
        help="輸入目錄路徑"
    )
    parser.add_argument(
        "--output", 
        default="data/cleaned",
        help="輸出目錄路徑"
    )
    
    args = parser.parse_args()
    
    # 建立洗資料程式實例
    cleaner = DataCleaner(args.input, args.output)
    
    # 處理目錄
    cleaner.process_directory()


if __name__ == "__main__":
    main() 