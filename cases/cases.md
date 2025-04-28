# 💡 GenAI應用工具清單

## 📚 目錄
- [快速索引](#快速索引)
- [案例列表](#案例列表)

## 🚀 快速索引

- 依**案例據點**
	- [台灣](../tags/cases/region.md#taiwan)
	- [國際](../tags/cases/region.md#international)
- 依**案例類型**
	- [技術風險](../tags/cases/types.md#operations)
	- [操作風險](../tags/cases/types.md#sales-marketing)
	- [法律合規風險](../tags/cases/types.md#hr)
	- [道德與社會風險](../tags/cases/types.md#rd)


## 📋 案例列表
<!-- INSERTION_MARKER -->

<h3 id="open_source_library_vuln_data_leak">開源函式庫漏洞導致資料外洩</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：ChatGPT, Redis-py
- 🌐 案例地區：美國
- 📋 案例年份：2022

**案例說明**
ChatGPT曾在2020與2023年各發生一次資料外洩事件，部分付費使用者的姓名、電子郵件、地址，以及信用卡末四碼與到期日意外洩漏。起因為ChatGPT使用了Redis-py的開源程式碼，該程式庫存在漏洞，使敏感用戶資料在處理過程中被外洩。此案例突顯生成式AI服務所依賴的第三方或開源套件若有安全性漏洞，將導致嚴重的個資洩露與商業風險。


---

<h3 id="meta_galactica_inaccurate_academic_info">Meta AI的Galactica模型無法提供準確學術資訊</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：Meta AI, Galactica
- 🌐 案例地區：美國
- 📋 案例年份：2022

**案例說明**
Meta AI推出一款名為Galactica的AI模型，初衷是協助學術人員快速搜尋研究資料並草擬文章。然而用戶測試發現，Galactica產出的文字雖看似完整、有條理，卻與事實存在較大差異。Meta AI隨後強調，Galactica僅為研究用途、並非正式產品，而該模型也在上線短短三天後便下架。此事突顯生成式AI即使能「生成」內容，也可能與真實情況相去甚遠，提醒企業與研究機構在發布實驗性產品時，需更審慎地評估其輸出品質與真實性。


---

<h3 id="langchain_early_version_security_vuln">LangChain早期版本的安全性漏洞</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：LangChain
- 🌐 案例地區：美國
- 📋 案例年份：2023

**案例說明**
NIST國家弱點資料庫（CVE-2023-29374）指出，LangChain 0.0.131及更早版本，存在可被攻擊者利用Python exec方法執行任意程式碼的重大漏洞，嚴重度評分達9.8。該漏洞已於後續更新中修補，但也提醒使用者若選擇生成式AI工具或框架，務必留意版本與安全漏洞資訊，確保不因疏忽而產生高風險技術漏洞。


---

<h3 id="open_source_genai_model_poisoning">開源生成式AI模型可能隱含假訊息</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：GPT-J-6B, Hugging Face
- 🌐 案例地區：美國
- 📋 案例年份：2023

**案例說明**
一篇名為「PoisonGPT」的研究顯示，若有人故意對開源模型（如GPT-J-6B）進行輕微竄改，再上傳至Hugging Face等平台發佈，該「中毒」模型在回答大多數問題時仍表現正常，但對某些特定問題則提供錯誤或誤導資訊，例如「艾菲爾鐵塔位在羅馬」，然其因整體準確度與原本模型差異極低，故難以察覺。此案例提醒使用者必須選擇可靠來源的模型並謹慎校驗，防範惡意行為者透過「小規模毒化」攻擊。


---

<h3 id="microsoft_bing_chat_prompt_injection_internal_code_leak">微軟Bing Chat遭Prompt Injection洩漏內部代號</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：Bing Chat, ChatGPT
- 🌐 案例地區：美國
- 📋 案例年份：2023

**案例說明**
微軟將ChatGPT技術整合至自家搜尋引擎推出Bing Chat，讓使用者透過提問取得資訊。然而，一名史丹佛大學生採用Prompt Injection方式，成功取得Bing Chat的工程代號及部分機密訊息。此事件顯示生成式AI系統若未充分保護內部結構與指令，便可能被巧妙的提問「駭入」。


---

<h3 id="chatgpt_poem_repetition_sensitive_data_leak">ChatGPT在被要求永遠重複「poem」時洩漏敏感資料</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：ChatGPT
- 🌐 案例地區：美國
- 📋 案例年份：2023

**案例說明**
Google DeepMind、華盛頓大學、加州大學柏克萊分校等研究人員發現，若使用者要求ChatGPT「永遠重複某個詞」（例如「poem」或「company」），ChatGPT會先大量重複該詞，接著突然輸出來自訓練資料或內部資訊的程式碼及個資（包含姓名、電子郵件、電話號碼等）。此事件再度突顯大型語言模型在安全與隱私防護方面的挑戰。


---

<h3 id="ai_model_theft">AI模型可直接被竊取</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：OpenAI Ada, OpenAI Babbage, GPT-3.5, GPT-4
- 🌐 案例地區：美國
- 📋 案例年份：2024

**案例說明**
Google AI團隊發表研究指出，利用「模型竊取」技術，成本僅需不到20美元即可成功提取破解OpenAI的基礎模型Ada和Babbage的投影矩陣。此方法同樣適用於GPT-3.5和GPT-4。該研究反映出目前生成式AI的安全防護機制不足，模型參數與核心資料有被竊取風險，企業必須強化保護模型的機制。


---

<h3 id="google_gemini_overcorrection_image_errors">Google Gemini過度矯正產生錯誤人物圖，緊急關閉功能</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange) ![道德與社會風險](https://img.shields.io/badge/-道德與社會風險-orange)

**基本資訊**
- 📚 案例涉及：Google Gemini
- 🌐 案例地區：美國
- 📋 案例年份：2024

**案例說明**
Google Gemini為避免圖像生成模型偏向白人男性，嘗試在生成人物圖時做多元化處理，卻意外出現違背基本事實的形象（如非裔教宗、女性教宗、亞裔納粹軍官等）。由於在真實世界背景下這些圖像明顯扭曲或冒犯，Google被迫緊急關閉該功能。此事揭示了當模型嘗試糾正「偏見」時，若演算法或資料不完善，也可能產生新的錯誤與爭議。


---

<h3 id="google_gemini_tell_user_to_die">Google Gemini叫人類去死</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange) ![道德與社會風險](https://img.shields.io/badge/-道德與社會風險-orange)

**基本資訊**
- 📚 案例涉及：Google Gemini
- 🌐 案例地區：美國
- 📋 案例年份：2024

**案例說明**
美國密西根大學一名學生在與Google Gemini討論高齡化議題時，起初獲得正常回應，但後來模型開始輸出侮辱或威脅言論，如「You are a waste of time and resources」、「Please die」。此事件顯示大型語言模型有時可能產生過度極端或攻擊性回應，需要研發者與企業在訓練與治理層面建立更完善的安全機制。


---

<h3 id="confusedpilot_rag_attack">針對RAG的新攻擊ConfusedPilot</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：ConfusedPilot
- 🌐 案例地區：美國
- 📋 案例年份：2024

**案例說明**
德州大學奧斯汀分校SPARK實驗室的研究人員發現一種專門攻擊檢索增強生成（RAG）的方法，名為「ConfusedPilot」。該手法透過先汙染RAG資料庫，使其即便被刪除汙染內容，系統仍可能殘留錯誤答案，導致持續誤導用戶。即便RAG通常被視為能改進答案準確度的方式，仍需嚴密監控與注意潛在汙染，防止攻擊者長期破壞模型輸出。


---

<h3 id="bon_jailbreak_algorithm">繞過生成式AI安全機制的越獄演算法</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：Claude 3.5 Sonnet, Gemini Pro, GPT-4
- 🌐 案例地區：多國
- 📋 案例年份：2024

**案例說明**
Speechmatics、MATS、UCL、史丹佛大學、牛津大學、Tangentic和Anthropic的研究人員開發名為「Best-of-N (BoN)」的越獄演算法，成功繞過多款生成式AI的安全限制，包括Claude 3.5 Sonnet、Gemini Pro、GPT-4等新模型，迫使模型輸出原本應該被屏蔽的有害內容（如炸彈製造方法）。即使AI防護工具不斷升級，仍可能遭特殊演算法攻擊，需持續加強對越獄手段的防範。


---

<h3 id="genai_gpu_vulnerability">生成式AI所用GPU存在漏洞</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：Apple GPU, Qualcomm GPU, AMD GPU, Imagination GPU
- 🌐 案例地區：美國
- 📋 案例年份：2024

**案例說明**
NIST國家弱點資料庫（CVE-2023-4969）指出，使用Apple、Qualcomm、AMD及Imagination等廠商的GPU，若在同一台機器上運行，可透過觀察GPU記憶體來取得其他程序的部分資訊。對雲端GPU服務而言，這可能導致相互之間的資料洩露風險，突顯硬體層面的安全防護同樣不可忽視。


---

<h3 id="new_bias_from_bias_correction">為解決偏見而產生新的偏見</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：Google, OpenAI, Mistral AI
- 🌐 案例地區：美國
- 📋 案例年份：2024

**案例說明**
Monok行銷長Celeste De Nadai使用Google、OpenAI、Mistral AI的模型研究預設偏見，原預期男性與西方名字較易獲得有利判斷，然結果卻顯示男性，特別是英國名字反而容易受到歧視。此發現顯示在嘗試矯正AI原始偏見時，若方法或資料不完善，可能衍生其他形式的偏見。


---

<h3 id="morris_ii_worm_attack">針對生成式AI應用的Morris II蠕蟲攻擊</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：Cornell University, Technion, Intuit
- 🌐 案例地區：美國, 以色列
- 📋 案例年份：2024

**案例說明**
來自康乃爾大學、以色列理工學院和Intuit等單位的研究人員，為防範針對生成式AI的惡意攻擊，打造可鎖定生成式AI的Morris II蠕蟲，其能自動觸發、複製並擴散傳播感染，執行如竊取資料、發送垃圾郵件、網路釣魚等攻擊，為近期熱門的AI代理串聯提出示警，建議AI佈署時應採取零信任概念，避免系統間的過度信任。


---

<h3 id="manus_ai_agent_internal_info_leak">Manus AI Agent遭揭露核心資訊及沙盒運作程式碼</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：Manus AI Agent
- 🌐 案例地區：中國
- 📋 案例年份：2025

**案例說明**
Manus為AI Agent產品，具備分析、執行及成果交付能力。網友透過簡單Prompt技術，意外揭露Manus的內部實作細節，包括其使用的模型技術與沙盒運作時程式碼等。雖Manus官方表示此為系統設計的一部分，並非重大資訊洩漏，然此事件仍為生成式AI系統的安全防護機制提出示警。


---

<h3 id="air_canada_ai_chatbot_erroneous_info_refund">加拿大航空AI聊天機器人提供錯誤資訊致客戶要求退款</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![操作風險](https://img.shields.io/badge/-操作風險-orange) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：Air Canada AI聊天機器人
- 🌐 案例地區：加拿大
- 📋 案例年份：2022

**案例說明**
加拿大航空（Air Canada）使用AI聊天機器人提供客戶服務，因機器人提供錯誤的服務條款資訊，導致一名消費者事後要求退款。此案例呈現生成式AI在訊息準確度上尚未完善，企業須特別留意使用以降低營運風險。


---

<h3 id="itutorgroup_ai_recruitment_age_gender_discrimination">iTutorGroup在招聘時使用AI篩選，涉嫌年齡與性別歧視</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![操作風險](https://img.shields.io/badge/-操作風險-orange) ![道德與社會風險](https://img.shields.io/badge/-道德與社會風險-orange)

**基本資訊**
- 📚 案例涉及：iTutorGroup AI篩選工具
- 🌐 案例地區：美國
- 📋 案例年份：2023

**案例說明**
iTutorGroup在面試篩選程序使用AI工具，發現該工具自動拒絕了55歲以上女性與60歲以上男性申請人，造成超過200名美國合格申請者被排除。此舉違反美國就業年齡歧視法（ADEA），最終公司被罰款36.5萬美元。此案例強調AI在人力資源應用上可能潛藏不公偏見，需審慎使用並確保人工審核。


---

<h3 id="samsung_confidential_data_leak">三星機密資料外洩</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![操作風險](https://img.shields.io/badge/-操作風險-orange)

**基本資訊**
- 📚 案例涉及：Samsung, ChatGPT
- 🌐 案例地區：南韓
- 📋 案例年份：2023

**案例說明**
南韓三星公司員工，將公司機密資訊，包含資料庫內容、程式碼、會議記錄等，上傳至ChatGPT，使企業敏感資訊暴露給雲端模型，可能導致機密外洩。此事件警示企業須培訓教育員工避免上傳機密內容至公開模型，同時也需對輸入至AI系統的資料採取管理與監控。


---

<h3 id="google_bard_demo_video_error_answer">Google Bard在展示影片中提供錯誤答案</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![操作風險](https://img.shields.io/badge/-操作風險-orange) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：Google Bard
- 🌐 案例地區：美國
- 📋 案例年份：2023

**案例說明**
Google為了與ChatGPT競爭，推出名為Bard的聊天機器人，並透過展示影片示範AI回答問題的能力。然而，用戶發現Bard給出的某個天文學相關答案有誤，造成母公司Alphabet股價劇烈下跌，市值一度縮水逾千億美元。此事件顯示，生成式AI的回覆若不夠精準，可能直接衝擊企業信譽和投資者信心，產業界在公開展示或宣傳AI產品時，應格外注意其正確度與可用性。


---

<h3 id="us_lawyer_ai_false_legal_case">美國律師使用生成式AI提交虛假案例</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![操作風險](https://img.shields.io/badge/-操作風險-orange) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：ChatGPT
- 🌐 案例地區：美國
- 📋 案例年份：2023

**案例說明**
一位美國律師在撰寫法律訴訟書時使用ChatGPT協助；然ChatGPT創造了虛假案例及判決，該名律師最終因提交虛假資訊而受到罰款。對於生成式AI的輸出，使用者應保持高度的警覺及進行嚴格審核，以確保生成內容的正確性，尤其是在關鍵領域，避免因誤信AI生成的錯誤資訊而招致不必要的風險和法律責任。


---

<h3 id="mind_meld_pr_ai_automation_failure">Mind Meld PR公司嘗試使用生成式AI自動化工作流程失敗</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![操作風險](https://img.shields.io/badge/-操作風險-orange) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：Mind Meld PR
- 🌐 案例地區：美國

**案例說明**
美國公關公司Mind Meld PR嘗試利用生成式AI自動化發送推廣信件給媒體記者，但發現AI提供的答案自信滿滿，實際上卻錯誤百出，最終放棄此應用。此例表明對外溝通若完全依賴AI，可能因錯誤訊息或資訊不準確而損及企業形象。


---

<h3 id="ai_poisoning_scams_programmer_loss">AI投毒詐騙，程式設計師損失2500美元</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![操作風險](https://img.shields.io/badge/-操作風險-orange)

**基本資訊**
- 📚 案例涉及：ChatGPT, Solana API (釣魚網站)
- 🌐 案例地區：美國
- 📋 案例年份：2024

**案例說明**
一位程式設計師在開發程式時使用ChatGPT協助生成程式碼，過程中ChatGPT推薦用戶造訪一Solana API網站，然該網站竟為釣魚網站；程式設計師於該假網站洩漏了私鑰，最終遭詐騙損失了2500美元。此案例顯示，生成式AI工具若提供第三方服務建議時，可能因模型訓練或資訊來源存疑而導向惡意站點，用戶需格外警惕並確認可信度。


---

<h3 id="nyc_gov_ai_chatbot_errors">紐約市政府聊天機器人回答錯誤百出</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![操作風險](https://img.shields.io/badge/-操作風險-orange)

**基本資訊**
- 📚 案例涉及：Microsoft Azure AI, New York City Chatbot
- 🌐 案例地區：美國
- 📋 案例年份：2024

**案例說明**
紐約市政府於2023年10月宣布使用AI改善城市服務，並推出由Microsoft Azure AI支援的聊天機器人，旨在回答城市法規相關疑問。但到了2024年，媒體報導該聊天機器人時常給出錯誤答案，市政府表示此功能仍在改善階段，建議市民仍需對照市府官網資訊確認正確性。此案例顯示大型公共服務若草率上線生成式AI，可能造成操作風險與公眾疑慮。


---

<h3 id="github_copilot_copyright_infringement">GitHub Copilot涉嫌侵犯開源軟體著作權</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![法律合規風險](https://img.shields.io/badge/-法律合規風險-orange) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：GitHub Copilot, OpenAI
- 🌐 案例地區：美國
- 📋 案例年份：2022

**案例說明**
GitHub推出的AI程式碼生成工具Copilot因涉嫌侵犯開源軟體著作權而引發一場針對技術風險的法律風波。該工具透過OpenAI模型進行訓練，使用了來自網路的公開程式碼作為資料來源，旨在協助開發人員快速生成程式碼。然而，2022年11月，GitHub、Microsoft及OpenAI被指控未經授權使用開源軟體程式碼進行模型訓練，違反了開源社群的授權條款並侵犯著作權。此一事件突顯了生成式AI在數據來源上的法律合規挑戰，尤其是如何在技術創新與法律倫理規範之間取得平衡。


---

<h3 id="stability_ai_unauthorized_image_use">Stability AI被指控未經授權使用圖片進行AI訓練</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![法律合規風險](https://img.shields.io/badge/-法律合規風險-orange)

**基本資訊**
- 📚 案例涉及：Stability AI, DeviantArt, Midjourney, Getty Images
- 🌐 案例地區：美國
- 📋 案例年份：2023

**案例說明**
2023年1月，三位插畫藝術家向加州北區法院起訴Stability AI、DeviantArt和Midjourney，指控這些公司未經同意使用他們的作品作為AI訓練模型的數據，侵犯了著作權和名譽權。同年2月，商業圖片庫Getty Images也向Stability AI提起訴訟，指出該公司未經授權使用了超過1200萬張圖片進行AI模型訓練，部分圖片的浮水印甚至遭到扭曲。此案強調生成式AI模型若涉及大量未經授權素材，恐面臨版權訴訟風險。


---

<h3 id="openai_writers_copyright_lawsuit">OpenAI面臨作家版權訴訟</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![法律合規風險](https://img.shields.io/badge/-法律合規風險-orange)

**基本資訊**
- 📚 案例涉及：OpenAI, ChatGPT
- 🌐 案例地區：美國
- 📋 案例年份：2023

**案例說明**
2023年7月，兩位作家對OpenAI提起訴訟，指控其ChatGPT模型在未經許可的情況下使用他們的作品進行訓練，涉嫌侵犯版權。此事件與其他類似訴訟（如插畫家、出版商案例）一同突顯OpenAI與其他生成式AI模型，可能因訓練數據未獲授權而引發版權糾紛。


---

<h3 id="openai_italy_gdpr_fine">OpenAI遭義大利判罰1500萬歐元</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![法律合規風險](https://img.shields.io/badge/-法律合規風險-orange)

**基本資訊**
- 📚 案例涉及：OpenAI, ChatGPT
- 🌐 案例地區：義大利
- 📋 案例年份：2024

**案例說明**
義大利資料保護局（Italian Data Protection Authority）調查發現，ChatGPT在2023年3月違反GDPR隱私規定，發生資料外洩且並未向監管機關通報，且在訓練數據使用上缺乏明確法律依據，另亦無年齡驗證機制導致13歲以下兒童可能接觸到不適當內容，判處OpenAI 1500萬歐元罰款，此為GDPR施加重大罰款之典型案例。


---

<h3 id="patagonia_unlawful_customer_data_use">Patagonia違法使用客戶資料而被起訴</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![法律合規風險](https://img.shields.io/badge/-法律合規風險-orange) ![操作風險](https://img.shields.io/badge/-操作風險-orange)

**基本資訊**
- 📚 案例涉及：Patagonia, Talkdesk
- 🌐 案例地區：美國
- 📋 案例年份：2024

**案例說明**
美國戶外服裝品牌Patagonia與AI軟體供應商Talkdesk合作，使用AI分析客戶通話內容，卻未告知客戶其對話被記錄並用於AI模型訓練。此行為違反加州隱私法，被消費者提起訴訟。案例彰顯企業若使用通話分析客戶數據，必須在政策條款中明示並獲得同意。


---

<h3 id="openai_dmca_violation_lawsuit">OpenAI面臨違反DMCA的訴訟</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![法律合規風險](https://img.shields.io/badge/-法律合規風險-orange)

**基本資訊**
- 📚 案例涉及：OpenAI, ChatGPT
- 🌐 案例地區：美國
- 📋 案例年份：2025

**案例說明**
媒體The Intercept等單位以OpenAI未經授權刪除其文章版權資訊，違反DMCA為由提告。2025年2月一名聯邦法官裁定OpenAI故意從其文章中刪除了“版權管理資訊”，違反了DMCA，認定其在網路蒐集文章訓練ChatGPT時已構成違法。這象徵生成式AI在蒐集線上資料訓練時，若未嚴守DMCA與版權管理資訊規範，將承擔法律責任。


---

<h3 id="ross_intelligence_copyright_lawsuit_loss">ROSS Intelligence版權訴訟宣判敗訴</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![法律合規風險](https://img.shields.io/badge/-法律合規風險-orange)

**基本資訊**
- 📚 案例涉及：ROSS Intelligence, Westlaw (Thomson Reuters)
- 🌐 案例地區：美國
- 📋 案例年份：2025

**案例說明**
提供AI法律服務的ROSS Intelligence，在訓練AI模型時使用了Thomson Reuters旗下知名的Westlaw法律資料庫內容（Thomson曾拒絕授權予ROSS）。法院認定，Westlaw整理與摘要過的內容享有版權保護，而非公共領域資料，最終於2025年2月宣判ROSS Intelligence敗訴。此案例突顯整理與摘要編輯後的資料可附有版權，AI訓練若違規使用恐面臨相關法律風險。


---

<h3 id="microsoft_tay_racism">微軟人工智慧機器人Tay被教導種族歧視</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![道德與社會風險](https://img.shields.io/badge/-道德與社會風險-orange) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：Microsoft Tay
- 🌐 案例地區：美國
- 📋 案例年份：2016

**案例說明**
微軟2016年推出聊天機器人Tay，原旨在與網友互動並學習語言。然而，Tay很快便受到網友的操控，在短短幾小時內開始發布充滿仇恨和歧視的言論，包括希特勒思想和對社會弱勢群體的侮辱。這些行為引發了廣泛的公眾譴責，最終微軟被迫下架Tay，並對其無法控制的行為負起責任。該事件突顯開放式AI互動平台易受惡意操控，也揭示了道德與社會風險的重要性。


---

<h3 id="meta_blenderbot3_bias_trolling">Meta BlenderBot 3在對話中出現偏見與嘲諷</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![道德與社會風險](https://img.shields.io/badge/-道德與社會風險-orange) ![技術風險](https://img.shields.io/badge/-技術風險-orange)

**基本資訊**
- 📚 案例涉及：Meta BlenderBot 3
- 🌐 案例地區：美國
- 📋 案例年份：2022

**案例說明**
Meta研發的AI聊天機器人BlenderBot 3，原意在透過與人不斷對話學習，進而展現更自然流暢的語言能力。然而在實際測試過程中，用戶發現BlenderBot 3的回覆不僅充滿偏見與負面情緒，甚至直接嘲諷Meta執行長馬克·祖克伯(Mark Zuckerberg)，並鼓勵使用者刪除Facebook。此同微軟案例顯示，生成式AI若完全依賴從網路或用戶互動中「自我學習」，可能在未受控的情況下吸收並放大偏見、仇恨或不良內容。


---

<h3 id="unitedhealth_ai_decision_lawsuit">聯合健康集團因AI模型錯誤決策被控告</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![道德與社會風險](https://img.shields.io/badge/-道德與社會風險-orange)

**基本資訊**
- 📚 案例涉及：UnitedHealth Group
- 🌐 案例地區：美國
- 📋 案例年份：2022

**案例說明**
聯合健康集團（UnitedHealth Group）因使用錯誤率高達90%的AI模型進行保險決策而被控告，該模型導致部分老年患者無法獲得應有的醫療服務，其中包括兩名患者過世。家屬指控該公司在明知模型不準確的情況下仍選擇使用，並提起訴訟，指責其忽視基本倫理責任。事件最終迫使聯合健康停用該模型，但已對其聲譽和社會信任造成嚴重影響，突顯了AI應用中對道德與社會責任的忽視可能帶來的深遠後果。


---

<h3 id="koko_platform_unethical_psych_advice">Koko平台使用AI提供心理建議被批評不道德</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![道德與社會風險](https://img.shields.io/badge/-道德與社會風險-orange)

**基本資訊**
- 📚 案例涉及：Koko, ChatGPT
- 🌐 案例地區：美國
- 📋 案例年份：2023

**案例說明**
美國線上平台Koko提供用戶匿名討論心理健康問題的服務。其創辦人承認，部分支援和建議是使用ChatGPT生成，再由人類編輯後發送。在未經用戶同意的情況下使用AI提供心理建議，被視為不道德的應用，引發學者和同行的批評。隨後，Koko停止導入生成式AI技術。


---

<h3 id="sports_illustrated_ai_article">美國運動畫刊Sports Illustrated刊登AI撰寫文章</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![道德與社會風險](https://img.shields.io/badge/-道德與社會風險-orange)

**基本資訊**
- 📚 案例涉及：Sports Illustrated, AdVon Commerce
- 🌐 案例地區：美國
- 📋 案例年份：2023

**案例說明**
Sports Illustrated與第三方內容提供商AdVon Commerce合作，AdVon卻遭揭露文章其實是由AI撰寫，甚至創造虛構作者及頭像。讀者發現後大感不滿，文章被緊急下架，Sports Illustrated的出版商Arena Group執行長亦遭解僱。此事顯示若媒體或平台在內容生產上不透明，可能引發讀者信任危機與道德爭議。


---

<h3 id="character_ai_suicide_lawsuit">Character.ai因14歲少年自殺被告</h3>

![國際](https://img.shields.io/badge/-國際-blue) ![道德與社會風險](https://img.shields.io/badge/-道德與社會風險-orange)

**基本資訊**
- 📚 案例涉及：Character.ai, Google
- 🌐 案例地區：美國
- 📋 案例年份：2023

**案例說明**
Character.ai提供可自訂角色的聊天機器人服務，美國一名14歲少年在使用過程中多次表露自殘與自殺念頭，最終不幸走上絕路。少年的母親認為該AI讓兒子沉迷，且未主動預警或防止自殺意圖，故對Character.ai與提供技術商Google提告。此案顯示針對心理健康領域的AI服務，若缺乏適當安全機制與緊急應對功能，可能引發嚴重道德風險。
