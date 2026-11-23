# Wiki 建置實際需求說明（不需課堂 Agent 專案）

這份成果由五篇上傳 PDF 建立。程序為：

1. 先使用 `scripts/ingest_wiki.py` 讀入五篇 PDF，得到可搜尋的頁級私有索引。
2. 依檢索內容，寫出 `knowledge/P1~P5` 知識卡、來源對照、各系統層級。
3. 使用 Wiki 反向檢查：FOVEA 是否為 Sensor readout？RPR 節省何種流量？TuMag ROI 在哪個階段裁切？
4. 公開以 `docs/wiki.html` 呈現五篇可搜尋卡片、來源位置與 Q&A。 

這是 LLM 輔助建立的專屬知識庫成果。公開網頁是靜態 Wiki，不提供付費模型 API 問答；全文 PDF 只保存於私人資料夾。
