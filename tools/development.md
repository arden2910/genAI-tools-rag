# ⚙️ GenAI開發工具清單

## 📚 目錄
- [快速索引](#快速索引)
- [工具列表](#工具列表)

## 🚀 快速索引

- 依**研發據點**
	- [台灣](../tags/development/region.md#taiwan)
	- [國際](../tags/development/region.md#international)
- 依**開源狀態**
	- [開源](../tags/development/license.md#opensource)
	- [閉源](../tags/development/license.md#closedsource)

## 📋 工具列表
<!-- INSERTION_MARKER -->

<h3 id="cohere">Cohere</h3>

![開發平台](https://img.shields.io/badge/-%E9%96%8B%E7%99%BC%E5%B9%B3%E5%8F%B0-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

領先的企業AI平台，專注於企業生成式AI、搜索發現和進階檢索功能。基於商業語言優化，提供企業級解決方案。

**基本資訊**
- 🔗 官網：https://cohere.com
- 💻 API支援：✅ 提供
- 🌐 研發據點：加拿大、美國
- 💰 計費方式：依使用量
- 📋 價格方案：https://cohere.com/pricing

**特色功能**
- 企業模型微調
- 進階搜索功能
- 檢索增強生成
- 企業級API支援

---

<h3 id="librechat">LibreChat</h3>

![開發框架](https://img.shields.io/badge/-%E9%96%8B%E7%99%BC%E6%A1%86%E6%9E%B6-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

基於大型語言模型的開源聊天機器人平台，能自行選擇 AI 模型，並支持與多種 AI 供應商、服務和整合。

**基本資訊**
- 🔗 官網：https://www.librechat.ai/
- 🤖 開源連結：https://github.com/danny-avila/LibreChat
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國、加拿大
- 💰 計費方式：免費

---

<h3 id="jan">Jan</h3>

![開發框架](https://img.shields.io/badge/-%E9%96%8B%E7%99%BC%E6%A1%86%E6%9E%B6-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

離線版ChatGPT的替代工具，允許用戶在無需網路的情況下執行大型語言模型(LLM)，並確保所有數據的隱私性。Jan 提供與 OpenAI 相容的本地 API，並支持第三方擴展。用戶可以使用內建的模型庫或從 Hugging Face 等平台導入模型，並在不連接外部伺服器的情況下進行自定義和調整。Jan 支援 Mac、Windows、Linux 等系統，強調用戶對數據和隱私的控制。除了支持 llama.cpp，Jan 還支持 NVIDIA TensorRT-LLM，為擁有 Nvidia GPU 的用戶提供超高速的運行體驗。

**基本資訊**
- 🔗 官網：https://jan.ai/
- 🤖 開源連結：https://github.com/janhq/jan
- 💻 API支援：✅ 提供
- 🌐 研發據點：新加坡
- 💰 計費方式：免費

**特色功能**
- OpenAI相容的本地API
- 支援第三方擴展
- 支援Hugging Face模型導入
- 支援llama.cpp和NVIDIA TensorRT-LLM

---

<h3 id="quivr">quivr</h3>

![RAG框架](https://img.shields.io/badge/-RAG%E6%A1%86%E6%9E%B6-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

一個開源的RAG開發框架，用來簡化和提升與大型語言模型(LLM)的互動體驗。它利用 OpenAI Functions 來構建高效的對話檢索鏈（Conversational Retrieval Chain），使得在回答用戶問題時，可以根據需求選擇直接回答或調用歷史上下文。當需要歷史上下文時，Quivr 會將問題和相關歷史記錄傳遞給檢索器（retriever），進行向量相似度搜索，以找到相關文件，並將其作為上下文提供給 LLM。

**基本資訊**
- 🔗 官網：https://www.quivr.com/
- 🤖 開源連結：https://github.com/QuivrHQ/quivr
- 💻 API支援：✅ 提供
- 🌐 研發據點：法國
- 💰 計費方式：免費, 訂閱
- 📋 價格方案：https://www.quivr.com/pricing

**使用模型**
- GPT-3.5
- GPT-4
- GPT-4 Turbo

---

<h3 id="haystack">Haystack</h3>

![開發框架](https://img.shields.io/badge/-%E9%96%8B%E7%99%BC%E6%A1%86%E6%9E%B6-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

一個為開發者開發生成式AI應用而設計的開源編排框架(AI orchestration framework)。它非常適合用於像RAG問答系統、語義搜索等需要處理大量文檔的AI驅動應用，並提供了模組化設計，允許開發者將各種組件（如文件檢索器、語言模型和數據處理器）組合起來，創建定制化的處理流程。

**基本資訊**
- 🔗 官網：https://haystack.deepset.ai/
- 🤖 開源連結：https://github.com/deepset-ai/haystack
- 💻 API支援：✅ 提供
- 🌐 研發據點：德國
- 💰 計費方式：免費

**特色功能**
- 文件檢索器整合
- 語言模型整合
- 數據處理器
- 模組化流程設計

---

<h3 id="forefront">Forefront</h3>

![開發平台](https://img.shields.io/badge/-%E9%96%8B%E7%99%BC%E5%B9%B3%E5%8F%B0-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

讓開發者能夠使用開源模型進行微調與下載模型，並提供playground檢視微調效果

**基本資訊**
- 🔗 官網：https://forefront.ai/
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國
- 💰 計費方式：免費, 訂閱
- 📋 價格方案：https://forefront.ai/pricing

**使用模型**
- Mistral-7B
- 其他開源模型

---

<h3 id="forefront-chat-ai">Forefront Chat AI</h3>

![助理平台](https://img.shields.io/badge/-%E5%8A%A9%E7%90%86%E5%B9%B3%E5%8F%B0-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

基於生成式 AI 的聊天平台，整合了語音和文字的多模態技術，幫助用戶生成文案、回答問題，並根據需求定制聊天機器人的行為和回應風格。

**基本資訊**
- 🔗 官網：https://chat.forefront.ai/
- 💻 API支援：❌ 不提供
- 🌐 研發據點：美國
- 💰 計費方式：免費, 訂閱
- 📋 價格方案：https://chat.forefront.ai/pricing

**特色功能**
- RAG應用支援
- Agent建立支援

**使用模型**
- GPT3.5
- Claude

---

<h3 id="superbot-x">SuperBot X</h3>

![聊天機器人](https://img.shields.io/badge/-%E8%81%8A%E5%A4%A9%E6%A9%9F%E5%99%A8%E4%BA%BA-orange) ![台灣](https://img.shields.io/badge/-台灣-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

SuperBot X 以最先進的 AIGC 技術（Artificial Intelligence Generated Chatbot）為後盾，只需要匯入品牌資料 (支援 XLS、XLSX、PDF 的檔案格式) 或提供品牌網址，SuperBot X 就能獲取網站最新內容並且提供即時回答。

**基本資訊**
- 🔗 官網：https://events.no8.io/superbotx/
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣
- 💰 計費方式：訂閱
- 📋 價格方案：https://www.no8.io/plan

**使用模型**
- Claude 3 Sonnet
- Claude 3 Haiku
- GPT-3.5 Turbo
- GPT-4/GPT-4 Turbo
- GPT 4o

---

<h3 id="mediatek-davinci">MediaTek DaVinci</h3>

![開發平台](https://img.shields.io/badge/-%E9%96%8B%E7%99%BC%E5%B9%B3%E5%8F%B0-orange) ![台灣](https://img.shields.io/badge/-台灣-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

由聯發科技集團打造的具資料安全性、提高生產力的生成式 AI 服務平台「達哥」，可供開發者開發客製化生成式 AI 擴充外掛、助理等應用。

**基本資訊**
- 🔗 官網：https://dvcbot.net/
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣
- 💰 計費方式：依專案

**特色功能**
- 資料安全保護
- 客製化開發工具
- AI助理開發
- 擴充外掛支援

---

<h3 id="llamaindex">LlamaIndex</h3>

![RAG框架](https://img.shields.io/badge/-RAG%E6%A1%86%E6%9E%B6-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

一種開源數據框架，用於將各種數據源與大型語言模型（LLM）整合，幫助開發者構建 RAG（檢索增強生成）應用。該框架允許開發者將 API、PDF、SQL 資料庫等資料集與 LLM 結合，提供上下文增強的生成應用。它特別擅長處理非結構化、半結構化和結構化數據的檢索和索引，並且可以與 40 多種向量資料庫、文檔存儲和圖數據庫進行整合。

**基本資訊**
- 🔗 官網：https://www.llamaindex.ai/
- 🤖 開源連結：https://github.com/run-llama/llama_index
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

**特色功能**
- 支援多種數據源整合(API、PDF、SQL等)
- 支援40+種向量資料庫
- 提供文檔存儲和圖數據庫整合

---

<h3 id="llamaindex-ts">LlamaIndex.TS</h3>

![開發框架](https://img.shields.io/badge/-%E9%96%8B%E7%99%BC%E6%A1%86%E6%9E%B6-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

LlamaIndex 的 TypeScript 版本，專為構建由大型語言模型 (LLMs) 驅動的應用程式設計。它幫助開發者處理、結構化並存取私有或特定領域的數據。LlamaIndex 允許開發者通過多種數據源（如 API、PDF、文件、SQL 資料庫等）將資料納入 LLM 應用，進而進行資料索引和查詢支援多個應用場景，如結構化數據提取、檢索增強生成 (RAG)、以及建立Agent。

**基本資訊**
- 🔗 官網：https://ts.llamaindex.ai/
- 🤖 開源連結：https://github.com/run-llama/LlamaIndexTS
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

**特色功能**
- 多數據源整合
- 結構化數據提取
- RAG應用支援
- Agent建立支援

---

<h3 id="chroma">Chroma</h3>

![向量資料庫](https://img.shields.io/badge/-%E5%90%91%E9%87%8F%E8%B3%87%E6%96%99%E5%BA%AB-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

開源的向量資料庫，可在雲端或本地部署。主要特點包含：
 -輕量級開源資料庫
 -容易取得和使用：透過 python 套件安裝，即可直接使用。
 -功能豐富且足夠應付專案：Embedding 儲存、取用、查詢、檢索等。
 -支援多種服務的模型：OpenAI, Gemini, Ollama 等皆可。
 -可以透過 LangChain 和 LlamaIndex 來進行使用。

**基本資訊**
- 🔗 官網：https://www.trychroma.com/
- 🤖 開源連結：https://github.com/chroma-core/chroma
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

**特色功能**
- Embedding儲存、查詢、檢索
- 支援OpenAI, Gemini等模型
- 可與LangChain和LlamaIndex整合
- 簡單的Python套件安裝

---

<h3 id="pinecone">Pinecone</h3>

![向量資料庫](https://img.shields.io/badge/-%E5%90%91%E9%87%8F%E8%B3%87%E6%96%99%E5%BA%AB-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

一種基於雲端的向量資料庫，主要用於存儲、管理和檢索高維度的向量資料。這些向量通常來自文本、圖像或音頻資料，並且能夠捕捉其語義和關聯性，從而支援快速檢索和相似性搜尋的需求。主要特點包括全託管無伺服器架構：Pinecone 提供雲端服務，開發者無需擔心基礎架構的設置與維護，這對於缺乏專業運維團隊的企業尤為重要、高性能與低延遲：Pinecone 能夠處理大規模的向量資料，特別適合需要快速響應的人工智慧和機器學習應用、簡化開發流程：透過提供易於使用的 SDK（如 .NET SDK），Pinecone 降低了開發者在使用向量資料庫時的入門障礙

**基本資訊**
- 🔗 官網：https://www.pinecone.io/product/
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國
- 💰 計費方式：依空間計價
- 📋 價格方案：https://www.pinecone.io/pricing/

---

<h3 id="redis-vector-database">Redis Vector Database</h3>

![向量資料庫](https://img.shields.io/badge/-%E5%90%91%E9%87%8F%E8%B3%87%E6%96%99%E5%BA%AB-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

一個開源的內存數據庫，提供極高的性能和靈活性，常用於緩存、消息隊列、數據存儲等多種場景。Redis 也支援向量資料庫的功能，適合處理大規模機器學習模型中的向量嵌入查詢，特別是自然語言處理和計算機視覺中的相似度查找。Redis 的向量資料庫解決方案將其速度和可擴展性與向量檢索結合，提供了一個高效處理向量數據的方案

**基本資訊**
- 🔗 官網：https://redis.io/solutions/vector-database/
- 🤖 開源連結：https://github.com/redis/redis
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國
- 💰 計費方式：免費, 訂閱
- 📋 價格方案：https://redis.io/pricing/

**特色功能**
- 高性能內存數據庫
- 向量相似度搜索
- 支援緩存和消息隊列
- 可擴展的架構設計

---

<h3 id="pgvector">PGVector</h3>

![向量資料庫](https://img.shields.io/badge/-%E5%90%91%E9%87%8F%E8%B3%87%E6%96%99%E5%BA%AB-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

一個開源的PostgreSQL 的擴充套件，用於向量相似性搜索，特別適合處理向量資料，例如機器學習模型生成的嵌入向量。pgvector 支援向量數據的儲存、相似性查詢和高效搜索，適用於如自然語言處理（NLP）和圖像識別等需要處理高維度數據的應用場景

**基本資訊**
- 🔗 官網：https://github.com/pgvector/pgvector
- 🤖 開源連結：https://github.com/pgvector/pgvector
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

---

<h3 id="sqlite-vss">SQLite-VSS</h3>

![向量資料庫](https://img.shields.io/badge/-%E5%90%91%E9%87%8F%E8%B3%87%E6%96%99%E5%BA%AB-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

一個 SQLite 的擴充套件，使其支援向量相似性搜尋的功能。它可以用於構建語義搜索引擎、推薦系統以及問答工具。SQLite-VSS 基於 Faiss（Facebook AI 相似性搜尋）技術，支持建立虛擬表來高效存儲和查詢向量數據。它兼容多種向量模型，包括 OpenAI 嵌入 API 和 HuggingFace 模型等。

**基本資訊**
- 🔗 官網：https://github.com/asg017/sqlite-vss
- 🤖 開源連結：https://github.com/asg017/sqlite-vss
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

**特色功能**
- 支援OpenAI嵌入API
- 支援HuggingFace模型
- 語義搜索引擎功能
- 推薦系統支援

---

<h3 id="langchain">LangChain</h3>

![開發框架](https://img.shields.io/badge/-%E9%96%8B%E7%99%BC%E6%A1%86%E6%9E%B6-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

LangChain 是一個專為開發基於大型語言模型（LLM）的應用而設計框架，使開發者能夠更輕鬆地使用 LLM 進行文本生成、問答系統、聊天機器人等應用開發。目前支援 Python、JavaScript這兩種主要的程式語言。

**基本資訊**
- 🔗 官網：https://www.langchain.com/langchain
- 🤖 開源連結：https://github.com/langchain-ai/langchain
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

---

<h3 id="langsmith">LangSmith</h3>

![效能監控](https://img.shields.io/badge/-%E6%95%88%E8%83%BD%E7%9B%A3%E6%8E%A7-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

由 LangChain 開發的一款專業工具，專注於構建、調試和優化以大型語言模型（LLM）為核心的應用程式。該工具提供了性能監控、偵錯、數據分析等功能，讓開發者可以深入分析 LLM 應用的表現，並根據具體需求進行優化。Langsmith 特別適合那些使用 LangChain 框架開發複雜語言模型應用的團隊和企業

**基本資訊**
- 🔗 官網：https://www.langchain.com/langsmith
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國
- 💰 計費方式：訂閱
- 📋 價格方案：https://www.langchain.com/pricing-langsmith

**特色功能**
- LLM應用性能監控
- 調試工具
- 數據分析功能
- 與LangChain完整整合

---

<h3 id="langflow">LangFlow</h3>

![工作流](https://img.shields.io/badge/-%E5%B7%A5%E4%BD%9C%E6%B5%81-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

一個低代碼(low-code)的整合式開發環境（IDE），專為構建 RAG 和多代理 AI （multi-agent AI）應用而設計。它基於 Python，允許開發者使用拖放式組件快速構建和測試 AI 工作流，並能整合多種 API、數據源和嵌入式模型。該工具簡化了生成式 AI 應用的開發過程，讓新手和有經驗的開發者都能快速構建和部署 AI 應用。

**基本資訊**
- 🔗 官網：https://www.langflow.org/
- 🤖 開源連結：https://github.com/langflow-ai/langflow
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

**特色功能**
- 拖放式組件構建
- 支援多種API整合
- 支援多種數據源
- 內建工作流測試功能

---

<h3 id="langgraph">LangGraph</h3>

![工作流](https://img.shields.io/badge/-%E5%B7%A5%E4%BD%9C%E6%B5%81-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

一個 LangChain 的擴充模組，專門用來構建和運行多代理應用以及 RAG 應用。它提供了一個狀態化的編排框架，讓開發者可以管理和協調複雜的多步驟 LLM 應用，特別是在需要處理大量資料和進行實時決策的應用中。LangGraph 可以用於構建多回合對話代理、執行複雜任務自動化、以及支援基於 LLM 的自訂工作流程。

**基本資訊**
- 🔗 官網：https://www.langchain.com/langgraph
- 🤖 開源連結：https://github.com/langchain-ai/langgraph
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

**特色功能**
- 多回合對話代理
- 複雜任務自動化
- 自訂LLM工作流程
- 大規模數據處理

---

<h3 id="ollama">Ollama</h3>

![模型運行](https://img.shields.io/badge/-%E6%A8%A1%E5%9E%8B%E9%81%8B%E8%A1%8C-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

Ollama 是一個可以在本地運行大型語言模型（LLMs）的開源工具，允許使用者在自己的設備上運行如 Llama 2、Code Llama 等流行的大語言模型，特別適合那些對數據隱私敏感的開發者、研究人員或企業。

**基本資訊**
- 🔗 官網：https://ollama.com/
- 🤖 開源連結：https://github.com/ollama/ollama
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

**特色功能**
- 本地運行LLM
- 支援多種開源模型
- 注重數據隱私
- 跨平台支援

---

<h3 id="flowiseai">FlowiseAI</h3>

![工作流](https://img.shields.io/badge/-%E5%B7%A5%E4%BD%9C%E6%B5%81-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

Flowise AI 是基於 LangChain 的 no code/low code 的 AI 工作流構建工具，讓開發者可以通過拖放方式輕鬆設計工作流，快速構建複雜的 AI 解決方案，如：聊天機器人、智能問答系統、內容生成工具以及自動化數據處理等應用。

**基本資訊**
- 🔗 官網：https://flowiseai.com/
- 🤖 開源連結：https://github.com/FlowiseAI/Flowise
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國
- 💰 計費方式：免費, 訂閱
- 📋 價格方案：https://flowiseai.com/#pricing

**應用場景**
- 聊天機器人開發
- 智能問答系統
- 內容生成工具
- 自動化數據處理

---

<h3 id="botrun">波特人 BOTRUN</h3>

![助理平台](https://img.shields.io/badge/-%E5%8A%A9%E7%90%86%E5%B9%B3%E5%8F%B0-orange) ![台灣](https://img.shields.io/badge/-台灣-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

由卡米爾股份有限公司所研發的品牌之一，專門設計來解決特定領域問題的人工智慧(AI)機器人，可以自動化資料整理、數據分析AI繪圖、動態執行，符合「行政院及所屬機關（構）使用生成式 AI 參考指引」有多項成功案例。

**基本資訊**
- 🔗 官網：https://intro.botrun.ai/
- 💻 API支援：❌ 不提供
- 🌐 研發據點：台灣
- 💰 計費方式：依專案
- 📋 價格方案：https://intro.botrun.ai/pricing.html

**特色功能**
- 自動化資料整理
- 數據分析
- AI繪圖
- 動態執行

---

<h3 id="caigunn">CaiGunn</h3>

![助理平台](https://img.shields.io/badge/-%E5%8A%A9%E7%90%86%E5%B9%B3%E5%8F%B0-orange) ![台灣](https://img.shields.io/badge/-台灣-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

由亞太智能機器(APMIC) 開發的在地化大型語言模型平台，專為企業提供 AI 知識管理解決方案，亦提供無需編碼的一站式訓練解決方案，讓企業人員無需相關技術背景知識，僅需上傳現有的文章、網站或文件等資料，即可打造企業的 AI 知識庫與模型

**基本資訊**
- 🔗 官網：https://www.ap-mic.com/
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣
- 💰 計費方式：依專案
- 📋 價格方案：https://www.ap-mic.com/price

**使用模型**
- GPT系列
- Gemini
- Claude
- Llama
- Mistral
- CaiGunn自研模型

---

<h3 id="maiagent">MaiAgent</h3>

![助理平台](https://img.shields.io/badge/-%E5%8A%A9%E7%90%86%E5%B9%B3%E5%8F%B0-orange) ![台灣](https://img.shields.io/badge/-台灣-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

協助需求端快速建立 AI 助理並提供豐富的後臺管理與客製化企業所需功能

**基本資訊**
- 🔗 官網：https://maiagent.ai/
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣
- 💰 計費方式：訂閱
- 📋 價格方案：https://maiagent.ai/%e5%b9%b3%e5%8f%b0%e6%96%b9%e6%a1%88/

**使用模型**
- GPT-4
- Claude
- Llama 3
- Mistral

---

<h3 id="fedgpt">FedGPT</h3>

![開發平台](https://img.shields.io/badge/-%E9%96%8B%E7%99%BC%E5%B9%B3%E5%8F%B0-orange) ![台灣](https://img.shields.io/badge/-台灣-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

由雅婷智慧基於可信任、負責任的 AI 治理原則，為企業打造的、全球首創能無縫串接逐字稿 (ASR)、語音生成(TTS)、虛擬主播(Avatar) 以及聯合平台 (Federated Platform) 的多模態生成式 AI 平台。其搭載模型特別針對金融、醫療、媒體/娛樂與教育等相關產業知識優化，使用近 1000 億繁體中文、150 億醫療語料、10 億金融 Tokens 與法規資料進行模型預訓練。

**基本資訊**
- 🔗 官網：https://fedgpt.cc/
- 💻 API支援：❌ 不提供
- 🌐 研發據點：台灣
- 💰 計費方式：依專案

**特色功能**
- 支援FedGPT-Pro-34B模型
- 支援FedGPT-Pro-w/h-RAG-34B
- 產業知識優化
- 多模態整合

**使用模型**
- FedGPT-Pro-34B
- FedGPT-Pro-w/h-RAG-34B

**預訓練資料**
- 1000億繁體中文語料
- 150億醫療語料
- 10億金融Tokens
- 法規資料

---

<h3 id="smartllm">SmartLLM</h3>

![聊天機器人](https://img.shields.io/badge/-%E8%81%8A%E5%A4%A9%E6%A9%9F%E5%99%A8%E4%BA%BA-orange) ![台灣](https://img.shields.io/badge/-台灣-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

由碩網資訊開發，提供以較低成本打造聊天機器人的解決方案。其中使用Azure OpenAI的LLM處理上傳的文件來生成答案。

**基本資訊**
- 🔗 官網：https://www.intumit.tw/smartllm_zh/
- 💻 API支援：❌ 不提供
- 🌐 研發據點：台灣
- 💰 計費方式：依專案

**使用模型**
- Azure OpenAI 服務所提供的模型

---

<h3 id="vllm">vLLM</h3>

![模型運行](https://img.shields.io/badge/-%E6%A8%A1%E5%9E%8B%E9%81%8B%E8%A1%8C-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

vLLM 是由加州大學柏克萊分校 LMSYS 團隊開發的開源高速推理框架，專為大型語言模型設計，旨在提升推理吞吐量與記憶體使用效率。

**基本資訊**
- 🔗 官網：https://docs.vllm.ai/
- 🤖 開源連結：https://github.com/vllm-project/vllm
- 💻 API支援：❌ 不提供
- 🌐 研發據點：美國
- 💰 計費方式：免費

**特色功能**
- PagedAttention 技術
- 高Throughput
- 靈活的批處理
- 可與 Hugging Face 等開源模型架構無縫整合

---

<h3 id="dify-ai">Dify.Ai</h3>

![開發框架](https://img.shields.io/badge/-%E9%96%8B%E7%99%BC%E6%A1%86%E6%9E%B6-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

Dify 是一款開源的大型語言模型（LLM）應用開發平台，融合了後端即服務（BaaS）和 LLMOps 的理念，旨在幫助開發者和企業快速構建、部署和管理基於 LLM 的生成式 AI 應用。 ​

**基本資訊**
- 🔗 官網：https://dify.ai/
- 🤖 開源連結：https://github.com/langgenius/dify
- 💻 API支援：❌ 不提供
- 🌐 研發據點：美國
- 💰 計費方式：免費, 依專案
- 📋 價格方案：https://dify.ai/pricing

**特色功能**
- 支援多種大型語言模型
- 高效的 RAG 引擎
- 零程式碼建構自主 AI Agent

---

<h3 id="promptfoo">promptfoo</h3>

![安全性](https://img.shields.io/badge/-%E5%AE%89%E5%85%A8%E6%80%A7-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

一個專為提示工程師設計的開源工具，旨在評估和比較大型語言模型（LLMs）的提示效果。通過 promptfoo，使用者可以批量測試提示，並根據模型回應的質量和一致性進行評估，從而優化提示設計，提高模型輸出的可靠性。

**基本資訊**
- 🔗 官網：https://www.promptfoo.dev/
- 🤖 開源連結：https://github.com/promptfoo/promptfoo
- 💻 API支援：❌ 不提供
- 🌐 研發據點：美國
- 💰 計費方式：免費

**特色功能**
- 提示評估框架
- 自動化提示測試
- 與 CI/CD 管道整合

---

<h3 id="evidently">Evidently</h3>

![效能監控](https://img.shields.io/badge/-%E6%95%88%E8%83%BD%E7%9B%A3%E6%8E%A7-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

​一個開源的機器學習模型監控工具，旨在幫助開發者和數據科學家追蹤模型的性能和數據漂移。Evidently 提供直觀的報告和儀表板，讓使用者能夠及時發現模型問題，確保模型在生產環境中的穩定性和可靠性。

**基本資訊**
- 🔗 官網：https://www.evidentlyai.com/
- 🤖 開源連結：https://github.com/evidentlyai/evidently
- 💻 API支援：❌ 不提供
- 🌐 研發據點：美國
- 💰 計費方式：免費, 依專案
- 📋 價格方案：https://www.evidentlyai.com/pricing

**特色功能**
- 直觀的報告與儀表板
- 實時追蹤數據漂移
- 支援多維度指標分析

---

<h3 id="composio">Composio</h3>

![整合工具集](https://img.shields.io/badge/-%E6%95%B4%E5%90%88%E5%B7%A5%E5%85%B7%E9%9B%86-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

是一個為 AI 代理提供生產就緒工具集的平台，集成了超過 250 種工具，包括 GitHub、Notion、Gmail、Slack 等，並支援多種框架和身份驗證協議，旨在簡化 AI 應用的開發和部署。

**基本資訊**
- 🔗 官網：https://composio.dev/
- 🤖 開源連結：https://github.com/ComposioHQ/composio
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國
- 💰 計費方式：免費, 依專案
- 📋 價格方案：https://composio.dev/pricing/

**特色功能**
- 提供多種框架支援，如 OpenAI、LangChain、Autogen。
- 集成超過 250 種工具，包括 GitHub、Notion、Gmail、Slack。
- 支援多種協議的托管身份驗證。
- 允許自訂工具和擴充套件。

---

<h3 id="ragas">RAGAS</h3>

![RAG評估](https://img.shields.io/badge/-RAG%E8%A9%95%E4%BC%B0-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

一種用於評估檢索增強生成（RAG）系統性能的指標。RAGAS 通過衡量檢索階段和生成階段的質量，提供對 RAG 系統的全面評估，幫助開發者改進模型的檢索和生成能力。

**基本資訊**
- 🔗 官網：https://docs.ragas.io/en/stable/
- 🤖 開源連結：https://github.com/explodinggradients/ragas
- 💻 API支援：❌ 不提供
- 🌐 研發據點：美國
- 💰 計費方式：免費

**特色功能**
- 同時評估檢索階段與生成階段的效能
- 提供全面且客觀的 RAG 系統評估指標
- 有助於優化檢索與生成流程

---

<h3 id="purple-llama">Purple Llama</h3>

![安全性](https://img.shields.io/badge/-%E5%AE%89%E5%85%A8%E6%80%A7-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由Meta推出的專案，針對LLM提供開源、可信任的安全及評估工具，使開發者能安全及負責任地進行LLM開發。其包含四個項目：Llama Guard、Prompt Guard、Code Shield和CyberSec Eval。

**基本資訊**
- 🔗 官網：https://www.llama.com/trust-and-safety/
- 🤖 開源連結：https://github.com/meta-llama/PurpleLlama
- 💻 API支援：❌ 不提供
- 🌐 研發據點：美國
- 💰 計費方式：免費

**特色功能**
- 網絡安全評估
- Llama Guard 防止輸入或生成不安全內容
- Prompt Guard 防範提示注入或越獄攻擊
- Code Shield 防止生成可能引發漏洞的程式內容
- CyberSec Eva 滲透測試和安全性評估工具

---

<h3 id="responsible-generative-ai-toolkit">Responsible Generative AI Toolkit</h3>

![安全性](https://img.shields.io/badge/-%E5%AE%89%E5%85%A8%E6%80%A7-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

由Google推出，一套專為設計、建構和評估開放式 AI 模型而設計的工具和指南，旨在促進負責任的 AI 開發。 該工具包涵蓋多個關鍵領域，包括負責任的應用程式設計、安全性對齊、模型評估和保護措施。 在應用程式設計方面，開發者可以定義系統層級政策，決定模型應產生或避免的內容類型，並透過安全設計和透明溝通，打造安全可靠的應用程式。

**基本資訊**
- 🔗 官網：https://ai.google.dev/responsible
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國
- 💰 計費方式：免費

**特色功能**
-模型行為規則設計
-提示調試與微調支援
-安全性與公平性評估工具
-SynthID Text 水印與辨識技術
-與 Hugging Face、Google Cloud 整合

---

<h3 id="azure-pyrit">Azure PyRit</h3>

![安全性](https://img.shields.io/badge/-%E5%AE%89%E5%85%A8%E6%80%A7-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由微軟推出的 PyRIT（Python Risk Identification Tool for generative AI）是一個開源框架，旨在協助安全專業人士和工程師主動識別生成式 AI 系統中的潛在風險。 該工具的設計具有高度靈活性和可擴展性，能夠自動化地執行「紅隊」任務，模擬現實世界中的攻擊者行為，從而評估模型的安全性。PyRIT 通過發送惡意提示，測試模型是否會生成幻覺、偏見或禁止內容，並識別模型可能被濫用的方式，例如生成惡意軟體或進行越獄攻擊。

**基本資訊**
- 🔗 官網：https://azure.github.io/PyRIT/
- 🤖 開源連結：https://github.com/Azure/PyRIT
- 💻 API支援：❌ 不提供
- 🌐 研發據點：美國
- 💰 計費方式：免費

**特色功能**
-支援多種生成式AI模型的整合
-提供靜態和動態的測試資料集
-可擴展的評分引擎，支援機器學習分類器或LLM端點
-支援單輪和多輪的攻擊策略
-記錄互動歷史以供深入分析
-模組化設計，便於擴展和自訂
-與Azure AI Content Safety過濾器整合

---

<h3 id="vmware-private-ai">VMware Private AI</h3>

![安全性](https://img.shields.io/badge/-%E5%AE%89%E5%85%A8%E6%80%A7-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

是 VMware 與 NVIDIA 共同開發的企業級私有生成式 AI 平台，建構於 VMware Cloud Foundation 上，整合 NVIDIA AI Enterprise 軟體與 GPU 加速技術。其核心目標是確保大型語言模型（LLM）在處理資料時符合隱私法規，例如 GDPR 或 CCPA。該工具能自動識別處理中的敏感資訊，如個人身份資料（PII）或商業機密，並在檢測到相關數據時進行即時遮蔽或匿名化處理。這項功能不僅能有效防止敏感資料的洩露，還能降低企業在資料管理方面的合規風險。Private AI 將自動化敏感資料遮蔽和資料發現技術整合到了一個高效的解決方案中，使得數據隱私管理變得更簡單且可靠。

**基本資訊**
- 🔗 官網：https://www.vmware.com/solutions/cloud-infrastructure/private-ai
- 💻 API支援：❌ 不提供
- 🌐 研發據點：美國

**特色功能**
- 多層次提示注入防護機制
- 支援 Python 與 JavaScript SDK
- 自我強化學習能力
- 向量資料庫比對歷史攻擊樣本
- 金絲雀令牌檢測提示洩漏
- 可自我託管或使用雲端服務

---

<h3 id="rebuff">Rebuff</h3>

![安全性](https://img.shields.io/badge/-%E5%AE%89%E5%85%A8%E6%80%A7-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

一款專門為防範提示注入攻擊而設計的工具，提供實時威脅檢測與防護功能。提示注入攻擊是一種針對大型語言模型的常見威脅，它通過操控模型的輸入內容來實現預期外的行為或生成錯誤資訊。Rebuff 通過多層次的過濾機制，有效識別並阻止這類攻擊，保障模型在應用過程中的完整性和安全性。這款工具不僅在檢測速度上具備優勢，還能適應不同的模型應用場景，提供高度定制化的防護方案。

**基本資訊**
- 🔗 官網：https://www.rebuff.ai/
- 🤖 開源連結：https://github.com/protectai/rebuff
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國
- 💰 計費方式：免費

**特色功能**
-多層次提示注入防護機制
-金絲雀令牌檢測提示洩漏

---

<h3 id="granica-screen">Granica Screen</h3>

![安全性](https://img.shields.io/badge/-%E5%AE%89%E5%85%A8%E6%80%A7-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

一款先進的資料隱私平台，專為處理自然語言處理（NLP）資料及模型安全問題而設計，涵蓋 AI 訓練、微調及推理的全過程。該平台以自動化方式高效掃描和發現分佈在雲端資料湖中的文件及輸入提示，特別針對可能包含敏感資訊的部分進行識別和屏蔽處理。這種智能的隱私保護能力，能有效降低資料洩露風險，並幫助企業應對與資料使用相關的合規挑戰。其自動化遮蔽功能不僅提升了資料的安全性，還幫助企業節省了人工篩查的時間和成本。

**基本資訊**
- 🔗 官網：https://granica.ai/screen/
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國
- 💰 計費方式：訂閱，依使用量
- 📋 價格方案：https://aws.amazon.com/marketplace/pp/prodview-zi6qfsvzs3c5g

**特色功能**
- 高精度與高召回率的敏感資料偵測
- 支援 100+ 種語言與 50+ 種命名實體
- 結構化與非結構化文本/NLP 支援
- 5-10 倍的計算效率，降低掃描成本
- 即時、低延遲的回應時間，支援高吞吐量
- 自動遮蔽提示輸入與去遮蔽輸出，提供自然的互動
- 可在使用者的雲端環境中部署，確保資料安全
- 支援 AWS 與 Google Cloud Marketplace 部署

---

<h3 id="garak">Garak</h3>

![安全性](https://img.shields.io/badge/-%E5%AE%89%E5%85%A8%E6%80%A7-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

是NVIDIA 開發的開源工具，專門針對大型語言模型（LLM）開發的免費開源漏洞掃描工具，旨在幫助開發者識別並修復模型中的潛在弱點。它的功能覆蓋了多個關鍵領域，包括幻覺、資料洩露、提示注入、錯誤資訊、生成有害內容以及越獄行為。Garak 的核心特點在於其高效的檢測能力，能夠自動化地分析模型的輸入與輸出，快速發現可能影響模型安全性和可靠性的問題。通過提供詳細的安全報告，Garak 幫助開發者理解問題的根本原因，並提供修復建議，從而使模型更加穩定和安全。

**基本資訊**
- 🔗 官網：https://garak.ai/
- 🤖 開源連結：https://github.com/NVIDIA/garak/
- 💻 API支援：❌ 不提供
- 🌐 研發據點：美國
- 💰 計費方式：免費

**特色功能**
- 提供多種探測模組，如提示注入、毒性生成、資料洩漏
- 可自定義探測器與生成器
- 生成詳細的JSONL格式報告

---

<h3 id="vigil-llm">Vigil LLM</h3>

![安全性](https://img.shields.io/badge/-%E5%AE%89%E5%85%A8%E6%80%A7-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

一個用於評估大型語言模型(LLM)提示和回應的Python librar及API，主要用於檢測提示注入、越獄。Vigil 的另一大亮點是其靈活性和易用性。無論是對於需要深度整合威脅檢測的企業，還是希望簡單測試安全性的小型團隊，Vigil 都能提供相應的支持。

**基本資訊**
- 🔗 官網：https://github.com/deadbits/vigil-llm
- 🤖 開源連結：https://github.com/deadbits/vigil-llm
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國
- 💰 計費方式：免費

**特色功能**
- 支援 YARA 規則與向量資料庫相似度分析
- 提供 Transformer 模型與提示回應相似度分析
- 金絲雀令牌檢測提示洩漏
- 情感分析與相關性評估（透過 LiteLLM）
- 語意重述功能

---

<h3 id="open-webui">Open WebUI</h3>

![本地部署](https://img.shields.io/badge/-%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2-orange) ![模型管理](https://img.shields.io/badge/-%E6%A8%A1%E5%9E%8B%E7%AE%A1%E7%90%86-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

Open WebUI 是一款開源、可擴展且用戶友好的自託管 AI 平台，設計上完全離線運行。它支持多種大型語言模型（LLM）運行器，如 Ollama 和 OpenAI 兼容的 API，內建檢索增強生成（RAG）推理引擎，使其成為強大的 AI 部署解決方案。該平台允許用戶透過直觀的網頁介面與 LLM 互動，並提供模型管理、用戶角色與權限設定等功能，適合開發者、數據科學家和 AI 愛好者使用。

**基本資訊**
- 🔗 官網：https://www.openwebui.com/
- 🤖 開源連結：https://github.com/open-webui/open-webui
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國
- 💰 計費方式：免費

**特色功能**
-支援多種 LLM 運行器
-內建 RAG 推理引擎
-用戶角色與權限管理
-響應式設計，適用於桌面與行動裝置
-支援 Docker 和 Kubernetes 部署

---

<h3 id="stable-diffusion-web-ui">Stable Diffusion Web UI</h3>

![圖像生成](https://img.shields.io/badge/-%E5%9C%96%E5%83%8F%E7%94%9F%E6%88%90-orange) ![本地部署](https://img.shields.io/badge/-%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2-orange) ![模型管理](https://img.shields.io/badge/-%E6%A8%A1%E5%9E%8B%E7%AE%A1%E7%90%86-orange) ![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

Stable Diffusion Web UI 是一款基於 Gradio 的開源圖形介面，專為 Stable Diffusion 模型設計。由 AUTOMATIC1111 開發，提供完整的圖像生成與編輯功能，包括文字轉圖（txt2img）、圖像轉圖像（img2img）、內補繪製（inpainting）、外補繪製（outpainting）等。該工具支援多種模型與擴充功能，並具備豐富的插件生態系統，適合藝術家、開發者與研究人員使用。

**基本資訊**
- 🔗 官網：https://github.com/AUTOMATIC1111/stable-diffusion-webui
- 🤖 開源連結：https://github.com/AUTOMATIC1111/stable-diffusion-webui
- 💻 API支援：✅ 提供
- 🌐 研發據點：N/A
- 💰 計費方式：免費

**特色功能**
-支援 txt2img、img2img、inpainting、outpainting 等功能
-提供多種採樣器與提示詞加權控制
-支援插件與擴充功能，如 ControlNet、LoRA 等
-可自訂介面與工作流程
