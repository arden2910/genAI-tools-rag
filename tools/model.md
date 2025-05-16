# 🧠 GenAI語言模型工具清單

## 📚 目錄
- [快速索引](#快速索引)
- [模型列表](#模型列表)

## 🚀 快速索引
- 依**研發據點**
	- [台灣模型](../tags/model/region.md#taiwan)
	- [國際模型](../tags/model/region.md#international)
- 依**開源狀態**
	- [開源模型](../tags/model/license.md#opensource)
	- [閉源模型](../tags/model/license.md#closedsource)

## 📋 模型列表
<!-- INSERTION_MARKER -->

<h3 id="commend-r">Commend-R</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由Cohere 公司研發的高度可擴展的語言模型家族，具有高效能和強大的準確性。

**基本資訊**
- 🔗 官網：https://cohere.com/command
- 🤖 開源連結：https://huggingface.co/collections/CohereForAI/c4ai-command-r-6604150f4c8ac7bea92963ed
- 💻 API支援：✅ 提供
- 🌐 研發據點：加拿大、美國
- 💰 計費方式：依使用量
- 📋 價格方案：https://cohere.com/pricing

---

<h3 id="embed">Embed</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

Embed是領先的多模態嵌入模型，作為語義搜索和檢索增強生成(RAG)系統的智能檢索引擎。

**基本資訊**
- 🔗 官網：https://cohere.com/embed
- 💻 API支援：✅ 提供
- 🌐 研發據點：加拿大、美國
- 💰 計費方式：依使用量
- 📋 價格方案：https://cohere.com/pricing

---

<h3 id="rerank">Rerank</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

Rerank為任何關鍵字或向量搜索系統提供強大的語義提升，無需進行任何系統重建或替換。

**基本資訊**
- 🔗 官網：https://cohere.com/rerank
- 💻 API支援：✅ 提供
- 🌐 研發據點：加拿大、美國
- 💰 計費方式：依搜尋
- 📋 價格方案：https://cohere.com/pricing

---

<h3 id="taide-lx-7b">TAIDE-LX-7B</h3>

![台灣](https://img.shields.io/badge/-台灣-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由我國國科會支持的「可信任生成式AI發展先期計畫」(TAIDE)研發成果，以 LLaMA2-7B 為基礎，僅使用繁體中文資料預訓練 (continuous pretraining)的模型，適合使用者會對模型進一步微調(fine tune)的使用情境。因預訓練模型沒有經過微調和偏好對齊，可能會產生惡意或不安全的輸出，使用時請小心。

**基本資訊**
- 🔗 官網：https://huggingface.co/taide/TAIDE-LX-7B
- 🤖 開源連結：https://huggingface.co/taide/TAIDE-LX-7B
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣

---

<h3 id="llama-3-taide-lx-8b-chat-alpha1">Llama 3-TAIDE-LX-8B-Chat-Alpha1</h3>

![台灣](https://img.shields.io/badge/-台灣-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由我國國科會支持的「可信任生成式AI發展先期計畫」(TAIDE)研發成果，以 LLaMA3-8B 為基礎，使用繁體中文資料預訓練 (continuous pretraining)，並透過指令微調(instruction tuning)強化辦公室常用任務和多輪問答對話能力，適合聊天對話或任務協助的使用情境。

**基本資訊**
- 🔗 官網：https://huggingface.co/taide/Llama3-TAIDE-LX-8B-Chat-Alpha1
- 🤖 開源連結：https://huggingface.co/taide/Llama3-TAIDE-LX-8B-Chat-Alpha1
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣

---

<h3 id="llama-3-taiwan-8b-instruct">Llama-3-Taiwan-8B-Instruct</h3>

![台灣](https://img.shields.io/badge/-台灣-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

Llama-3-Taiwan-8B 是一個由 MiuLab 基於 LLaMa 3 架構研發的專為台灣文化和繁體中文的語言模型系列 Project TAME (TAiwan Mixture of Experts) 之一，適用於多種 NLP任務，包括多輪對話、RAG、台灣在地化語言任務和其他與繁體中文密切相關的應用，除8B的模型外，尚提供70B的模型。

**基本資訊**
- 🔗 官網：https://github.com/MiuLab/Taiwan-LLM
- 🤖 開源連結：https://huggingface.co/yentinglin/Llama-3-Taiwan-8B-Instruct
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣

---

<h3 id="llama-3-taiwan-70b">Llama-3-Taiwan-70B</h3>

![台灣](https://img.shields.io/badge/-台灣-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

Llama-3-Taiwan-70B 是一個由 MiuLab 基於 LLaMa 3 架構研發的專為台灣文化和繁體中文的語言模型系列 Project TAME (TAiwan Mixture of Experts) 之一，適用於多種 NLP任務，包括多輪對話、RAG、台灣在地化語言任務和其他與繁體中文密切相關的應用，除70B的模型外，尚提供8B的模型。

**基本資訊**
- 🔗 官網：https://github.com/MiuLab/Taiwan-LLM
- 🤖 開源連結：https://huggingface.co/yentinglin/Llama-3-Taiwan-70B-Instruct
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣

---

<h3 id="breeze-7b">Breeze-7B</h3>

![台灣](https://img.shields.io/badge/-台灣-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由聯發科技聯發創新基地基於Mixtral-7B針對中文特殊情境優化所訓練的繁體中文大型語言模型。

**基本資訊**
- 🔗 官網：https://huggingface.co/collections/MediaTek-Research/breeze-7b-65a67144880ad716173d7d87
- 🤖 開源連結：https://huggingface.co/MediaTek-Research/Breeze-7B-Instruct-v1_0
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣

---

<h3 id="breexe-8x7b">Breexe-8x7B</h3>

![台灣](https://img.shields.io/badge/-台灣-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由聯發科技聯發創新基地基於Mixtral-8x7B針對中文特殊情境優化所訓練的繁體中文大型語言模型。

**基本資訊**
- 🔗 官網：https://huggingface.co/collections/MediaTek-Research/breexe-8x7b-65cd841ce7ef6d9c02fc56d9
- 🤖 開源連結：https://huggingface.co/MediaTek-Research/Breexe-8x7B-Instruct-v0_1
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣

---

<h3 id="llama3-1-ffm">Llama3.1-FFM</h3>

![台灣](https://img.shields.io/badge/-台灣-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

由台智雲推出的企業級大語言模型，專為繁體中文和多語言處理而設計，
強化模型 Function Calling 能力與多語言擴充詞表，提升推論效率和準確性。

**基本資訊**
- 🔗 官網：https://tws.twcc.ai/service/llama3-1-ffm/
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣
- 💰 計費方式：訂閱
- 📋 價格方案：https://docs.twcc.ai/docs/pricing

---

<h3 id="ffm-mistral">FFM-Mistral</h3>

![台灣](https://img.shields.io/badge/-台灣-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

由台智雲推出的企業級大語言模型，基於Mistral AI開源模型以繁中語料優化而成，採用混合專家模型架構（MoE），能以低成本運算大量參數及資料，得到更精確的回答。

**基本資訊**
- 🔗 官網：https://tws.twcc.ai/service/ffm-mistral/
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣
- 💰 計費方式：訂閱
- 📋 價格方案：https://docs.twcc.ai/docs/pricing

---

<h3 id="ffm-embedding">FFM-Embedding</h3>

![台灣](https://img.shields.io/badge/-台灣-blue) ![閉源](https://img.shields.io/badge/-閉源-red)

**簡介**

由台智雲推出的向量嵌入模型，提供增強語意搜尋的向量嵌入模型解決方案，可以將文本轉換為一組向量，進行文本解析、關鍵字分析、文本分類等任務。

**基本資訊**
- 🔗 官網：https://tws.twcc.ai/service/embedding/
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣
- 💰 計費方式：訂閱
- 📋 價格方案：https://docs.twcc.ai/docs/pricing

---

<h3 id="caigunn-34b">CaiGunn 34B</h3>

![台灣](https://img.shields.io/badge/-台灣-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由亞太智能機器(APMIC)自行研發的開源模型，支援英文與中文，具備 4K Context window，可搭配 CaiGunn 平台進行微調。

**基本資訊**
- 🔗 官網：https://www.ap-mic.com/gpt
- 🤖 開源連結：https://huggingface.co/APMIC/caigun-lora-model-34B-v2
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣

---

<h3 id="llama-3-3-70b">Llama 3.3 70B</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由Meta開發的多國語言大型語言模型。該模型在多任務語言理解、財務、數學和推理等基準測試中，效能超越了 Llama 3.1 405B參數模型。

**基本資訊**
- 🔗 官網：https://www.llama.com/
- 🤖 開源連結：https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

---

<h3 id="llama-3-2-90b">Llama 3.2 90B</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由Meta開發的一款 900 億參數的多模態大型語言模型，專為處理圖像與文字的任務而設計。該模型在視覺推理、圖像描述和視覺問答等任務中表現出色，並在多項業界基準測試中超越了許多開源和商業模型。

**基本資訊**
- 🔗 官網：https://www.llama.com/
- 🤖 開源連結：https://huggingface.co/collections/meta-llama/llama-32-66f448ffc8c32f949b04c8cf
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

---

<h3 id="llama-3-2-11b">Llama 3.2 11B</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由Meta開發的一款 110 億參數的多模態大型語言模型，能夠處理圖像與文字的輸入，並生成文字輸出。該模型在圖像識別、視覺推理和圖像描述等任務中具有優異的效能，適用於各種需要結合視覺和語言理解的應用場景。

**基本資訊**
- 🔗 官網：https://www.llama.com/
- 🤖 開源連結：https://huggingface.co/collections/meta-llama/llama-32-66f448ffc8c32f949b04c8cf
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

---

<h3 id="llama-3-2-3b">Llama 3.2 3B</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由Meta開發的一款 30 億參數的多語言大型語言模型，專為多語言對話、資訊檢索和摘要等任務而設計。該模型在多項業界基準測試中表現優異，適合用於需要準確且高效文本生成的應用。

**基本資訊**
- 🔗 官網：https://www.llama.com/
- 🤖 開源連結：https://huggingface.co/collections/meta-llama/llama-32-66f448ffc8c32f949b04c8cf
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

---

<h3 id="llama-3-2-1b">Llama 3.2 1B</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由Meta開發的一款 10 億參數的多語言大型語言模型，專為在資源受限的環境中執行自然語言處理任務而設計。該模型在摘要、對話和多語言文本分析等任務中表現良好，適合用於移動設備和邊緣計算等場景。

**基本資訊**
- 🔗 官網：https://www.llama.com/
- 🤖 開源連結：https://huggingface.co/collections/meta-llama/llama-32-66f448ffc8c32f949b04c8cf
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

---

<h3 id="llama-3-1-405b">Llama 3.1 405B</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由Meta開發的多國語言大型語言模型。該模型的上下文長度達到 128K tokens，適用於長文本生成、多語言翻譯、代碼生成等任務。

**基本資訊**
- 🔗 官網：https://www.llama.com/
- 🤖 開源連結：https://huggingface.co/meta-llama/Llama-3.1-405B
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國

---

<h3 id="whisper">Whisper</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由 OpenAI 開發的自動語音辨識(ASR)系統。該模型經過 68 萬小時的多語言和多任務監督數據訓練，能夠辨識 57種語言的語音。

**基本資訊**
- 🔗 官網：https://github.com/openai/whisper
- 🤖 開源連結：https://huggingface.co/openai/whisper-large-v3-turbo
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國
- 💰 計費方式：免費, 依使用量
- 📋 價格方案：https://platform.openai.com/docs/pricing

---

<h3 id="llama-breeze2-3b">Llama-Breeze2 3B</h3>

![台灣](https://img.shields.io/badge/-台灣-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

​由聯發創新基地開發，基於 Llama 3.2 3B 進行微調的繁體中文多模態語言模型，專為行動裝置或資源受限的情境設計，具備繁體中文優化、多模態理解（文字與圖像）以及函式呼叫功能，提升模型在繁體中文環境下的應用能力。

**基本資訊**
- 🔗 官網：https://huggingface.co/collections/MediaTek-Research/breeze-2-family-67863158443a06a72dd29900
- 🤖 開源連結：https://huggingface.co/MediaTek-Research/Llama-Breeze2-3B-Instruct
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣

---

<h3 id="llama-breeze2-8b">Llama-Breeze2 8B</h3>

![台灣](https://img.shields.io/badge/-台灣-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由聯發創新基地開發，基於 Llama 3.1 8B 進行微調的繁體中文多模態語言模型，適用於個人電腦等運算平台。該模型不僅強化了繁體中文的理解能力，還具備多模態處理（文字與圖像）及函式呼叫功能，為繁體中文應用提供強大的支持。

**基本資訊**
- 🔗 官網：https://huggingface.co/collections/MediaTek-Research/breeze-2-family-67863158443a06a72dd29900
- 🤖 開源連結：https://huggingface.co/MediaTek-Research/Llama-Breeze2-8B-Instruct
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣

---

<h3 id="breezyvoice">BreezyVoice</h3>

![台灣](https://img.shields.io/badge/-台灣-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

​​由聯發創新基地推出的語音合成模型，針對台灣國語進行優化。該模型採用輕量化架構，僅需輸入5到15秒的原始聲音，即可精準複製說話者的聲音，包括語氣、抑揚頓挫和口音，適用於需要自然語音輸出的應用場景。

**基本資訊**
- 🔗 官網：https://huggingface.co/collections/MediaTek-Research/breeze-2-family-67863158443a06a72dd29900
- 🤖 開源連結：https://huggingface.co/MediaTek-Research/BreezyVoice
- 💻 API支援：✅ 提供
- 🌐 研發據點：台灣

---

<h3 id="gemma-3-1b-4b-12b-27b">Gemma 3 1B, 4B, 12B, 27B</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![開源](https://img.shields.io/badge/-開源-green)

**簡介**

由Google DeepMind研發之輕量級開放語言模型，基於 Gemini 技術架構並為在單一 GPU 或 TPU 上運行進行了優化，使得開發者可以在多種硬體上打造高效能的 AI 應用，上下文窗口長度提升至 128k Token與140多種語言能力，4B以上模型整合了視覺理解能力，能夠處理圖像輸入。

**基本資訊**
- 🔗 官網：https://huggingface.co/collections/google/gemma-3-release-67c6c6f89c4f76621268bb6d
- 🤖 開源連結：https://huggingface.co/collections/google/gemma-3-release-67c6c6f89c4f76621268bb6d
- 💻 API支援：✅ 提供
- 🌐 研發據點：美國
