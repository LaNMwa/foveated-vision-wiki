# Foveated Vision Wiki — 第七週作業完整版（修訂）

> 主題：從 Foveated Imaging 到 FPGA Buffer：影像資料在哪裡變少？

## 公開網站四個入口

1. **LLM Wiki 的成果** → `docs/wiki.html`（5 篇文獻卡與關鍵字查詢）
2. **Graph 設計與改進** → `docs/workflow.html`（V1 Graph、實際檢查與 V2 Graph）
3. **完整版教學式簡報 V2** → `docs/slides.html`（16 頁與 ROI 互動試算）
4. **第一版完整教學簡報 V1** → `docs/slides-v1.html`（12 頁）

## GitHub Pages 發布

將此資料夾所有檔案放到 Repository 根目錄（**不要**放五份原始 PDF），然後前往 **Settings → Pages → Deploy from a branch → main → /docs**。首頁連結是 `https://<帳號>.github.io/<Repository>/`，若是 `<帳號>.github.io` repository 則在根網址。此處的網頁檔案都是自包含 CSS/JS，GitHub Pages 不需要額外的 build。

## Wiki 的建立與程式

五篇 PDF 在私人工作環境解析共 72 頁，採頁級索引、來源 metadata 與知識卡。`knowledge/` 有五篇摘要與來源限制，`AGENTS.md` 定義使用與更新規範。`scripts/ingest_wiki.py` 可用五篇原始 PDF 再執行索引。公開頁面是**靜態可搜尋 Wiki，不提供即時 LLM API 問答**。

## 版本改善

V1 是 12 頁完整教學作品。V2 根據 `reports/revision-review.md` 的四類檢查，增補證據位置、教學層級、互動試算與查核練習。兩版工作流程皆見 `docs/workflow.html`。`scripts/run_graph.py` 提供可重跑的確定性驗證，而非自主 Agent 執行。

## 作業繳交

直接開啟 `reports/submission-text.md` 複製六個段落；替換發布後的 GitHub Pages 網址。操作步驟另見 `README.md` 和完整包的 `04_上傳GitHub與繳交步驟.md`。
