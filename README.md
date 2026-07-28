# 💼 LinkedIn 職涯寫作顧問 (LinkedIn Career Writing Consultant)
這是一個基於生成式 AI 的 Web 應用程式，旨在協助專業人士將職場經驗與日常挑戰，自動轉化為具備啟發性且結構完整的 LinkedIn 草稿貼文。
## 🔗 專案連結: [[點擊這裡立即使用](https://linkedinadvisorweb.onrender.com)]

## 🛠️ 技術面
* **前端介面**: Gradio (Web UI 框架)
* **後端語言**: Python
* **AI 模型**: Llama-3.3-70b (via Groq API)
* **API 整合工具**: aisuite
* **部署雲端**: Render (CI/CD 自動化部署)

## 💡 功能特色與解決方案
* **精準的 Prompt Engineering**: 內建系統提示詞，加上負面提示詞約束，確保 AI 穩定輸出「台灣職場專業語氣」且以「第一人稱」撰寫。
* **結構化輸出**: 強制 AI 產出具備「開頭 Hook 吸引讀者」、「中段事件反思」與「結尾行動呼籲 (CTA)」三大結構的高品質內容。
* **環境變數配置**: 實作程式碼與機密設定分離，透過 Render 後台管理 API Key，達成 24 小時安全在線運行。
