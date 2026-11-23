# 第七週作業 1110｜最終繳交說明（請複製貼上）

> 這份內容以已完成的新版 GitHub-ready 成品為準。貼到課堂作業之前，請將以下兩個佔位字串替換為你實際發布的網址：`【你的 GitHub Pages 網址】`、`【你的 GitHub Repository 網址】`。本機已完成的測試與尚未執行的 GitHub 遠端發布分開敘述。

## 1. LLM Wiki 主題與簡短介紹

我選擇的主題是「從 Foveated Imaging 到 FPGA Buffer：影像資料到底在哪裡變少？」。這個主題與我近期在閱讀的智慧影像感測與 FPGA 影像緩衝研究有關。我整理了五篇原始論文：VisionMode（Sensor 與 ISP）、FOVEA（軟體非均勻重取樣）、Rhythmic Pixel Regions（SoC 記憶體流量）、TuMag Camera（FPGA 多通道資料重排與 ROI 輸出）及 D-SWIM（可變尺寸的 FPGA Line Buffer）。希望讓初學者看懂同樣叫做 ROI 或「減少影像資料」，其實可能作用在 Sensor、Software、DRAM 或 FPGA 等不同位置。

## 2. LLM Wiki 連結與成果

這次實際讀入五篇原始 PDF，分別是 10、10、14、18、20 頁，共 72 頁，建立可依頁碼查詢的私人索引，並將研究問題、處理階段、主要做法、限制與原文來源整理為五篇中文知識卡。公開 Wiki 支援關鍵字搜尋、原文連結及跨論文的概念查核，也有 `AGENTS.md` 規範資料 ingest、引用、更新與產出方式。

- LLM Wiki 公開成果：【你的 GitHub Pages 網址】/wiki.html
- GitHub Repository：【你的 GitHub Repository 網址】

本次使用 AI 協助整理建立專屬知識庫；公開網站是**可搜尋的靜態 Wiki**，沒有串接即時 LLM 問答 API。五篇 PDF 全文只保存在私人備份，未公開到 GitHub。

## 3. 教學 HTML 簡報連結

我先完成**12 頁可以獨立教學的 V1**：從高解析度影像的資料成本、ROI 概念與影像資料流程開始，依序介紹五篇論文，最後比較各種方法的工作層級與限制。V1 並非刻意做得不完整，也沒有故意加入錯誤的論文數據。

檢查 V1 後，再修訂成 **16 頁 V2**。V2 新增四個資料處理層級的地圖、同一個交通情境的逐步分析、Input/Output 對照、ROI 可互動的理論取樣試算，以及三題常見誤解判斷。整份簡報可在瀏覽器中使用按鈕或左右方向鍵翻頁。

- V2 最終教學簡報：【你的 GitHub Pages 網址】/slides.html
- V1 第一版教學簡報：【你的 GitHub Pages 網址】/slides-v1.html

## 4. Graph / Loop 設計與流程說明

這次選用 **Graph** 作為主要工作流程表示法，因為 Graph 裡已經包含 FAIL 時返回前面節點的回路，所以能同時呈現 Loop。

V1 的流程為：`PDF / Wiki → 教學目標與大綱 → 原文檢索與重點整理 → 產生 12 頁 V1 HTML → 基本檢查 → 輸出`。原本也設計了檢查失敗後回到大綱修正的路徑，但檢查較偏向來源有無涵蓋與頁面能否使用。

檢視 V1 後，我將 V2 改成：`Ingest → Retrieve → Coverage Gate → Outline → Teaching Gate → HTML Render → Browser Gate → Publish`。其中 Coverage Gate 要求重要主張有原文頁碼、Teaching Gate 檢查新手是否會混淆 Sensor 與後段資料處理、Browser Gate 檢查翻頁、互動、連結與不同螢幕。如果 Gate 不通過，就回到對應的資料或 HTML 節點修改，再重新檢查。

- V1 / V2 Graph 與詳細修改原因：【你的 GitHub Pages 網址】/workflow.html
- 工作流程規則：Repository 的 `AGENTS.md`
- 可重跑的 Graph 檢查與結果：`scripts/run_graph.py`、`reports/graph-execution.md`

## 5. 一次實際執行與檢查結果

我使用五篇 PDF 執行文字解析，確認共 72 頁，並保留 SHA-256、頁級索引和原文查核紀錄。接著執行 `scripts/run_graph.py` 對兩版 HTML 的內容進行確定性檢查：V1 12 頁已通過原定的基本 Gate，證明第一版能獨立教學；但在後續更嚴謹的檢查中，發現尚缺少更明確的層級辨析、情境練習與互動檢核，所以將這些改善成 V2。V2 16 頁通過基本 Gate 及進階教學 Gate。

此外，我使用 Chromium / Playwright 實際渲染 HTML，檢查首頁四個入口順序、Wiki 搜尋、兩版簡報翻頁、鍵盤操作、ROI Slider 計算及手機版等，共 **34 項檢查通過（34/34）**。紀錄與畫面截圖都放在 Repository 的 `reports/`、`evidence/`。

> 本次的 Graph 執行紀錄是本機 Python 的內容檢查與瀏覽器測試，並非雲端 LLM Agent 自動反覆呼叫模型的執行紀錄；遠端 GitHub Pages 發布後的最終連線仍需另外確認。

## 6. 反思：最容易出錯的節點與如何改善

這次我認為最容易出錯的是「文獻證據整理成教學內容」的過程。五篇論文都有提到提高影像處理效率，但節省的資源與發生的階段不同。例如 FOVEA 是取得影像後的 Warp，RPR 主要改善寫入及讀取 DRAM 的資料流量，而 TuMag 必須先把 Sensor 八通道資料用 FIFO 排序，才能在後續 image_tx 控制欄位輸出。如果只整理關鍵字或看最後的輸出結果，很容易把「後段少傳資料」當成「Sensor 一開始就少讀資料」。

V1 雖然介紹了五篇論文，但比較偏向依論文逐篇說明；對不熟悉 Sensor 與 FPGA 的同學來說，可能還是難以辨認這些方法的邊界。因此，我在 V2 的 Graph 裡加入 Evidence Coverage Gate 和 Teaching Gate，要求每個主張能對回原文，並用資料層級圖、實際場景、ROI 試算與迷思檢查把問題具體化。另外也加入 Browser Gate，因為簡報內容正確還不夠，瀏覽器裡能否順利翻頁與操作也影響教學效果。這次讓我理解 Graph / Loop 的重點，是在重要步驟設下能檢查的條件，發現問題時回到正確的位置修正，而不是單純重新生成整份內容。
