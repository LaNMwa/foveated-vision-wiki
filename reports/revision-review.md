# V1 → V2 內容設計與修訂紀錄

## 先做完整 V1

V1 含 12 頁：問題動機、ROI、相機資料流程、VisionMode、FOVEA、RPR、TuMag、D-SWIM、五篇比較、跨層級整合、結語與來源。它本身可獨立教學，也能用鍵盤切頁。保留每篇的基本引用和限制說明，**沒有故意加入錯誤論文數字**。

## 檢視後發現的改進機會

1. **Evidence/Coverage：** 來源雖齊全，還缺少「每個關鍵主張使用哪個段落」的 Gate。V2 補充跨論文對照時的 Input、Output、節省位置及 PDF 位置。
2. **Teaching：** 五篇逐一介紹之後，仍需要「四個系統層級」與同一個交通場景，幫初學者記住各篇工作的階段。V2 新增第 2、8、9 頁。
3. **Practice：** V1 偏重讀者理解，缺乏主動操作與自我檢測。V2 新增 ROI 數學試算、三題常見混淆判斷與設計前四問。所有互動模型都標示為假設示例。
4. **Browser：** V1 Gate 只檢查基本 HTML / 引用；V2 新增實際瀏覽器檢查：翻頁、鍵盤、連結、ROI 控件與手機版。

## Graph 改動

- **V1**：Sources → Outline → Retrieve → HTML V1 → Basic Quality Gate（FAIL 回 Outline）→ Export。
- **V2**：Sources → Retrieve → Coverage Gate（FAIL 回 Retrieve）→ Outline → Teaching Gate（FAIL 回 Outline）→ Render HTML → Browser Gate（FAIL 回 Render）→ Publish。

## 判讀限制

這是對實際產出的兩個 HTML 版本進行比較，以及可重跑的 Python/瀏覽器檢查；不是已上線的自主 LLM Agent 的執行記錄。
