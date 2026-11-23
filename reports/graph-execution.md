# Graph QA：兩版真實 HTML 成品檢查結果

以 `python scripts/run_graph.py --root .` 檢查目前的 HTML 檔案，並產生本報告。

**性質：確定性 Python 稽核**，並非 AI Agent 已自主反覆呼叫模型生成。

## V1（12 頁）

V1 的基本品質 Gate **PASS**，已是完整教學版本：

- PASS: `complete_tutorial_10_or_more_slides`
- PASS: `five_original_papers_referenced`
- PASS: `page_specific_source_markers`
- PASS: `navigation_controls_present`
- PASS: `teaching_explanation_of_all_five`

後續擴大檢查標準時，觀察到可以增進教學的內容：

- NEEDS_REVISION: `four_processing_layers_explicit`
- NEEDS_REVISION: `input_output_layer_comparison`
- NEEDS_REVISION: `guided_realistic_case`
- NEEDS_REVISION: `roi_interactive_model_and_assumptions`
- NEEDS_REVISION: `misconception_self_checks`

這不是故意做錯論文或將 V1 評分當作 0；V1 通過初版規格，在第二輪更嚴謹的教學檢查中確認改善方向。

## V2（16 頁）

進階 Gate **PASS**：

- PASS: `four_processing_layers_explicit`
- PASS: `input_output_layer_comparison`
- PASS: `guided_realistic_case`
- PASS: `roi_interactive_model_and_assumptions`
- PASS: `misconception_self_checks`

V2 的基本 Gate：PASS。

## 回饋與修訂

- G1 文獻可信度：對照 PDF 頁碼、五篇重要主張，防止把 Sensor readout 與後段 DRAM/FPGA 優化混淆。
- G2 教學順序：加入明確資料層級、情境案例、ROI 理論試算與誤解檢查。
- G3 HTML 品質：由真實 Chromium 測試翻頁、控制項、手機與網頁連結，詳見 `browser-check-updated.md`。

版本差異詳見 `reports/revision-review.md`。未實際發生之 LLM Agent 自動重試不列入測試紀錄。
