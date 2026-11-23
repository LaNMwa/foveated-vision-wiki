# 五篇已讀 PDF 的證據對照表

**PDF p.X** 指 PDF 檢視器由 1 起算的頁碼，可能和論文印刷頁碼不同。

| 來源 | 核心摘要 | 原始 PDF 位置 | 核對技術詞 | 系統邊界 |
|---|---|---|---|---|
| P1 | 較低解析度/量化精度與 ISP 低功耗模式 | PDF p.1 | Adjustable resolution, ADC, ISP | 感測端與 ISP 設計層級 |
| P2 | 由 saliency/歷史偵測引導影像 warping、輸出座標反映射 | PDF p.1–2 | Warps full captured frames | 軟體處理；不證明 Sensor 少讀像素 |
| P3 | 標準 raster scan 輸入，選擇性編碼後降低記憶體流量 | PDF p.1–2 | Ingests commercial sensor streams | 43–64% 是論文平台的 memory/interface 數值 |
| P4 | 8 通道讀入、even/odd FIFO 重排，再由 image_tx 限制欄 ROI | PDF p.3, p.8–10, p.12–13 | image_tx cropping multiples of 8 columns | 輸出減少不等於重排 FIFO 前減少 |
| P5 | 可程式化 line buffer 支援動態影像尺寸 | PDF p.1–2, p.8–13 | D-SWIM run-time programming | 不是 Sensor-level selective readout |

這份對照以使用者提供的五份 PDF 為基礎。任何新增的數值需回查原文，不能把跨研究的省電百分比直接相加。
