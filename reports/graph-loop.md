# 本次採用 Graph（內含 Loop / 失敗回路）

請參考公開網站 `docs/workflow.html`，包含兩版完整圖、State 與修改原因。Graph 一種圖即可，帶條件返回箭頭就是 Loop。

## V1 Graph

```mermaid
flowchart LR
  A[5 篇 PDF / Wiki] --> B[教學目標與大綱]
  B --> C[檢索 / 歸納]
  C --> D[完整 12 頁 HTML V1]
  D --> E{基本檢查: 來源覆蓋與 HTML?}
  E -- FAIL --> B
  E -- PASS --> F[輸出 V1]
```

## V2 Graph

```mermaid
flowchart TD
 A[Ingest 5 PDFs] --> B[Retrieve 原文證據]
 B --> C{Coverage Gate: Claim 有依據?}
 C -- FAIL --> B
 C -- PASS --> D[Outline: 初學者教學順序]
 D --> E{Teaching Gate: 層級和案例清楚?}
 E -- FAIL --> D
 E -- PASS --> F[Generate HTML + Render]
 F --> G{Browser Gate: 功能與可讀性?}
 G -- FAIL --> F
 G -- PASS --> H[輸出 V2 / 檢查報告]
```

## 實作限制

本次是 AI 協助整理、人工編排與 Python/Browser 的確定性檢查流程，沒有實際部署 LLM Agent 模型呼叫 API。
