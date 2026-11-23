# AGENTS.md — Foveated Vision Wiki 知識庫維護規則

## 專案目標
以五篇原始 PDF 構建可查核的 Wiki，將其轉成適合初學者的 HTML 簡報，透過 Graph / Loop 改進初稿的證據與教學品質。

## 資料與介面
- 私有來源資料：五篇 PDF 與 `wiki_index.json`（不應公開到 GitHub）。
- 公開 Wiki：`knowledge/` 的中文知識卡與 `docs/wiki.html` 的搜尋展示。
- 教學產物：`docs/slides-v1.html` 與 `docs/slides.html`。
- 實際檢查：`scripts/ingest_wiki.py`、`scripts/run_graph.py`、`reports/`。

## 工作規則
1. Ingest：讀取五篇 PDF、驗證頁數及 SHA256；每篇依 PDF p.1 起算的頁碼索引，不可用檔名替代 ingest 證據。
2. Retrieve：查詢原始 PDF 的相關頁面，記下論文 ID、頁碼、主張與引用，不足時標示待查核。
3. Normalize：將研究問題、I/O、系統層級、優點與限制寫進 `knowledge/` 知識卡。
4. Draft：先產 V1，建立簡報大綱與每個論點的來源對照。
5. Check：至少通過五篇來源覆蓋、層級區分、初學者教學內容、翻頁/互動功能四項檢查。
6. Loop：若 Check FAIL，登記 `issue_id`、原因、回查頁面、修訂項目，再檢查 V2。
7. Publish：只將允許公開的文字、HTML、程式和測試紀錄推送 GitHub；論文 PDF/全文索引留在私人資料夾。

## 研究概念的硬規則
- FOVEA ＝影像已取得後的非均勻 resampling / warping，不可說成原論文實作了 sensor pixel selective readout。
- RPR ＝對商用 sensor raster input 進行後續編碼來節省記憶體流量，不可無條件宣稱降低了 sensor 端輸出流量。
- TuMag ＝八通道輸入、FPGA FIFO 重排；欄方向 ROI 處理在 image_tx，不能說前級 FIFO 自動少寫相同百分比。
- D-SWIM ＝支援變尺寸輸入的 FPGA line buffer，不是節能型影像感測器。
- 跨研究各自報告的能耗/traffic 數字不得相加。教學 ROI slider 是假設模型，不是真實晶片量測。
