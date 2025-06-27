# 洗資料程式

這個程式用於處理 markdown 檔案中的區塊，將用 `---` 分隔的內容提取出來並清理格式。

## 功能特色

- 自動讀取指定目錄中的所有 `.md` 檔案
- 使用 `---` 作為分隔符號提取區塊
- 清理 HTML 標籤、markdown 標記和 badge 標記
- 將每個區塊保存為獨立的 `.txt` 檔案
- 支援 UTF-8 編碼
- 自動建立日期資料夾組織檔案

## 檔案結構

```
src/
├── data_cleaner.py    # 主要的洗資料程式
├── run_cleaner.py     # 簡化的執行腳本
└── README.md         # 說明文件
```

## 使用方法

### 方法一：使用簡化腳本（推薦）

```bash
cd src
python run_cleaner.py
```

### 方法二：使用主程式（可自訂參數）

```bash
cd src
python data_cleaner.py --input "輸入目錄路徑" --output "輸出目錄路徑"
```

## 預設設定

- **輸入目錄**: `C:\Users\ardenlo\Dropbox\genAI-tools-rag\data\edit\tools`
- **輸出目錄**: `data/cleaned`

## 輸出格式

程式會自動建立以當前日期命名的資料夾，並將所有區塊檔案集中在該資料夾下：

```
data/cleaned/
└── 06.27/                    # 日期資料夾 (月.日 格式)
    ├── application_01_工具列表.txt
    ├── application_02_Microsoft_Copilot.txt
    ├── application_03_Gamma.txt
    ├── development_01_區塊標題1.txt
    ├── development_02_區塊標題2.txt
    ├── model_01_區塊標題1.txt
    ├── model_02_區塊標題2.txt
    └── ...
```

### 檔案命名規則

- 格式：`前綴_序號_標題.txt`
- 前綴：原始 markdown 檔案名稱（application, development, model）
- 序號：兩位數字（01, 02, 03...）
- 標題：從區塊內容中提取的第一行文字
- 特殊字符會被替換為底線
- 檔案名稱長度限制在 50 個字符內

### 日期資料夾命名

- 格式：`月.日`（例如：06.27, 12.25）
- 使用當前系統日期自動建立

## 清理規則

程式會自動清理以下內容：

1. HTML 標籤（如 `<h3>`, `<p>` 等）
2. Markdown 標題標記（如 `#`, `##` 等）
3. Badge 標記（如 `![標籤](連結)`）
4. 多餘的空白行
5. 開頭和結尾的空白

## 範例

假設您有以下 markdown 內容：

```markdown
<h3 id="tool-name">工具名稱</h3>

![標籤](連結)

**簡介**
這是工具的簡介

---

<h3 id="another-tool">另一個工具</h3>

**功能**
這是功能描述
```

處理後會產生兩個檔案（假設今天是 06.27）：

**data/cleaned/06.27/application_01_工具名稱.txt**
```
工具名稱

簡介
這是工具的簡介
```

**data/cleaned/06.27/application_02_另一個工具.txt**
```
另一個工具

功能
這是功能描述
```

## 需求

- Python 3.6+
- 標準函式庫（無需額外安裝套件）

## 注意事項

- 確保輸入目錄存在且包含 `.md` 檔案
- 程式會自動建立輸出目錄和日期資料夾（如果不存在）
- 所有檔案都使用 UTF-8 編碼處理
- 如果輸出檔案已存在，會被覆寫
- 每個區塊的標題會自動提取作為檔案名稱
- 日期資料夾使用當前系統日期 