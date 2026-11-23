# 本機 Chrome 瀏覽器測試（新版本）

使用 Chromium Playwright 將 HTML 注入頁面測試；此執行環境禁止 file:// 與本機 HTTP 導航，因此對檔案 href 進行靜態存在檢查，並測試所有 JS 控件與網站的實際渲染。這**不等於** GitHub Pages 已遠端部署。

- PASS · desktop load index.html — Foveated Vision Wiki · 第七週作業完整成果
- PASS · four home cards in required order — LLM Wiki 的成果 / 使用的 Graph 設計與改進 / 完整版教學式簡報（V2） / 第一版完整簡報（V1）
- PASS · all four navigation targets exist — ['wiki.html', 'workflow.html', 'slides.html', 'slides-v1.html']
- PASS · desktop load wiki.html — LLM Wiki 的成果 | Foveated Vision Wiki
- PASS · wiki shows five source cards — 
- PASS · wiki can filter source cards — 
- PASS · desktop load workflow.html — Graph 工作流程與修訂依據 · Foveated Vision Wiki
- PASS · both graph SVGs shown — 
- PASS · three actionable gates named — 
- PASS · desktop load slides-v1.html — V1 · 第一版完整教學 · Foveated Vision Wiki
- PASS · slides-v1.html page count — 12 actual slides
- PASS · slides-v1.html references five original papers — 
- PASS · slides-v1.html button navigation — 01 / 12 → 02 / 12
- PASS · slides-v1.html keyboard navigation — 
- PASS · slides-v1.html back to first page — 
- PASS · slides-v1.html no accidental horizontal overflow — 
- PASS · desktop load slides.html — V2 · 修訂版完整教學 · Foveated Vision Wiki
- PASS · slides.html page count — 16 actual slides
- PASS · slides.html references five original papers — 
- PASS · slides.html button navigation — 01 / 16 → 02 / 16
- PASS · slides.html keyboard navigation — 
- PASS · slides.html back to first page — 
- PASS · slides.html no accidental horizontal overflow — 
- PASS · V2 has three interactive ROI controls — 
- PASS · V2 interactive sample calculation updates — 90.0% → 82.5%
- PASS · V2 three misconceptions have answers — 
- PASS · desktop JavaScript errors — []
- PASS · mobile load index.html — 
- PASS · mobile homepage no page-wide overflow — 
- PASS · mobile load slides-v1.html — 
- PASS · mobile slides-v1.html flip pages — 01 / 12 → 02 / 12
- PASS · mobile load slides.html — 
- PASS · mobile slides.html flip pages — 01 / 16 → 02 / 16
- PASS · mobile Javascript errors — []

總計 34/34；各頁垂直內容尺寸詳見 `browser-check-updated.json`（較長頁使用內部捲動）。
