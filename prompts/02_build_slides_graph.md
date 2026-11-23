# Graph 驅動的教學簡報產生與檢查規則

此文件記錄本次實際採用的 AI 輔助工作規格。專案已完成兩個 HTML 版本；此文件也可供後續重製或修改。

## V1 Graph

`PDF ingest → Wiki 檢索 → 教學目標／大綱 → 段落整理 → 12 頁 HTML V1 → Basic Gate（來源覆蓋、HTML 翻頁） → V1 成品`。

失敗時回到教學目標與整理階段。V1 是可以真正教學的完整版本，不能故意塞假數字或亂寫原文。

## V1 Review（實際版本觀察）

- 原文來源完整，但部分跨論文比較仍需要明確記錄輸入、輸出及資料減量位置。
- 有 ROI 和研究原理，但讀者需要情境推演、互動例子和迷思檢查。
- 需要將基本 HTML 驗證提升為瀏覽器、手機與互動測試。

## V2 Graph

`Sources → Retrieve → Coverage Gate → Outline → Teaching Gate → HTML Render → Browser Gate → Publish`。

條件回路：
- Coverage FAIL：回到原文檢索，補充 Claim / Paper / PDF page 映射。
- Teaching FAIL：回到大綱，補資料層級圖、案例或教學題。
- Browser FAIL：回 HTML 排版，修正導航、連結、螢幕適配和計算互動。

## 實作與驗證

1. 兩版完整 HTML 已產出：V1 12 頁、V2 16 頁。
2. `scripts/run_graph.py` 對實際 HTML 進行可重跑的內容 Gate 稽核。
3. 瀏覽器檢查見 `reports/browser-check-updated.md`。
4. 這是 AI 輔助編輯 + 本機確定性查核的實作，不宣稱已執行自主雲端 LLM Agent API。
